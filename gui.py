from ui_enigma import Ui_inputTextArea
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QMessageBox,
    QFileDialog
)
import sys
from enigma import Enigma
from components import Rotor, Reflector, Plugboard
from components import PlugboardConfigurationError
from enigma import (
    MalformedDataError,
    InvalidComponentError
)

from utils import int_to_char


class EnigmaUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = QWidget()
        # fixed problem with expanding by creating central widget and put everythiong in this widget
        self.setCentralWidget(self.central_widget)
        self.ui = Ui_inputTextArea()
        self.ui.setupUi(self.central_widget)

        self.enigma = None
        self._set_default_values()

        self._connect_signals()

    def _connect_signals(self):
        self.ui.textEdit.textChanged.connect(self._encryption)

        self._setup_rotors_signal(
            self.ui.rotor1Model,
            self.ui.rotor1InitialPosition,
            self.ui.rotor1RingSetting
        )

        self._setup_rotors_signal(
            self.ui.rotor2Model,
            self.ui.rotor2InitialPosition,
            self.ui.rotor2RingSetting
        )

        self._setup_rotors_signal(
            self.ui.rotor3Model,
            self.ui.rotor3InitialPosition,
            self.ui.rotor3RingSetting
        )

        self.ui.reflectorModel.currentTextChanged.connect(self._encryption)

        self.ui.plugboard.textChanged.connect(self._encryption)

        self.ui.reflectorModel.setCurrentText('B')

        self.ui.plugboard.setText('')

        self.ui.clearButton.clicked.connect(self._set_default_values)

        self.ui.saveButton.clicked.connect(self._save_enigma_settings)

        self.ui.loadButton.clicked.connect(self._load_enigma_settings)

        self.ui.chooseFileButton.clicked.connect(self._load_text)

        self.ui.exportToFile.clicked.connect(self._export_to_file)

    def _setup_rotors_signal(self, model, position, ring_setting):
        model.currentTextChanged.connect(self._encryption)

        position.valueChanged.connect(self._encryption)
        position.valueChanged.connect(
            lambda: self._update_spinbox_suffix(position)
        )

        ring_setting.valueChanged.connect(self._encryption)
        ring_setting.valueChanged.connect(
            lambda: self._update_spinbox_suffix(ring_setting)
        )

    def _update_spinbox_suffix(self, spin_box):
        letter = int_to_char(spin_box.value())
        spin_box.setSuffix(f" ({letter})")

    def _export_to_file(self):
        content = self.ui.outputText.toPlainText()
        if not content:
            QMessageBox.warning(self, "Warning", "There is no text to export")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "", "encrypted_text.txt", "Text files (*.txt);;All files (*)")

        if not file_path:
            return
        try:
            with open(file_path, 'w') as file_handle:
                file_handle.write(content)
            QMessageBox.information(self, "Saved encrypted text", "You succesfully saved encrypted text")
        except OSError as e:
            QMessageBox.critical(self, "", f"Error {e}")

    def _load_text(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "",
            "",
            "Text files (*.txt)"
        )

        if not file_path:
            return

        try:
            with open(file_path, 'r') as file_handle:
                content = file_handle.read()

            self.ui.textEdit.setText(content)
        except OSError as e:
            QMessageBox.critical(self, "Error", f"Could not open file:\n{e}")

    def _load_enigma_settings(self):
        widgets_to_block = [
                    self.ui.rotor1Model, self.ui.rotor1InitialPosition, self.ui.rotor1RingSetting,
                    self.ui.rotor2Model, self.ui.rotor2InitialPosition, self.ui.rotor2RingSetting,
                    self.ui.rotor3Model, self.ui.rotor3InitialPosition, self.ui.rotor3RingSetting,
                    self.ui.reflectorModel, self.ui.plugboard
                ]
        try:
            with open('settings.json', 'r') as file_handle:
                self.enigma.load_enigma_settings(file_handle)

                for widget in widgets_to_block:
                    widget.blockSignals(True)

                self.ui.rotor1Model.setCurrentText(self.enigma.rotor1.name)
                self.ui.rotor1InitialPosition.setValue(self.enigma.rotor1.initial_position)
                self.ui.rotor1RingSetting.setValue(self.enigma.rotor1.ring_setting)

                self.ui.rotor2Model.setCurrentText(self.enigma.rotor2.name)
                self.ui.rotor2InitialPosition.setValue(self.enigma.rotor2.initial_position)
                self.ui.rotor2RingSetting.setValue(self.enigma.rotor2.ring_setting)

                self.ui.rotor3Model.setCurrentText(self.enigma.rotor3.name)
                self.ui.rotor3InitialPosition.setValue(self.enigma.rotor3.initial_position)
                self.ui.rotor3RingSetting.setValue(self.enigma.rotor3.ring_setting)

                self.ui.reflectorModel.setCurrentText(self.enigma.reflector.name)

                self.ui.plugboard.setText(self.enigma.plugboard.connections_as_str)

                self._update_spinbox_suffix(self.ui.rotor1InitialPosition)
                self._update_spinbox_suffix(self.ui.rotor1RingSetting)
                self._update_spinbox_suffix(self.ui.rotor2InitialPosition)
                self._update_spinbox_suffix(self.ui.rotor2RingSetting)
                self._update_spinbox_suffix(self.ui.rotor3InitialPosition)
                self._update_spinbox_suffix(self.ui.rotor3RingSetting)

                self._encryption()
            QMessageBox.information(self, "Loaded", "Successfully loaded enigma settings")
            print("Loaded")
        except MalformedDataError as e:
            print(f"Error during loading settings {e}")
            QMessageBox.critical(self, "Error", f"Loading Error: {e}")
        except InvalidComponentError as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Error", f"Loading Error: {e}")

        # finally guaranttes that this lines of code will always execute no matter what
        finally:
            for widget in widgets_to_block:
                widget.blockSignals(False)

    def _save_enigma_settings(self):
        try:
            with open('settings.json', 'w') as file_handle:
                self.enigma.save_enigma_settings(file_handle)
            QMessageBox.information(self, "Saved", "Successfully saved current settings")
            print("Saved")
        except Exception as e:
            print(f"Error {e}")
            QMessageBox.critical(self, "Save Error", f"Cannot save enigma settings: {e}")

    def _set_default_values(self):
        self.ui.rotor1Model.setCurrentText("I")
        self.ui.rotor1InitialPosition.setValue(0)
        self._update_spinbox_suffix(self.ui.rotor1InitialPosition)
        self.ui.rotor1RingSetting.setValue(0)
        self._update_spinbox_suffix(self.ui.rotor1RingSetting)

        self.ui.rotor2Model.setCurrentText("II")
        self.ui.rotor2InitialPosition.setValue(0)
        self._update_spinbox_suffix(self.ui.rotor2InitialPosition)
        self.ui.rotor2RingSetting.setValue(0)
        self._update_spinbox_suffix(self.ui.rotor2RingSetting)

        self.ui.rotor3Model.setCurrentText("III")
        self.ui.rotor3InitialPosition.setValue(0)
        self._update_spinbox_suffix(self.ui.rotor3InitialPosition)
        self.ui.rotor3RingSetting.setValue(0)
        self._update_spinbox_suffix(self.ui.rotor3RingSetting)

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
        try:
            self._rebuild_enigma()
            self.ui.plugboard.setStyleSheet("")
        except PlugboardConfigurationError as e:
            self.ui.plugboard.setStyleSheet("border: 1px solid red; background-color: rgba(255, 0, 0, 30);")
            self.ui.outputText.setText(f'{e}')
            print(e)
            return
        if not text:
            self.ui.outputText.clear()
            return

        encrypted_text = self.enigma.encrypt(text)
        self.ui.outputText.setText(encrypted_text)


def guiMain(args):
    app = QApplication(args)
    window = EnigmaUI()
    window.show()
    return app.exec()