# Asystent PDF - Czat z wieloma dokumentami 📚🤖

Poznaj aplikację Asystent PDF! 🚀 Rozmawiaj płynnie z wieloma dokumentami PDF jednocześnie dzięki technologiom Langchain, Google Gemini Pro i bazie wektorowej FAISS. Otrzymuj natychmiastowe, dokładne odpowiedzi dzięki modelowi językowemu Google Gemini. 📚💬 Zrewolucjonizuj swoją pracę z dokumentami PDF już teraz! 🔥✨

## 📝 Opis

Asystent PDF to aplikacja webowa oparta na Streamlit, zaprojektowana do prowadzenia interaktywnych rozmów z chatbotem. Aplikacja pozwala użytkownikom wgrać wiele dokumentów PDF, wyodrębnić z nich informacje tekstowe i wytrenować chatbota na podstawie tej zawartości. Użytkownicy mogą następnie prowadzić rozmowy w czasie rzeczywistym z chatbotem, zadając pytania dotyczące zawartości dokumentów.

## 🎯 Jak to działa:

![Schemat działania aplikacji](img/Architecture.jpg)

Aplikacja działa według następujących kroków:

1. **Wczytywanie PDF**: Aplikacja odczytuje wiele dokumentów PDF i wyodrębnia ich zawartość tekstową.
2. **Podział tekstu**: Wyodrębniony tekst jest dzielony na mniejsze fragmenty, które mogą być efektywnie przetwarzane.
3. **Model językowy**: Aplikacja wykorzystuje model językowy do generowania reprezentacji wektorowych (embeddings) fragmentów tekstu.
4. **Dopasowanie podobieństwa**: Gdy zadajesz pytanie, aplikacja porównuje je z fragmentami tekstu i identyfikuje te najbardziej semantycznie podobne.
5. **Generowanie odpowiedzi**: Wybrane fragmenty są przekazywane do modelu językowego, który generuje odpowiedź na podstawie odpowiedniej zawartości dokumentów PDF.

## 🎯 Kluczowe funkcje

- **Adaptacyjne dzielenie tekstu**: Nasza technika Sliding Window Chunking dynamicznie dostosowuje rozmiar i pozycję okna dla RAG, równoważąc dostęp do danych o różnej granulacji w zależności od złożoności danych i kontekstu.
- **Wielodokumentowe konwersacyjne Q&A**: Obsługuje proste i wieloetapowe zapytania w wielu dokumentach jednocześnie, przełamując ograniczenie pojedynczego dokumentu.
- **Kompatybilność plików**: Obsługuje formaty plików PDF i TXT.
- **Kompatybilność z modelami LLM**: Obsługuje Google Gemini Pro, OpenAI GPT 3, Anthropic Claude, Llama2 i inne open-source'owe modele LLM.

## 🌟 Wymagania

- **Streamlit**: Biblioteka Pythona do tworzenia aplikacji webowych z interaktywnymi elementami.
- **google-generativeai**: Pakiet zapewniający możliwości generatywnej sztucznej inteligencji dla chatbotów i wirtualnych agentów.
- **python-dotenv**: Biblioteka do ładowania zmiennych środowiskowych z pliku `.env`.
- **langchain**: Niestandardowa biblioteka do zadań przetwarzania języka naturalnego, w tym wyszukiwania konwersacyjnego, dzielenia tekstu, osadzania, przechowywania wektorów, modeli czatu i pamięci.
- **PyPDF2**: Biblioteka do odczytu i manipulacji plikami PDF w Pythonie.
- **faiss-cpu**: FAISS (Facebook AI Similarity Search) to biblioteka opracowana przez Facebooka do efektywnego wyszukiwania podobieństwa, osadzania uczenia maszynowego, wyszukiwania informacji, filtrowania opartego na zawartości i klastrowania gęstych wektorów.
- **langchain_google_genai**: Pakiet zapewniający integrację między LangChain a SDK Google generative-ai.

## ▶️ Instalacja

Sklonuj repozytorium:

```bash
https://github.com/Darek1966/Asystent_PDF_Gemini.git
```

Zainstaluj wymagane pakiety Pythona:

```bash
pip install -r requirements.txt
```

Skonfiguruj klucz API Google z `https://makersuite.google.com/app/apikey`, tworząc plik .env w katalogu głównym projektu o następującej zawartości:

```bash
GOOGLE_API_KEY=twój-klucz-api
```

Uruchom aplikację Streamlit:

```bash
streamlit run chatapp.py
```

## 💡 Użytkowanie

Aby korzystać z Asystenta PDF, wykonaj następujące kroki:

1. Upewnij się, że zainstalowałeś wymagane zależności i dodałeś **klucz API Google do pliku `.env`** (KONIECZNE).
2. Uruchom plik `chatapp.py` za pomocą CLI Streamlit. Wykonaj następujące polecenie:
3. Aplikacja uruchomi się w domyślnej przeglądarce internetowej, wyświetlając interfejs użytkownika.
4. Wgraj wiele dokumentów PDF do aplikacji, postępując zgodnie z instrukcjami na pasku bocznym. Na pasku bocznym znajdziesz opcję wgrania dokumentów PDF. Kliknij przycisk "Wgraj dokumenty i kliknij Przetwórz" i wybierz jeden lub więcej plików PDF.
5. Nie zapomnij kliknąć przycisku "Prześlij i Przetwórz".
6. Zadawaj pytania w języku naturalnym dotyczące wgranych dokumentów PDF za pomocą interfejsu czatu.
7. Rozmowa z dokumentami: Po wgraniu i przetworzeniu dokumentów PDF możesz zadawać pytania, wpisując je w pole tekstowe. Naciśnij Enter lub kliknij przycisk "Zapytaj", aby wysłać pytanie.

Aplikacja wykorzysta sztuczną inteligencję konwersacyjną, aby udzielić odpowiedzi na podstawie zawartości wgranych dokumentów. Odpowiedzi będą wyświetlane w interfejsie czatu.

---

## Kontakt

[![Email](https://img.shields.io/badge/Email-Napisz%20do%20mnie-blue?style=for-the-badge&logo=gmail&logoColor=white)](mailto:netdark_1966@op.pl)

[![GitHub](https://img.shields.io/badge/GitHub-Darek1966-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Darek1966)

## Licencja
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE).

---
