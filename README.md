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

## ©️ Licencja 🪪

Rozpowszechniane na licencji MIT. Zobacz `LICENSE`, aby uzyskać więcej informacji.

---

## Kontakt

<div style="display: flex; align-items: center; gap: 15px;">
  <img src="logo.png" alt="Icon" width="70">
  <div style="display: flex; align-items: center; gap: 10px;">
    <span>netdark_1966</span>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
    </svg>
    <a href="mailto:netdark_1966@op.pl">netdark_1966</a>
    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
    </svg>
    <a href="https://github.com/Darek1966">GitHub — Darek1966</a>
  </div>
</div>

---
