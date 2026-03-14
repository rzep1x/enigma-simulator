# Enigma Machine Simulator (PIPR25Z Project)

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)

## Assignment

Design and implement a simulator of the Enigma encryption machine.

Handle file reading and writing, including persistence layer for machine settings. Provide batch and graphical modes - a simple GUI is sufficient for testing and demonstration.

Notes
Thoroughly test the created program and develop its demonstration.
Detailing the project scope is part of the project.

## Description
The program is a faithful simulator of the military Enigma encryption machine (M3/Wehrmacht model).
The application replicates the full bidirectional electrical signal path through all mechanical components: plugboard, rotors, and reflector.
In configuration, the user has 8 historical rotor models (I-VIII) and two reflector models (B,C) to choose from.
The program also allows the user to save the current Enigma settings and load them.
Import text for encryption from a txt file and save the encrypted message to a txt file.

## Encryption Logic
[Enigma encryption logic](/docs/enigma_flow.pdf)

## Single Rotor Passage Logic
![Single rotor passage logic based on a simplified rotor version with indices 0 to 5](/docs/rotor.png)

## Project Structure
- enigma/ — main Python package containing source code.
  - __init__.py
  - main.py — responsible for launching the program.
  - enigma.py — main Enigma class: construction, rotor steps, encryption, saving/loading settings.
  - components.py — implementation of Rotor, Reflector, Plugboard and configuration validations.
  - config.py — configuration data for rotors and reflectors.
  - utils.py — helper functions.
  - gui/ — user interface subpackage.
    - __init__.py
    - gui.py — main GUI logic.
    - ui_enigma.py — generated interface (PySide6).
    - enigma.ui — Qt Designer UI file.
- config/ — configuration files.
  - settings.json — stores saved settings.
- examples/ — example files.
  - encrypted_text.txt — example encrypted text.
- docs/ — documentation.
- tests/ — unit tests (pytest).
- pyproject.toml — Python package configuration.
- README.md — this file (English).
- README_PL.md — this file (Polish).

## Installation
Install the program using the commands:
```bash
git clone https://github.com/rzep1x/enigma-simulator.git
cd enigma
python -m pip install .
```

For development (tests, linting tools):
```bash
python -m pip install -e ".[dev]"
```

## Requirements
- Python 3.8+ (as defined in `pyproject.toml`, tested on 3.9.6)

## Running
If you have the appropriate Python version and installed packages from `pyproject.toml`, run the program with commands (being in the project folder):

- Graphical mode (GUI):
```bash
python -m enigma.main
# or
enigma
```
- Batch Mode
This mode allows encrypting data directly from the console, without opening the program window. Requires providing three arguments: text source, output file, and settings file.

| Short Flag | Long Flag | Description |
| :---: | :--- | :--- |
| `-i` | `--input` | Path to input file (e.g. `examples/message.txt`). |
| `-t` | `--text` | Text to encrypt provided directly (e.g. `"MESSAGE"`). |
| `-o` | `--output` | Path to output file (e.g. `examples/encrypted.txt`). |
| `-s` | `--settings` | Path to JSON file with machine settings (e.g. `config/settings.json`). |

Usage examples:
```bash
python -m enigma.main -t "TextToEncrypt" -o examples/encrypted_text.txt -s config/settings.json
```
```bash
python -m enigma.main -i examples/message_to_encrypt.txt -o examples/encrypted_text.txt -s config/settings.json
```

## Implementation Notes
- Encryption ignores non-ASCII characters / numbers / special characters / spaces.
- Encryption accepts lowercase and uppercase letters but the encoded message will always be uppercase.
- Plugboard accepts letter pairs in the format "AB CD EF" (unique pairs).
- Enigma.save_enigma_settings and load_enigma_settings operate on JSON files and validate the structure.

## Author
Filip Rzepkowski

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
