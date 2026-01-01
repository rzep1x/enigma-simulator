# Enigma — symulator maszyny Enigma (projekt uczelniany)

## Krótki opis
- Prosty symulator maszyny Enigma z interfejsem GUI (PySide6) i zestawem testów unitarnych (pytest).
- Obsługuje 3 rotory, reflektor, oraz plugboard (konfiguracja par liter).
- [Logika szyfrowania enigmy](/text/enigma_flow.png)

## Struktura projektu (najważniejsze pliki)
- enigma.py — główna klasa Enigma: budowa, kroki rotorów, szyfrowanie, zapisywanie/ładowanie ustawień.
- components.py — implementacja Rotor, Reflector, Plugboard oraz walidacje konfiguracji.
- config.py — dane konfiguracyjne rotorów i reflektorów.
- ui_enigma.py — interfejs użytkownika (PySide6).
- gui.py - opowiedzialne za uruchomienie programu oraz za interfejs.
- utils.py — pomocnicze funkcje.
- settings.json — przechowuje zapisane
- requirements.txt — wymagane pakiety.
- tests/ — testy jednostkowe (pytest).

## Wymagania
- Python 3.9+ (Testowano na wersji 3.9.6)
- Zainstaluj biblioteki:
```bash
pip install -r requirements.txt
```

## Uruchamianie
Uruchom program komendami bedąc w katalogu projektu:
```bash
git clone https://gitlab-stud.elka.pw.edu.pl/frzepkow/enigma.git
cd enigma
python3 ./gui.py
```

## Ustawienia i pliki
- settings.json — zapis/odczyt konfiguracji (rotory, pozycje, ring settings, reflektor, plugboard).
- Z GUI można wczytać/ zapisać ustawienia oraz importować/eksportować teksty.

## Uwagi implementacyjne
- Szyfrowanie ignoruje znaki nie-ASCII / cyfry / znaki specjalne.
- Plugboard przyjmuje pary liter w formacie "AB CD EF" (unikatowe pary).
- Enigma.save_enigma_settings i load_enigma_settings operują na plikach JSON i walidują strukturę.
