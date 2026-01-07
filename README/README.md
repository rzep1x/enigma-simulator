# Enigma — symulator maszyny Enigma (projekt PIPR25Z)

## Opis
 Program jest  wiernym symulatorem wojskowej maszyny szyfrującej Enigma (model M3/Wehrmacht).
 Aplikacja odwzorowuje pełną, dwukierunkową ścieżkę sygnału elektrycznego przez wszystkie komponenty mechaniczne: łącznicę kablową, wirniki oraz reflektor.
 Przy konfiguracji użytkownik posiada do wyboru 5 historycznych modeli wirników (I-V) oraz dwa modele reflektorów (B,C).
 Program umożliwia użytkownikowi także zapis ustawień enigmy na której aktualnie pracuje i wczytanie jej po ponownym uruchomieniu programu.
 Import tekstu do szyfrowania z pliku txt oraz zapis zaszyfrowanej wiadomości także do pliku o rozszerzeniu .txt

## Logika szyfrowania
[Logika szyfrowania enigmy](/README/enigma_flow.pdf)

## Logika przejścia przez pojedynczy wirnik
[Logika przejścia przez pojedynczy rotor na podstawie uproszczonej wersji rotora z indeksami od 0 do 5](/README/rotor.png)

Na podstawie narysowanego schematu można zauważyć, że indeks wejścia w rotor wyraża sie wzorem:
```python
 index_in = (input_index + shift) % 26
 ```
 gdzie:
 ```python
 shift = self.current_position - self.ring_setting
 ```
Na przykładzie ostatniego z podanych schematów:
klikamy literkę A więc input_index = 0
shift = 3 - 1 = 2
więc index_in = 0 + 2 = 2 co jest zgodne z przedstawionych schematem

Wzór na numer pinu którym wychodzi prąd jest następujący:
bierzemy do jakiego pinu wyjściowego na stałe podpięty jest pin wejściowy
```python
mapped_index = self._wiring[index_in]
```
teraz mamy indeks pinu lecz musimy ustalić na jakim on jest miejscu.
```python
index_out = (mapped_index - shift) % 26
```
Kontynuując poprzedni przykład wiemy, że prąd wejdzie do rotora pinem nr 2 jest on połączony na stałe z pinem nr 4
więc według wzoru: index_out = 4 - 2 = 2 co jest zgodne z przedstawionych schematem.
Widzimy więc ze po kliknięciu litery A po przejściu przez pojedynczy rotor wychodzi nam C


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

## Wymagania
- Python 3.9+ (Testowano na wersji 3.9.6)
- Zainstaluj biblioteki:
```bash
pip install -r requirements.txt
```

## Uruchamianie
Jeśli posiadasz odpowiednie wersje Pythona oraz pakiety z requirements.txt uruchom program komendami:

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

## Uwagi implementacyjne
- Szyfrowanie ignoruje znaki nie-ASCII / cyfry / znaki specjalne / spacje.
- Szyfrowanie przyjmuje litery małe i wielkie lecz zakodowana wiadomość zawsze będzie wielkimi literami
- Plugboard przyjmuje pary liter w formacie "AB CD EF" (unikatowe pary).
- Enigma.save_enigma_settings i load_enigma_settings operują na plikach JSON i walidują strukturę.
