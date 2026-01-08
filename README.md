# Enigma — symulator maszyny Enigma (projekt PIPR25Z)

## Polecenie

Proszę zaprojektować i zaimplementować symulator maszyny szyfrującej Enigma.

Proszę obsłużyć czytanie i zapis do pliku, w tym warstwę trwałości dla ustawień maszyny szyfrującej. Proszę dostarczyć pracy w trybie wsadowym i graficznym - wystarczy proste GUI na potrzeby testowania i demonstracji.

Uwagi
Proszę dokładnie przetestować stworzony program i opracować jego demonstrację.
Uszczegółowienie zakresu projektu jest elementem projektu.


## Opis
 Program jest  wiernym symulatorem wojskowej maszyny szyfrującej Enigma (model M3/Wehrmacht).
 Aplikacja odwzorowuje pełną, dwukierunkową ścieżkę sygnału elektrycznego przez wszystkie komponenty mechaniczne: łącznicę kablową, wirniki oraz reflektor.
 Przy konfiguracji użytkownik posiada do wyboru 8 historycznych modeli wirników (I-VIII) oraz dwa modele reflektorów (B,C).
 Program umożliwia użytkownikowi także zapis ustawień enigmy na której aktualnie pracuje i wczytanie tych ustawień.
 Import tekstu do szyfrowania z pliku txt oraz zapis zaszyfrowanej wiadomości także do pliku o rozszerzeniu .txt

## Logika szyfrowania
[Logika szyfrowania enigmy](/docs/enigma_flow.pdf)

## Logika przejścia przez pojedynczy wirnik
![Logika przejścia przez pojedynczy rotor na podstawie uproszczonej wersji rotora z indeksami od 0 do 5](/docs/rotor.png)

## Struktura projektu (najważniejsze pliki)
- main.py - odpowiedzialna za uruchomienie programu.
- enigma.py — główna klasa Enigma: budowa, kroki rotorów, szyfrowanie, zapisywanie/ładowanie ustawień.
- components.py — implementacja Rotor, Reflector, Plugboard oraz walidacje konfiguracji.
- config.py — dane konfiguracyjne rotorów i reflektorów.
- ui_enigma.py, gui.py — interfejs użytkownika (PySide6).
- utils.py — pomocnicze funkcje.
- settings.json — przechowuje zapisane ustawienia
- requirements.txt — wymagane pakiety.
- tests/ — testy jednostkowe (pytest).

## Instalacja
Instalacja programu poprzez komendy
```bash
git clone https://gitlab-stud.elka.pw.edu.pl/frzepkow/enigma.git
```

## Wymagania
- Python 3.9+ (Testowano na wersji 3.9.6)
- Zainstaluj biblioteki:
```bash
pip install -r requirements.txt
```

## Uruchamianie
Jeśli posiadasz odpowiednie wersje Pythona oraz pakiety z requirements.txt uruchom program komendami (bedąc w folderze programu):

- Tryb graficzny (GUI):
```bash
python3 ./main.py
```
- Tryb wsadowy (Batch Mode)
Tryb ten pozwala na szyfrowanie danych bezpośrednio z konsoli, bez otwierania okna programu. Wymaga podania trzech argumentów: źródła tekstu, pliku wyjściowego oraz pliku z ustawieniami.


| Flaga Krótka | Flaga Długa | Opis |
| :---: | :--- | :--- |
| `-i` | `--input` | Ścieżka do pliku wejściowego (np. `message.txt`). |
| `-t` | `--text` | Tekst do zaszyfrowania podany bezpośrednio (np. `"MESSAGE"`). |
| `-o` | `--output` | Ścieżka do pliku wynikowego (np. `encrypted.txt`). |
| `-s` | `--settings` | Ścieżka do pliku JSON z ustawieniami maszyny. |


Przykłady użycia:
```bash
python3 ./main.py -t "TextToEncyrpt" -o ./encrypted_text.txt -s ./settings.json
```
```bash
python3 ./main.py -i ./message_to_encrypt.txt -o ./encrypted_text.txt -s ./settings.json
```

## Uwagi implementacyjne
- Szyfrowanie ignoruje znaki nie-ASCII / cyfry / znaki specjalne / spacje.
- Szyfrowanie przyjmuje litery małe i wielkie lecz zakodowana wiadomość zawsze będzie wielkimi literami
- Plugboard przyjmuje pary liter w formacie "AB CD EF" (unikatowe pary).
- Enigma.save_enigma_settings i load_enigma_settings operują na plikach JSON i walidują strukturę.

## Autor
Filip Rzepkowski
