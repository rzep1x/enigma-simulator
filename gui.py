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

        self.ui.rotor1Model.setCurrentText("I")
        self.ui.rotor1InitialPosition.setValue(0)
        self.ui.rotor1RingSetting.setValue(0)

        self.ui.rotor2Model.setCurrentText("I")
        self.ui.rotor2InitialPosition.setValue(0)
        self.ui.rotor2RingSetting.setValue(0)

        self.ui.rotor3Model.setCurrentText("I")
        self.ui.rotor3InitialPosition.setValue(0)
        self.ui.rotor3RingSetting.setValue(0)

        self.ui.reflectorModel.setCurrentText('B')

        self.ui.plugboard.setText('')

        self.enigma = None
        self._rebuild_enigma()

        self._connect_signals()

    def _connect_signals(self):
        # self.ui.textEdit.textChanged.connect(self._encrypt)

        self.ui.rotor1Model.currentTextChanged.connect(self._rebuild_enigma)
        self.ui.rotor1InitialPosition.valueChanged.connect(self._rebuild_enigma)
        self.ui.rotor1RingSetting.valueChanged.connect(self._rebuild_enigma)

        self.ui.rotor2Model.currentTextChanged.connect(self._rebuild_enigma)
        self.ui.rotor2InitialPosition.valueChanged.connect(self._rebuild_enigma)
        self.ui.rotor2RingSetting.valueChanged.connect(self._rebuild_enigma)

        self.ui.rotor3Model.currentTextChanged.connect(self._rebuild_enigma)
        self.ui.rotor3InitialPosition.valueChanged.connect(self._rebuild_enigma)
        self.ui.rotor3RingSetting.valueChanged.connect(self._rebuild_enigma)

        self.ui.reflectorModel.currentTextChanged.connect(self._rebuild_enigma)

        self.ui.plugboard.textChanged.connect(self._rebuild_enigma)

    def _rebuild_enigma(self):
        try:
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

