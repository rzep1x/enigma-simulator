from ui_enigma import Ui_inputTextArea
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
import sys
from enigma import Enigma
from components import Rotor, Reflector, Plugboard
from components import (
    PlugboradConfigurationLenghtError,
    PlugboradConfigurationWrongLettersError,
    PlugboardConfigurationLetterAlreadyUsedError
)


class EnigmaUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cetral_widget = QWidget()
        # fixed problem with expanding by creating central widget and put everythiong in this widget
        self.setCentralWidget(self.cetral_widget)
        self.ui = Ui_inputTextArea()
        self.ui.setupUi(self.cetral_widget)

        self.enigma = None
        self._set_deafult_values()

        self._connect_signals()

    def _connect_signals(self):
        self.ui.textEdit.textChanged.connect(self._encryption)

        self.ui.rotor1Model.currentTextChanged.connect(self._encryption)
        self.ui.rotor1InitialPosition.valueChanged.connect(self._encryption)
        self.ui.rotor1RingSetting.valueChanged.connect(self._encryption)

        self.ui.rotor2Model.currentTextChanged.connect(self._encryption)
        self.ui.rotor2InitialPosition.valueChanged.connect(self._encryption)
        self.ui.rotor2RingSetting.valueChanged.connect(self._encryption)

        self.ui.rotor3Model.currentTextChanged.connect(self._encryption)
        self.ui.rotor3InitialPosition.valueChanged.connect(self._encryption)
        self.ui.rotor3RingSetting.valueChanged.connect(self._encryption)

        self.ui.reflectorModel.currentTextChanged.connect(self._encryption)

        self.ui.plugboard.textChanged.connect(self._encryption)

        self.ui.reflectorModel.setCurrentText('B')

        self.ui.plugboard.setText('')

        self.ui.clearButton.clicked.connect(self._set_deafult_values)

        self.ui.saveButton.clicked.connect(self._save_enigma_settings)

        self.ui.loadButton.clicked.connect(self._load_enigma_settings)

    def _load_enigma_settings(self):
        try:
            with open('settings.json', 'r') as file_handle:
                self.enigma.load_enigma_settings(file_handle)
            QMessageBox.information(self, "Loaded", "Successfully loaded enigma settings")
            print("Loaded")
        except Exception as e:
            print(f"Error {e}")
            QMessageBox.critical(self, "Loading Error", f'Coudlnt load settings: {e}')

    def _save_enigma_settings(self):
        try:
            self._rebuild_enigma()
            with open('settings.json', 'w') as file_handle:
                self.enigma.save_enigma_settings(file_handle)
            QMessageBox.information(self, "Saved", "Successfully saved current settings")
            print("Saved")
        except Exception as e:
            print(f"Error {e}")
            QMessageBox.critical(self, "Save Error", f"Cannot save enigma settings: {e}")

    def _set_deafult_values(self):
        self.ui.rotor1Model.setCurrentText("I")
        self.ui.rotor1InitialPosition.setValue(0)
        self.ui.rotor1RingSetting.setValue(0)

        self.ui.rotor2Model.setCurrentText("II")
        self.ui.rotor2InitialPosition.setValue(0)
        self.ui.rotor2RingSetting.setValue(0)

        self.ui.rotor3Model.setCurrentText("III")
        self.ui.rotor3InitialPosition.setValue(0)
        self.ui.rotor3RingSetting.setValue(0)

        self.ui.reflectorModel.setCurrentText('B')

        self.ui.plugboard.setText('')

        self.ui.textEdit.clear()
        self.ui.outputText.clear()

        self._rebuild_enigma()

    def _rebuild_enigma(self):
        r1_model = self.ui.rotor1Model.currentText()
        r1_pos = self.ui.rotor1InitialPosition.value()
        r1_ring_setting = self.ui.rotor1RingSetting.value()
        r1 = Rotor(r1_model, r1_pos, r1_ring_setting)

        r2_model = self.ui.rotor2Model.currentText()
        r2_pos = self.ui.rotor2InitialPosition.value()
        r2_ring_setting = self.ui.rotor2RingSetting.value()
        r2 = Rotor(r2_model, r2_pos, r2_ring_setting)

        r3_model = self.ui.rotor3Model.currentText()
        r3_pos = self.ui.rotor3InitialPosition.value()
        r3_ring_setting = self.ui.rotor3RingSetting.value()
        r3 = Rotor(r3_model, r3_pos, r3_ring_setting)

        plug_conn = self.ui.plugboard.text()
        plug = Plugboard(plug_conn)

        ref_model = self.ui.reflectorModel.currentText()
        ref = Reflector(ref_model)

        self.enigma = Enigma(rotor1=r1, rotor2=r2, rotor3=r3, reflector=ref, plugboard=plug)

    def _encryption(self):
        text = self.ui.textEdit.toPlainText()
        if not text:
            self.ui.outputText.clear()
            return

        try:
            self._rebuild_enigma()
            self.ui.plugboard.setStyleSheet("")
            encrypted_text = self.enigma.encrypt(text)
            self.ui.outputText.setText(encrypted_text)
        except (PlugboradConfigurationLenghtError, PlugboradConfigurationWrongLettersError) as e:
            self.ui.plugboard.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 30);")
            self.ui.outputText.setText(f'{e}')
            print(e)
        except PlugboardConfigurationLetterAlreadyUsedError as e:
            self.ui.plugboard.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 30);")
            self.ui.outputText.setText(f'{e}')
            print(e)


def guiMain(args):
    app = QApplication(args)
    window = EnigmaUI()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guiMain(sys.argv)
