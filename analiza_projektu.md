# Analiza struktury projektu "Asystent PDF"

## Ogólny opis projektu

Projekt "Asystent PDF" to aplikacja umożliwiająca zadawanie pytań dotyczących zawartości dokumentów PDF. Aplikacja wykorzystuje technologie sztucznej inteligencji do analizy treści dokumentów i udzielania odpowiedzi na pytania użytkownika na podstawie zawartości tych dokumentów.

## Struktura plików

Projekt składa się z następujących głównych plików:

1. **application.py** - główny plik aplikacji zawierający logikę działania programu
2. **requirements.txt** - lista zależności projektu
3. **README.md** - dokumentacja projektu z instrukcjami uruchomienia
4. **embeddings_creation.ipynb** - notebook Jupyter pokazujący proces tworzenia osadzań (embeddings)
5. **how it works/chat_with_multipdf.png** - grafika ilustrująca działanie aplikacji
6. Pliki konfiguracyjne: `.gitignore`, `.python-version`, `.env.example`

## Technologie i zależności

Projekt wykorzystuje następujące główne technologie i biblioteki:

1. **Streamlit** - do tworzenia interfejsu użytkownika
2. **LangChain** - framework do budowania aplikacji opartych na LLM
3. **OpenAI** - do generowania odpowiedzi i tworzenia osadzań
4. **FAISS** - do efektywnego przechowywania i wyszukiwania wektorów
5. **PDFPlumber** - do ekstrakcji tekstu z plików PDF
6. **Python-dotenv** - do zarządzania zmiennymi środowiskowymi

## Przepływ danych i logika aplikacji

Aplikacja działa według następującego schematu:

1. **Wczytywanie dokumentów PDF**:

   - Użytkownik przesyła pliki PDF przez interfejs Streamlit
   - Funkcja `get_pdf_text()` ekstrahuje tekst z dokumentów za pomocą PDFPlumber
2. **Przetwarzanie tekstu**:

   - Funkcja `get_text_chunks()` dzieli tekst na mniejsze fragmenty (chunks) o określonej długości
   - Wykorzystywany jest CharacterTextSplitter z parametrami: chunk_size=1500, chunk_overlap=100
3. **Tworzenie bazy wektorowej**:

   - Funkcja `get_vectorstore()` tworzy osadzania (embeddings) dla fragmentów tekstu za pomocą OpenAIEmbeddings
   - Osadzania są przechowywane w bazie FAISS dla szybkiego wyszukiwania podobieństwa
4. **Tworzenie łańcucha konwersacji**:

   - Funkcja `get_conversation_chain()` tworzy łańcuch przetwarzania dla konwersacji
   - Wykorzystuje model ChatOpenAI, pamięć konwersacji (ConversationBufferMemory)
   - Definiuje szablon promptu w języku polskim, który instruuje model, aby odpowiadał wyłącznie na podstawie dostarczonych dokumentów
5. **Obsługa interakcji z użytkownikiem**:

   - Funkcja `handle_userinput()` przetwarza pytania użytkownika
   - Wywołuje łańcuch konwersacji z pytaniem użytkownika
   - Zapisuje kontekst w pamięci konwersacji
   - Aktualizuje i wyświetla historię czatu
6. **Interfejs użytkownika**:

   - Funkcja `main()` konfiguruje interfejs Streamlit
   - Zawiera panel boczny do przesyłania dokumentów i przycisk "Process"
   - Wyświetla historię konwersacji w formie czatu

## Kluczowe funkcjonalności

1. **Przetwarzanie wielu dokumentów PDF** - aplikacja może jednocześnie analizować wiele plików PDF
2. **Kontekstowe odpowiedzi** - odpowiedzi są generowane wyłącznie na podstawie zawartości dokumentów
3. **Pamięć konwersacji** - aplikacja pamięta historię rozmowy, co pozwala na kontynuowanie wątków
4. **Wyszukiwanie semantyczne** - wykorzystanie osadzań wektorowych do znajdowania najbardziej odpowiednich fragmentów tekstu
5. **Ograniczenia odpowiedzi** - model jest instruowany, aby nie zgadywał i przyznawał się do niewiedzy, jeśli odpowiedź nie znajduje się w dokumentach

## Uwagi dotyczące wdrożenia

1. Aplikacja wymaga klucza API OpenAI, który powinien być skonfigurowany w zmiennych środowiskowych
2. Uruchomienie aplikacji odbywa się za pomocą komendy `streamlit run application.py`
3. Projekt jest prawdopodobnie częścią serii edukacyjnej, na co wskazują linki do odcinków wideo w README.md

## Podsumowanie

"Asystent PDF" to kompletne rozwiązanie do interaktywnej analizy dokumentów PDF z wykorzystaniem nowoczesnych technologii AI. Projekt ma jasną strukturę, dobrze zdefiniowany przepływ danych i wykorzystuje najlepsze praktyki w zakresie przetwarzania języka naturalnego i tworzenia interfejsów użytkownika.

---
