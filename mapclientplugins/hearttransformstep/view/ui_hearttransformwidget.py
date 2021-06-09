# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hearttransformwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclientplugins.hearttransformstep.view.transformwidget import TransformWidget


class Ui_HeartTransformWidget(object):
    def setupUi(self, HeartTransformWidget):
        if not HeartTransformWidget.objectName():
            HeartTransformWidget.setObjectName(u"HeartTransformWidget")
        HeartTransformWidget.resize(819, 567)
        self.horizontalLayout = QHBoxLayout(HeartTransformWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(HeartTransformWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet(u"QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.pageFile = QWidget()
        self.pageFile.setObjectName(u"pageFile")
        self.pageFile.setGeometry(QRect(0, 0, 124, 140))
        self.verticalLayout_2 = QVBoxLayout(self.pageFile)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonSave = QPushButton(self.pageFile)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_4.addWidget(self.pushButtonSave)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonLoad = QPushButton(self.pageFile)
        self.pushButtonLoad.setObjectName(u"pushButtonLoad")

        self.horizontalLayout_5.addWidget(self.pushButtonLoad)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonDone = QPushButton(self.pageFile)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout_3.addWidget(self.pushButtonDone)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.pageFile, u"File")
        self.pageView = QWidget()
        self.pageView.setObjectName(u"pageView")
        self.pageView.setGeometry(QRect(0, 0, 124, 192))
        self.verticalLayout_3 = QVBoxLayout(self.pageView)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonViewAll = QPushButton(self.pageView)
        self.pushButtonViewAll.setObjectName(u"pushButtonViewAll")

        self.horizontalLayout_2.addWidget(self.pushButtonViewAll)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonHideAll = QPushButton(self.pageView)
        self.pushButtonHideAll.setObjectName(u"pushButtonHideAll")

        self.horizontalLayout_6.addWidget(self.pushButtonHideAll)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.listWidget = QListWidget(self.pageView)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.listWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 238, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.pageView, u"View")
        self.pageSegmentation = QWidget()
        self.pageSegmentation.setObjectName(u"pageSegmentation")
        self.pageSegmentation.setGeometry(QRect(0, 0, 198, 426))
        self.verticalLayout_5 = QVBoxLayout(self.pageSegmentation)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.pageSegmentation)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.spinBoxPointSize = QSpinBox(self.groupBox)
        self.spinBoxPointSize.setObjectName(u"spinBoxPointSize")
        self.spinBoxPointSize.setMinimum(1)

        self.verticalLayout_4.addWidget(self.spinBoxPointSize)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.pageSegmentation)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBoxMode = QComboBox(self.groupBox_2)
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.setObjectName(u"comboBoxMode")

        self.verticalLayout_6.addWidget(self.comboBoxMode)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.toolBox.addItem(self.pageSegmentation, u"Transform")

        self.verticalLayout.addWidget(self.toolBox)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.widgetZinc = TransformWidget(HeartTransformWidget)
        self.widgetZinc.setObjectName(u"widgetZinc")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widgetZinc.sizePolicy().hasHeightForWidth())
        self.widgetZinc.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.widgetZinc)


        self.retranslateUi(HeartTransformWidget)

        self.toolBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(HeartTransformWidget)
    # setupUi

    def retranslateUi(self, HeartTransformWidget):
        HeartTransformWidget.setWindowTitle(QCoreApplication.translate("HeartTransformWidget", u"Heart Transform", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("HeartTransformWidget", u"Heart Tra&nsform Tools", None))
        self.pushButtonSave.setText(QCoreApplication.translate("HeartTransformWidget", u"Save", None))
        self.pushButtonLoad.setText(QCoreApplication.translate("HeartTransformWidget", u"Load", None))
        self.pushButtonDone.setText(QCoreApplication.translate("HeartTransformWidget", u"Done", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFile), QCoreApplication.translate("HeartTransformWidget", u"File", None))
        self.pushButtonViewAll.setText(QCoreApplication.translate("HeartTransformWidget", u"View All", None))
        self.pushButtonHideAll.setText(QCoreApplication.translate("HeartTransformWidget", u"Hide All", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageView), QCoreApplication.translate("HeartTransformWidget", u"View", None))
        self.groupBox.setTitle(QCoreApplication.translate("HeartTransformWidget", u"Point size", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("HeartTransformWidget", u"Mode", None))
        self.comboBoxMode.setItemText(0, QCoreApplication.translate("HeartTransformWidget", u"Apex", None))
        self.comboBoxMode.setItemText(1, QCoreApplication.translate("HeartTransformWidget", u"Base", None))
        self.comboBoxMode.setItemText(2, QCoreApplication.translate("HeartTransformWidget", u"RV", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.pageSegmentation), QCoreApplication.translate("HeartTransformWidget", u"Transform", None))
    # retranslateUi

