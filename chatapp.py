import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
# Dodałem usuwanie foldera faiss_index, jeśli istnieje
import atexit
import shutil

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
# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    # model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-002", temperature=0.3)  # Use gemini-1.5-pro for better performance

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain



def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    # new_db = FAISS.load_local("faiss_index", embeddings)s
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True) # dodałem allow_dangerous_deserialization=True, aby uniknąć błędu deserializacji

    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])




def main():
    st.set_page_config("Wieloplikowy chatbot PDF", page_icon = ":scroll:")
    st.header("Wiele plików PDF📚 - Agent czatu 🤖 ")

    user_question = st.text_input("Zadaj pytanie z przesłanych plików PDF .. ✍️📝")

    if user_question:
        user_input(user_question)

    with st.sidebar:

        st.image("img/logo.jpg")
        st.write("---")
        
        st.title("📁 Sekcja pliku PDF")
        pdf_docs = st.file_uploader("Prześlij swoje pliki PDF i \n Kliknij przycisk Prześlij i przetwórz ", accept_multiple_files=True)
        if st.button("Prześlij i przetwórz"):
            with st.spinner("Przetwarzanie..."): # user friendly message.
                raw_text = get_pdf_text(pdf_docs) # get the pdf text
                text_chunks = get_text_chunks(raw_text) # get the text chunks
                get_vector_store(text_chunks) # create vector store
                st.success("Zrobione")
        
        st.write("---")
        st.image("img/Robot.jpg")
        st.write("Asystent PDF_Gemini")  # add this line to display the image


    st.markdown(
        """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #0E1117; padding: 15px; text-align: center;">
            © <a href="https://github.com/Darek1966/Asystent_PDF_Gemini.git" target="_blank">Darek1966</a> | Made by Darek1966
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
