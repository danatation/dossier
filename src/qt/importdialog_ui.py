# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QLineEdit, QRadioButton,
    QSizePolicy, QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(441, 286)
        self.gridLayout_7 = QGridLayout(Dialog)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.importLayout = QGridLayout()
        self.importLayout.setObjectName(u"importLayout")
        self.nameGroupBox = QGroupBox(Dialog)
        self.nameGroupBox.setObjectName(u"nameGroupBox")
        self.gridLayout_3 = QGridLayout(self.nameGroupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.nameEdit = QLineEdit(self.nameGroupBox)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout_3.addWidget(self.nameEdit, 0, 0, 1, 1)


        self.importLayout.addWidget(self.nameGroupBox, 0, 0, 1, 1)

        self.locationGroupBox = QGroupBox(Dialog)
        self.locationGroupBox.setObjectName(u"locationGroupBox")
        self.gridLayout_4 = QGridLayout(self.locationGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.locationEdit = QLineEdit(self.locationGroupBox)
        self.locationEdit.setObjectName(u"locationEdit")

        self.gridLayout_4.addWidget(self.locationEdit, 0, 0, 1, 1)

        self.locationToolButton = QToolButton(self.locationGroupBox)
        self.locationToolButton.setObjectName(u"locationToolButton")

        self.gridLayout_4.addWidget(self.locationToolButton, 0, 1, 1, 1)


        self.importLayout.addWidget(self.locationGroupBox, 1, 0, 1, 1)

        self.methodGroup = QGroupBox(Dialog)
        self.methodGroup.setObjectName(u"methodGroup")
        self.gridLayout_5 = QGridLayout(self.methodGroup)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.symlinkRadio = QRadioButton(self.methodGroup)
        self.symlinkRadio.setObjectName(u"symlinkRadio")

        self.gridLayout_5.addWidget(self.symlinkRadio, 0, 1, 1, 1)

        self.copyRadio = QRadioButton(self.methodGroup)
        self.copyRadio.setObjectName(u"copyRadio")
        self.copyRadio.setChecked(True)

        self.gridLayout_5.addWidget(self.copyRadio, 0, 0, 1, 1)


        self.importLayout.addWidget(self.methodGroup, 2, 0, 1, 1)


        self.gridLayout_7.addLayout(self.importLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_7.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.nameGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Name", None))
        self.nameEdit.setInputMask("")
        self.nameEdit.setPlaceholderText("")
        self.locationGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Location", None))
        self.locationEdit.setInputMask("")
        self.locationEdit.setPlaceholderText("")
        self.locationToolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.methodGroup.setTitle(QCoreApplication.translate("Dialog", u"Install Method", None))
        self.symlinkRadio.setText(QCoreApplication.translate("Dialog", u"Symlink DDLC files", None))
        self.copyRadio.setText(QCoreApplication.translate("Dialog", u"Copy DDLC files", None))
    # retranslateUi

