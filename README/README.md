# Enigma — symulator maszyny Enigma (projekt uczelniany)

## Opis
 Program jest  wiernym symulatorem wojskowej maszyny szyfrującej Enigma (model M3/Wehrmacht). Aplikacja odwzorowuje pełną, dwukierunkową ścieżkę sygnału elektrycznego przez wszystkie komponenty mechaniczne: łącznicę kablową, wirniki oraz reflektor. Przy kofiguracji użytkownik posiada do wyboru 5 hisotrycznym modeli wirników (I-V) oraz dwa modele reflektorów (B,C).
 Program umożliwia użytkownikowi także zapis ustawień enigmy na której aktualnie pracuje i wczytanie jej po ponownym uruchomieniu programu. Import tesktu do szyfrowania z pliku txt oraz zapis zaszyfrowanej wiadomości także do pliku o rozszerzeniu .txt

## Logika szyfrowania
[Logika szyfrowania enigmy](/README/enigma_flow.pdf)

## Struktura projektu (najważniejsze pliki)
- enigma.py — główna klasa Enigma: budowa, kroki rotorów, szyfrowanie, zapisywanie/ładowanie ustawień.
- components.py — implementacja Rotor, Reflector, Plugboard oraz walidacje konfiguracji.
- config.py — dane konfiguracyjne rotorów i reflektorów.
- ui_enigma.py — interfejs użytkownika (PySide6).
- gui.py - opowiedzialne za uruchomienie programu oraz za interfejs.
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
```bash
git clone https://gitlab-stud.elka.pw.edu.pl/frzepkow/enigma.git
cd enigma
python3 ./gui.py
```

## Uwagi implementacyjne
- Szyfrowanie ignoruje znaki nie-ASCII / cyfry / znaki specjalne / spacje.
- Szyforwanie przyjmuje litery małe i wielkie lecz zakodowana wiadomość zawsze będzie wielkimi literami
- Plugboard przyjmuje pary liter w formacie "AB CD EF" (unikatowe pary).
- Enigma.save_enigma_settings i load_enigma_settings operują na plikach JSON i walidują strukturę.
