import atexit
import os
import shutil
import warnings

import streamlit as st

# Ukryj ostrzeżenia deprecation dla lepszego UX
warnings.filterwarnings("ignore", category=DeprecationWarning)

try:
    import google.generativeai as genai
    from dotenv import load_dotenv
    from langchain.chains.question_answering import load_qa_chain
    from langchain.prompts import PromptTemplate
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import FAISS
    from langchain_google_genai import (
        ChatGoogleGenerativeAI,
        GoogleGenerativeAIEmbeddings,
    )
    from PyPDF2 import PdfReader
except ImportError as e:
    st.error(f"Błąd importu: {str(e)}. Sprawdź czy wszystkie wymagane pakiety są zainstalowane.")
    st.stop()

INDEX_FOLDER = "faiss_index"


def clean_faiss_index():
    if os.path.exists(INDEX_FOLDER):
        try:
            shutil.rmtree(INDEX_FOLDER)
            print(f"Folder {INDEX_FOLDER} został usunięty po zakończeniu programu.")
        except Exception as e:
            print(f"Nie udało się usunąć folderu {INDEX_FOLDER}: {e}")


atexit.register(clean_faiss_index)
#

load_dotenv()

# Sprawdź czy klucz API jest dostępny
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Brak klucza API Google. Sprawdź plik .env")
    st.stop()

genai.configure(api_key=api_key)


def get_pdf_text(pdf_docs):
    text = ""
    try:
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:  # Sprawdź czy tekst nie jest pusty
                    text += page_text
    except Exception as e:
        st.error(f"Błąd podczas czytania pliku PDF: {str(e)}")
        print(f"Error in get_pdf_text: {e}")
    return text


def get_text_chunks(text):
    # Optymalizacja dla dużych dokumentów
    if len(text) > 100000:  # Jeśli tekst jest bardzo długi
        chunk_size = 1500
        chunk_overlap = 300
        st.info("📄 Wykryto duży dokument - używam większych fragmentów dla lepszej wydajności")
    else:
        chunk_size = 1000
        chunk_overlap = 200

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap, separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(text)
    st.info(f"📊 Utworzono {len(chunks)} fragmentów tekstu")
    return chunks


def get_vector_store(text_chunks):
    try:
        if not text_chunks:
            st.error("Brak tekstu do przetworzenia. Sprawdź czy pliki PDF zawierają tekst.")
            return

        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")

    except Exception as e:
        st.error(f"Błąd podczas tworzenia indeksu wektorowego: {str(e)}")
        print(f"Error in get_vector_store: {e}")


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    # model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-002", temperature=0.3
    )  # Use gemini-1.5-pro for better performance

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain


def user_input(user_question):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        # Sprawdź czy indeks FAISS istnieje
        if not os.path.exists("faiss_index"):
            st.error("Brak indeksu FAISS. Najpierw prześlij i przetwórz pliki PDF.")
            return

        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(
            user_question, k=3
        )  # Pobierz 3 najbardziej podobne fragmenty

        chain = get_conversational_chain()

        response = chain(
            {"input_documents": docs, "question": user_question}, return_only_outputs=True
        )

        print(response)
        st.write("**Odpowiedź:**")
        st.write(response["output_text"])

        # Pokaż źródła (opcjonalnie)
        with st.expander("📚 Pokaż fragmenty źródłowe"):
            for i, doc in enumerate(docs, 1):
                st.write(f"**Fragment {i}:**")
                st.write(
                    doc.page_content[:300] + "..."
                    if len(doc.page_content) > 300
                    else doc.page_content
                )
                st.write("---")

    except Exception as e:
        st.error(f"Wystąpił błąd podczas przetwarzania pytania: {str(e)}")
        print(f"Error in user_input: {e}")


def main():
    st.set_page_config("Wieloplikowy chatbot PDF", page_icon=":scroll:")
    st.header("Wiele plików PDF📚 - Agent czatu 🤖 ")

    # Sprawdź status indeksu FAISS
    if os.path.exists("faiss_index"):
        st.success("✅ Indeks FAISS gotowy - możesz zadawać pytania!")
    else:
        st.info("ℹ️ Najpierw prześlij i przetwórz pliki PDF, aby móc zadawać pytania.")

    user_question = st.text_input("Zadaj pytanie z przesłanych plików PDF .. ✍️📝")

    if user_question:
        user_input(user_question)

    with st.sidebar:

        st.image("img/logo.jpg")
        st.write("---")

        st.title("📁 Sekcja pliku PDF")
        pdf_docs = st.file_uploader(
            "Prześlij swoje pliki PDF i \n Kliknij przycisk Prześlij i przetwórz ",
            accept_multiple_files=True,
            type=["pdf"],
            help="Obsługiwane są tylko pliki PDF",
        )
        if st.button("Prześlij i przetwórz"):
            if pdf_docs:
                with st.spinner("Przetwarzanie..."):  # user friendly message.
                    raw_text = get_pdf_text(pdf_docs)  # get the pdf text
                    if raw_text.strip():  # Sprawdź czy udało się wyekstraktować tekst
                        text_chunks = get_text_chunks(raw_text)  # get the text chunks
                        get_vector_store(text_chunks)  # create vector store
                        st.success("Przetwarzanie zakończone pomyślnie!")
                    else:
                        st.error(
                            "Nie udało się wyekstraktować tekstu z plików PDF. Sprawdź czy pliki zawierają tekst."
                        )
            else:
                st.warning("Najpierw wybierz pliki PDF do przesłania.")

        st.write("---")
        st.image("img/Robot.jpg")
        st.write("Asystent PDF_Gemini")  # add this line to display the image

    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px; text-align: center;">
            © <a href="https://github.com/Darek1966/Asystent_PDF_Gemini.git" target="_blank">Darek1966</a> | Made by Darek1966
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
