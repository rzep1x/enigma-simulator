# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'enigma.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_inputTextArea(object):
    def setupUi(self, inputTextArea):
        if not inputTextArea.objectName():
            inputTextArea.setObjectName(u"inputTextArea")
        inputTextArea.resize(800, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(inputTextArea.sizePolicy().hasHeightForWidth())
        inputTextArea.setSizePolicy(sizePolicy)
        inputTextArea.setMinimumSize(QSize(800, 650))
        self.gridLayout_2 = QGridLayout(inputTextArea)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(inputTextArea)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(inputTextArea)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.textEdit)

        self.chooseFileButton = QPushButton(inputTextArea)
        self.chooseFileButton.setObjectName(u"chooseFileButton")

        self.verticalLayout.addWidget(self.chooseFileButton)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(inputTextArea)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rotor3Model = QComboBox(self.groupBox)
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.setObjectName(u"rotor3Model")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rotor3Model.sizePolicy().hasHeightForWidth())
        self.rotor3Model.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.rotor3Model, 9, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 16, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.saveButton)

        self.clearButton = QPushButton(self.groupBox)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy1.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.clearButton)

        self.loadButton = QPushButton(self.groupBox)
        self.loadButton.setObjectName(u"loadButton")
        sizePolicy1.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.loadButton)


        self.gridLayout.addLayout(self.horizontalLayout, 17, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)

        self.rotor1Model = QComboBox(self.groupBox)
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.setObjectName(u"rotor1Model")
        sizePolicy1.setHeightForWidth(self.rotor1Model.sizePolicy().hasHeightForWidth())
        self.rotor1Model.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.rotor1Model, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_7)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_14, 12, 0, 1, 1)

        self.plugboard = QLineEdit(self.groupBox)
        self.plugboard.setObjectName(u"plugboard")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plugboard.sizePolicy().hasHeightForWidth())
        self.plugboard.setSizePolicy(sizePolicy2)
        self.plugboard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plugboard.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plugboard.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.plugboard, 15, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rotor1InitialPosition = QSpinBox(self.groupBox)
        self.rotor1InitialPosition.setObjectName(u"rotor1InitialPosition")
        sizePolicy1.setHeightForWidth(self.rotor1InitialPosition.sizePolicy().hasHeightForWidth())
        self.rotor1InitialPosition.setSizePolicy(sizePolicy1)
        self.rotor1InitialPosition.setMaximum(25)

        self.horizontalLayout_4.addWidget(self.rotor1InitialPosition)

        self.rotor1RingSetting = QSpinBox(self.groupBox)
        self.rotor1RingSetting.setObjectName(u"rotor1RingSetting")
        sizePolicy1.setHeightForWidth(self.rotor1RingSetting.sizePolicy().hasHeightForWidth())
        self.rotor1RingSetting.setSizePolicy(sizePolicy1)
        self.rotor1RingSetting.setMaximum(25)

        self.horizontalLayout_4.addWidget(self.rotor1RingSetting)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rotor2InitialPosition = QSpinBox(self.groupBox)
        self.rotor2InitialPosition.setObjectName(u"rotor2InitialPosition")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.rotor2InitialPosition.sizePolicy().hasHeightForWidth())
        self.rotor2InitialPosition.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.rotor2InitialPosition)

        self.rotor2RingSetting = QSpinBox(self.groupBox)
        self.rotor2RingSetting.setObjectName(u"rotor2RingSetting")
        sizePolicy3.setHeightForWidth(self.rotor2RingSetting.sizePolicy().hasHeightForWidth())
        self.rotor2RingSetting.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.rotor2RingSetting)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rotor3InitialPosition = QSpinBox(self.groupBox)
        self.rotor3InitialPosition.setObjectName(u"rotor3InitialPosition")
        sizePolicy1.setHeightForWidth(self.rotor3InitialPosition.sizePolicy().hasHeightForWidth())
        self.rotor3InitialPosition.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.rotor3InitialPosition)

        self.rotor3RingSetting = QSpinBox(self.groupBox)
        self.rotor3RingSetting.setObjectName(u"rotor3RingSetting")
        sizePolicy1.setHeightForWidth(self.rotor3RingSetting.sizePolicy().hasHeightForWidth())
        self.rotor3RingSetting.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.rotor3RingSetting)


        self.gridLayout.addLayout(self.horizontalLayout_6, 11, 0, 1, 1)

        self.rotor2Model = QComboBox(self.groupBox)
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.setObjectName(u"rotor2Model")
        sizePolicy1.setHeightForWidth(self.rotor2Model.sizePolicy().hasHeightForWidth())
        self.rotor2Model.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.rotor2Model, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_11)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.reflectorModel = QComboBox(self.groupBox)
        self.reflectorModel.addItem("")
        self.reflectorModel.addItem("")
        self.reflectorModel.setObjectName(u"reflectorModel")
        sizePolicy1.setHeightForWidth(self.reflectorModel.sizePolicy().hasHeightForWidth())
        self.reflectorModel.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.reflectorModel, 13, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_13)


        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_16 = QLabel(inputTextArea)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_16)

        self.outputText = QTextEdit(inputTextArea)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setMinimumSize(QSize(0, 0))
        self.outputText.setAutoFillBackground(False)
        self.outputText.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.outputText)

        self.exportToFile = QPushButton(inputTextArea)
        self.exportToFile.setObjectName(u"exportToFile")

        self.verticalLayout_2.addWidget(self.exportToFile)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.horizontalLayout_8.setStretch(0, 4)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 4)

        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.retranslateUi(inputTextArea)

        QMetaObject.connectSlotsByName(inputTextArea)
    # setupUi

    def retranslateUi(self, inputTextArea):
        inputTextArea.setWindowTitle(QCoreApplication.translate("inputTextArea", u"Form", None))
        self.label.setText(QCoreApplication.translate("inputTextArea", u"Plain Text", None))
        self.chooseFileButton.setText(QCoreApplication.translate("inputTextArea", u"Choose file", None))
        self.groupBox.setTitle("")
        self.rotor3Model.setItemText(0, QCoreApplication.translate("inputTextArea", u"I", None))
        self.rotor3Model.setItemText(1, QCoreApplication.translate("inputTextArea", u"II", None))
        self.rotor3Model.setItemText(2, QCoreApplication.translate("inputTextArea", u"III", None))
        self.rotor3Model.setItemText(3, QCoreApplication.translate("inputTextArea", u"IV", None))
        self.rotor3Model.setItemText(4, QCoreApplication.translate("inputTextArea", u"V", None))

        self.label_2.setText(QCoreApplication.translate("inputTextArea", u"Rotor 1", None))
        self.saveButton.setText(QCoreApplication.translate("inputTextArea", u"Save", None))
        self.clearButton.setText(QCoreApplication.translate("inputTextArea", u"Clear", None))
        self.loadButton.setText(QCoreApplication.translate("inputTextArea", u"Load", None))
        self.label_15.setText(QCoreApplication.translate("inputTextArea", u"Plugboard", None))
        self.rotor1Model.setItemText(0, QCoreApplication.translate("inputTextArea", u"I", None))
        self.rotor1Model.setItemText(1, QCoreApplication.translate("inputTextArea", u"II", None))
        self.rotor1Model.setItemText(2, QCoreApplication.translate("inputTextArea", u"III", None))
        self.rotor1Model.setItemText(3, QCoreApplication.translate("inputTextArea", u"IV", None))
        self.rotor1Model.setItemText(4, QCoreApplication.translate("inputTextArea", u"V", None))

        self.label_6.setText(QCoreApplication.translate("inputTextArea", u"Initial position", None))
        self.label_7.setText(QCoreApplication.translate("inputTextArea", u"Ring Setting", None))
        self.label_14.setText(QCoreApplication.translate("inputTextArea", u"Reflector", None))
        self.label_4.setText(QCoreApplication.translate("inputTextArea", u"Rotor 2", None))
        self.label_5.setText(QCoreApplication.translate("inputTextArea", u"Rotor 3", None))
        self.rotor2Model.setItemText(0, QCoreApplication.translate("inputTextArea", u"I", None))
        self.rotor2Model.setItemText(1, QCoreApplication.translate("inputTextArea", u"II", None))
        self.rotor2Model.setItemText(2, QCoreApplication.translate("inputTextArea", u"III", None))
        self.rotor2Model.setItemText(3, QCoreApplication.translate("inputTextArea", u"IV", None))
        self.rotor2Model.setItemText(4, QCoreApplication.translate("inputTextArea", u"V", None))

        self.label_10.setText(QCoreApplication.translate("inputTextArea", u"Initial position", None))
        self.label_11.setText(QCoreApplication.translate("inputTextArea", u"Ring Setting", None))
        self.reflectorModel.setItemText(0, QCoreApplication.translate("inputTextArea", u"B", None))
        self.reflectorModel.setItemText(1, QCoreApplication.translate("inputTextArea", u"C", None))

        self.label_12.setText(QCoreApplication.translate("inputTextArea", u"Initial position", None))
        self.label_13.setText(QCoreApplication.translate("inputTextArea", u"Ring setting", None))
        self.label_16.setText(QCoreApplication.translate("inputTextArea", u"Cipher Text", None))
        self.exportToFile.setText(QCoreApplication.translate("inputTextArea", u"Export to file", None))
    # retranslateUi

