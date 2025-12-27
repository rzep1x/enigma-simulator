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
    QSizePolicy, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_inputTextArea(object):
    def setupUi(self, inputTextArea):
        if not inputTextArea.objectName():
            inputTextArea.setObjectName(u"inputTextArea")
        inputTextArea.resize(1168, 662)
        self.layoutWidget = QWidget(inputTextArea)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 31, 1141, 621))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.chooseFileButton = QPushButton(self.layoutWidget)
        self.chooseFileButton.setObjectName(u"chooseFileButton")

        self.verticalLayout.addWidget(self.chooseFileButton)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_11)


        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_13)


        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.rotor2Model = QComboBox(self.groupBox)
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.addItem("")
        self.rotor2Model.setObjectName(u"rotor2Model")
        sizePolicy.setHeightForWidth(self.rotor2Model.sizePolicy().hasHeightForWidth())
        self.rotor2Model.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.rotor2Model, 5, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rotor2InitialPosition = QSpinBox(self.groupBox)
        self.rotor2InitialPosition.setObjectName(u"rotor2InitialPosition")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rotor2InitialPosition.sizePolicy().hasHeightForWidth())
        self.rotor2InitialPosition.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.rotor2InitialPosition)

        self.rotor2RingSetting = QSpinBox(self.groupBox)
        self.rotor2RingSetting.setObjectName(u"rotor2RingSetting")
        sizePolicy1.setHeightForWidth(self.rotor2RingSetting.sizePolicy().hasHeightForWidth())
        self.rotor2RingSetting.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.rotor2RingSetting)


        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)

        self.rotor1Model = QComboBox(self.groupBox)
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.addItem("")
        self.rotor1Model.setObjectName(u"rotor1Model")
        sizePolicy.setHeightForWidth(self.rotor1Model.sizePolicy().hasHeightForWidth())
        self.rotor1Model.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.rotor1Model, 1, 0, 1, 1)

        self.plugboard = QLineEdit(self.groupBox)
        self.plugboard.setObjectName(u"plugboard")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plugboard.sizePolicy().hasHeightForWidth())
        self.plugboard.setSizePolicy(sizePolicy2)
        self.plugboard.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plugboard.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plugboard.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.plugboard, 15, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)

        self.rotor3Model = QComboBox(self.groupBox)
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.addItem("")
        self.rotor3Model.setObjectName(u"rotor3Model")
        sizePolicy.setHeightForWidth(self.rotor3Model.sizePolicy().hasHeightForWidth())
        self.rotor3Model.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.rotor3Model, 9, 0, 1, 1)

        self.reflectorModel = QComboBox(self.groupBox)
        self.reflectorModel.addItem("")
        self.reflectorModel.addItem("")
        self.reflectorModel.setObjectName(u"reflectorModel")
        sizePolicy.setHeightForWidth(self.reflectorModel.sizePolicy().hasHeightForWidth())
        self.reflectorModel.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.reflectorModel, 13, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rotor3InitialPosition = QSpinBox(self.groupBox)
        self.rotor3InitialPosition.setObjectName(u"rotor3InitialPosition")
        sizePolicy.setHeightForWidth(self.rotor3InitialPosition.sizePolicy().hasHeightForWidth())
        self.rotor3InitialPosition.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.rotor3InitialPosition)

        self.rotor3RingSetting = QSpinBox(self.groupBox)
        self.rotor3RingSetting.setObjectName(u"rotor3RingSetting")
        sizePolicy.setHeightForWidth(self.rotor3RingSetting.sizePolicy().hasHeightForWidth())
        self.rotor3RingSetting.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.rotor3RingSetting)


        self.gridLayout.addLayout(self.horizontalLayout_6, 11, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_7)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rotor1InitialPosition = QSpinBox(self.groupBox)
        self.rotor1InitialPosition.setObjectName(u"rotor1InitialPosition")
        sizePolicy.setHeightForWidth(self.rotor1InitialPosition.sizePolicy().hasHeightForWidth())
        self.rotor1InitialPosition.setSizePolicy(sizePolicy)
        self.rotor1InitialPosition.setMaximum(25)

        self.horizontalLayout_4.addWidget(self.rotor1InitialPosition)

        self.rotor1RingSetting = QSpinBox(self.groupBox)
        self.rotor1RingSetting.setObjectName(u"rotor1RingSetting")
        sizePolicy.setHeightForWidth(self.rotor1RingSetting.sizePolicy().hasHeightForWidth())
        self.rotor1RingSetting.setSizePolicy(sizePolicy)
        self.rotor1RingSetting.setMaximum(25)

        self.horizontalLayout_4.addWidget(self.rotor1RingSetting)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_14, 12, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.saveButton)

        self.clearButton = QPushButton(self.groupBox)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy3.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.clearButton)

        self.loadButton = QPushButton(self.groupBox)
        self.loadButton.setObjectName(u"loadButton")
        sizePolicy3.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.loadButton)


        self.gridLayout.addLayout(self.horizontalLayout, 16, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_16)

        self.outputText = QTextEdit(self.layoutWidget)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setAutoFillBackground(False)
        self.outputText.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.outputText)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.retranslateUi(inputTextArea)

        QMetaObject.connectSlotsByName(inputTextArea)
    # setupUi

    def retranslateUi(self, inputTextArea):
        inputTextArea.setWindowTitle(QCoreApplication.translate("inputTextArea", u"Form", None))
        self.label.setText(QCoreApplication.translate("inputTextArea", u"Plain Text", None))
        self.chooseFileButton.setText(QCoreApplication.translate("inputTextArea", u"Choose file", None))
        self.groupBox.setTitle("")
        self.label_10.setText(QCoreApplication.translate("inputTextArea", u"Initial position", None))
        self.label_11.setText(QCoreApplication.translate("inputTextArea", u"Ring Setting", None))
        self.label_12.setText(QCoreApplication.translate("inputTextArea", u"Initial position", None))
        self.label_13.setText(QCoreApplication.translate("inputTextArea", u"Ring setting", None))
        self.label_4.setText(QCoreApplication.translate("inputTextArea", u"Rotor 2", None))
        self.rotor2Model.setItemText(0, QCoreApplication.translate("inputTextArea", u"I", None))
        self.rotor2Model.setItemText(1, QCoreApplication.translate("inputTextArea", u"II", None))
        self.rotor2Model.setItemText(2, QCoreApplication.translate("inputTextArea", u"III", None))
        self.rotor2Model.setItemText(3, QCoreApplication.translate("inputTextArea", u"IV", None))
        self.rotor2Model.setItemText(4, QCoreApplication.translate("inputTextArea", u"V", None))

        self.rotor1Model.setItemText(0, QCoreApplication.translate("inputTextArea", u"I", None))
        self.rotor1Model.setItemText(1, QCoreApplication.translate("inputTextArea", u"II", None))
        self.rotor1Model.setItemText(2, QCoreApplication.translate("inputTextArea", u"III", None))
        self.rotor1Model.setItemText(3, QCoreApplication.translate("inputTextArea", u"IV", None))
        self.rotor1Model.setItemText(4, QCoreApplication.translate("inputTextArea", u"V", None))

        self.label_15.setText(QCoreApplication.translate("inputTextArea", u"Plugboard", None))
        self.rotor3Model.setItemText(0, QCoreApplication.translate("inputTextArea", u"I", None))
        self.rotor3Model.setItemText(1, QCoreApplication.translate("inputTextArea", u"II", None))
        self.rotor3Model.setItemText(2, QCoreApplication.translate("inputTextArea", u"III", None))
        self.rotor3Model.setItemText(3, QCoreApplication.translate("inputTextArea", u"IV", None))
        self.rotor3Model.setItemText(4, QCoreApplication.translate("inputTextArea", u"V", None))

        self.reflectorModel.setItemText(0, QCoreApplication.translate("inputTextArea", u"B", None))
        self.reflectorModel.setItemText(1, QCoreApplication.translate("inputTextArea", u"C", None))

        self.label_6.setText(QCoreApplication.translate("inputTextArea", u"Initial position", None))
        self.label_7.setText(QCoreApplication.translate("inputTextArea", u"Ring Setting", None))
        self.label_2.setText(QCoreApplication.translate("inputTextArea", u"Rotor 1", None))
        self.label_5.setText(QCoreApplication.translate("inputTextArea", u"Rotor 3", None))
        self.label_14.setText(QCoreApplication.translate("inputTextArea", u"Reflector", None))
        self.saveButton.setText(QCoreApplication.translate("inputTextArea", u"Save", None))
        self.clearButton.setText(QCoreApplication.translate("inputTextArea", u"Clear", None))
        self.loadButton.setText(QCoreApplication.translate("inputTextArea", u"Load", None))
        self.label_16.setText(QCoreApplication.translate("inputTextArea", u"Cipher Text", None))
    # retranslateUi

