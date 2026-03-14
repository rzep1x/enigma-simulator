# Symulator Maszyny Enigma (projekt PIPR25Z)

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

## Polecenie

Zaprojektować i zaimplementować symulator maszyny szyfrującej Enigma.

Obsłużyć czytanie i zapis do pliku, w tym warstwę trwałości dla ustawień maszyny szyfrującej. Dostarczyć pracy w trybie wsadowym i graficznym - wystarczy proste GUI na potrzeby testowania i demonstracji.

Uwagi
Dokładnie przetestować stworzony program i opracować jego demonstrację.
Uszczegółowienie zakresu projektu jest elementem projektu.

## Opis
Program jest wiernym symulatorem wojskowej maszyny szyfrującej Enigma (model M3/Wehrmacht).
Aplikacja odwzorowuje pełną dwukierunkową ścieżkę sygnału elektrycznego przez wszystkie komponenty mechaniczne: łącznicę kablową, wirniki oraz reflektor.
Przy konfiguracji użytkownik posiada do wyboru 8 historycznych modeli wirników (I-VIII) oraz dwa modele reflektorów (B,C).
Program umożliwia użytkownikowi także zapis ustawień enigmy na której aktualnie pracuje i wczytanie tych ustawień.
Import tekstu do szyfrowania z pliku txt oraz zapis zaszyfrowanej wiadomości także do pliku o rozszerzeniu .txt

## Logika szyfrowania
[Logika szyfrowania enigmy](/docs/enigma_flow.pdf)

## Logika przejścia przez pojedynczy wirnik
![Logika przejścia przez pojedynczy rotor na podstawie uproszczonej wersji rotora z indeksami od 0 do 5](/docs/rotor.png)

## Struktura projektu
- enigma/ — główny pakiet Pythona zawierający kod źródłowy.
  - __init__.py
  - main.py — odpowiedzialna za uruchomienie programu.
  - enigma.py — główna klasa Enigma: budowa, kroki rotorów, szyfrowanie, zapisywanie/ładowanie ustawień.
  - components.py — implementacja Rotor, Reflector, Plugboard oraz walidacje konfiguracji.
  - config.py — dane konfiguracyjne rotorów i reflektorów.
  - utils.py — pomocnicze funkcje.
  - gui/ — podpakiet interfejsu użytkownika.
    - __init__.py
    - gui.py — główna logika GUI.
    - ui_enigma.py — wygenerowany interfejs (PySide6).
    - enigma.ui — plik UI Qt Designer.
- config/ — pliki konfiguracyjne.
  - settings.json — przechowuje zapisane ustawienia.
- examples/ — przykładowe pliki.
  - encrypted_text.txt — przykładowy zaszyfrowany tekst.
- docs/ — dokumentacja.
- tests/ — testy jednostkowe (pytest).
- pyproject.toml — konfiguracja pakietu Python.
- README.md — ten plik (po angielsku).
- README_PL.md — ten plik (po polsku).

## Instalacja
Instalacja programu poprzez komendy
```bash
git clone https://github.com/yourusername/enigma-simulator.git
cd enigma-simulator
python -m pip install .
```

Dla developmentu (testy, narzędzia lint):
```bash
python -m pip install -e ".[dev]"
```

## Wymagania
- Python 3.8+ (zgodnie z `pyproject.toml`, testowano na wersji 3.9.6)

## Uruchamianie
Jeśli posiadasz odpowiednią wersję Pythona oraz pakiety zainstalowane z `pyproject.toml`, uruchom program komendami (będąc w folderze programu):

- Tryb graficzny (GUI):
```bash
python -m enigma.main
# lub
enigma
```
- Tryb wsadowy (Batch Mode)
Tryb ten pozwala na szyfrowanie danych bezpośrednio z konsoli, bez otwierania okna programu. Wymaga podania trzech argumentów: źródła tekstu, pliku wyjściowego oraz pliku z ustawieniami.

| Flaga Krótka | Flaga Długa | Opis |
| :---: | :--- | :--- |
| `-i` | `--input` | Ścieżka do pliku wejściowego (np. `examples/message.txt`). |
| `-t` | `--text` | Tekst do zaszyfrowania podany bezpośrednio (np. `"MESSAGE"`). |
| `-o` | `--output` | Ścieżka do pliku wynikowego (np. `examples/encrypted.txt`). |
| `-s` | `--settings` | Ścieżka do pliku JSON z ustawieniami maszyny (np. `config/settings.json`). |

Przykłady użycia:
```bash
python -m enigma.main -t "TextToEncrypt" -o examples/encrypted_text.txt -s config/settings.json
```
```bash
python -m enigma.main -i examples/message_to_encrypt.txt -o examples/encrypted_text.txt -s config/settings.json
```

## Uwagi implementacyjne
- Szyfrowanie ignoruje znaki nie-ASCII / cyfry / znaki specjalne / spacje.
- Szyfrowanie przyjmuje litery małe i wielkie lecz zakodowana wiadomość zawsze będzie wielkimi literami
- Plugboard przyjmuje pary liter w formacie "AB CD EF" (unikatowe pary).
- Enigma.save_enigma_settings i load_enigma_settings operują na plikach JSON i walidują strukturę.

## Autor
Filip Rzepkowski

## Licencja
Ten projekt jest licencjonowany na podstawie Licencji MIT - zobacz plik [LICENSE](LICENSE) po szczegóły.
