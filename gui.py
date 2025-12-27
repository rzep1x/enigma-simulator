from ui_enigma import Ui_inputTextArea
from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from enigma import Enigma
from components import Rotor, Reflector, Plugboard


class EnigmaUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_inputTextArea()
        self.ui.setupUi(self)
        self.enigma = Enigma()
        self._connect_signals()

    def _connect_signals(self):
        self.ui.textEdit.textChanged.connect(self._encrypt)

        self.ui.rotor1Model.currentTextChanged.connect(self._update_settings)
        self.ui.rotor1InitialPosition.valueChanged.connect(self._update_settings)
        self.ui.rotor1RingSetting.valueChanged.connect(self._update_settings)

        self.ui.rotor2Model.currentTextChanged.connect(self._update_settings)
        self.ui.rotor2InitialPosition.valueChanged.connect(self._update_settings)
        self.ui.rotor2RingSetting.valueChanged.connect(self._update_settings)

        self.ui.rotor3Model.currentTextChanged.connect(self._update_settings)
        self.ui.rotor3InitialPosition.valueChanged.connect(self._update_settings)
        self.ui.rotor3RingSetting.valueChanged.connect(self._update_settings)

        self.ui.reflectorModel.currentTextChanged.connect(self._update_settings)

        self.ui.plugboard.textChanged.connect(self._update_settings)

    def _update_settings(self):
        try:
            r1_model = self.ui.rotor1Model.currentText()
            r1_pos = self.ui.rotor1InitialPosition.value()
            r1_ring_setting = self.ui.rotor1RingSetting.value()
            self.enigma.set_rotor1(Rotor(r1_model, r1_pos, r1_ring_setting))

            r2_model = self.ui.rotor2Model.currentText()
            r2_pos = self.ui.rotor2InitialPosition.value()
            r2_ring_setting = self.ui.rotor2RingSetting.value()
            self.enigma.set_rotor2(Rotor(r2_model, r2_pos, r2_ring_setting))

            r3_model = self.ui.rotor3Model.currentText()
            r3_pos = self.ui.rotor3InitialPosition.value()
            r3_ring_setting = self.ui.rotor3RingSetting.value()
            self.enigma.set_rotor3(Rotor(r3_model, r3_pos, r3_ring_setting))

            plug = self.ui.plugboard.text()
            self.enigma.set_plugboard(Plugboard(plug))

            ref_model = self.ui.reflectorModel.currentText()
            self.enigma.set_reflector(Reflector(ref_model))

            self._encryption()
        except Exception as e:
            print(f"Configuration Error {e}")






def guiMain(args):
    app = QApplication(args)
    window = EnigmaUI()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guiMain(sys.argv)

