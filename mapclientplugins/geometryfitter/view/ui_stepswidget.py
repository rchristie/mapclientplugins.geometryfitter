# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stepswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from cmlibs.widgets.draggablelistwidget import DraggableListWidget
from mapclientplugins.geometryfitter.view.alignwidget import AlignWidget
from mapclientplugins.geometryfitter.view.configwidget import ConfigWidget
from mapclientplugins.geometryfitter.view.fitwidget import FitWidget
from mapclientplugins.geometryfitter.view.groupsettingswidget import GroupSettingsWidget
from mapclientplugins.geometryfitter.view.initialconfigwidget import InitialConfigWidget

class Ui_Steps(object):
    def setupUi(self, Steps):
        if not Steps.objectName():
            Steps.setObjectName(u"Steps")
        Steps.resize(477, 346)
        self.verticalLayout = QVBoxLayout(Steps)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stepsAddDelete_frame = QFrame(Steps)
        self.stepsAddDelete_frame.setObjectName(u"stepsAddDelete_frame")
        self.stepsAddDelete_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.stepsAddDelete_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stepsAddAlign_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsAddAlign_pushButton.setObjectName(u"stepsAddAlign_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsAddAlign_pushButton)

        self.stepsAddConfig_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsAddConfig_pushButton.setObjectName(u"stepsAddConfig_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsAddConfig_pushButton)

        self.stepsAddFit_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsAddFit_pushButton.setObjectName(u"stepsAddFit_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsAddFit_pushButton)

        self.stepsDelete_pushButton = QPushButton(self.stepsAddDelete_frame)
        self.stepsDelete_pushButton.setObjectName(u"stepsDelete_pushButton")

        self.horizontalLayout_10.addWidget(self.stepsDelete_pushButton)


        self.verticalLayout.addWidget(self.stepsAddDelete_frame)

        self.steps_listWidget = DraggableListWidget(Steps)
        self.steps_listWidget.setObjectName(u"steps_listWidget")

        self.verticalLayout.addWidget(self.steps_listWidget)

        self.stepedit_scrollArea = QScrollArea(Steps)
        self.stepedit_scrollArea.setObjectName(u"stepedit_scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepedit_scrollArea.sizePolicy().hasHeightForWidth())
        self.stepedit_scrollArea.setSizePolicy(sizePolicy)
        self.stepedit_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stepedit_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.stepedit_scrollArea.setWidgetResizable(True)
        self.stepedit_scrollAreaWidgetContents = QWidget()
        self.stepedit_scrollAreaWidgetContents.setObjectName(u"stepedit_scrollAreaWidgetContents")
        self.stepedit_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 453, 114))
        self.verticalLayout_3 = QVBoxLayout(self.stepedit_scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.initialConfig_widget = InitialConfigWidget(self.stepedit_scrollAreaWidgetContents)
        self.initialConfig_widget.setObjectName(u"initialConfig_widget")

        self.verticalLayout_3.addWidget(self.initialConfig_widget)

        self.align_widget = AlignWidget(self.stepedit_scrollAreaWidgetContents)
        self.align_widget.setObjectName(u"align_widget")

        self.verticalLayout_3.addWidget(self.align_widget)

        self.fit_widget = FitWidget(self.stepedit_scrollAreaWidgetContents)
        self.fit_widget.setObjectName(u"fit_widget")

        self.verticalLayout_3.addWidget(self.fit_widget)

        self.config_widget = ConfigWidget(self.stepedit_scrollAreaWidgetContents)
        self.config_widget.setObjectName(u"config_widget")

        self.verticalLayout_3.addWidget(self.config_widget)

        self.groupSettings_widget = GroupSettingsWidget(self.stepedit_scrollAreaWidgetContents)
        self.groupSettings_widget.setObjectName(u"groupSettings_widget")

        self.verticalLayout_3.addWidget(self.groupSettings_widget)

        self.stepedit_scrollArea.setWidget(self.stepedit_scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.stepedit_scrollArea)


        self.retranslateUi(Steps)

        QMetaObject.connectSlotsByName(Steps)
    # setupUi

    def retranslateUi(self, Steps):
        Steps.setWindowTitle(QCoreApplication.translate("Steps", u"Steps", None))
        self.stepsAddAlign_pushButton.setText(QCoreApplication.translate("Steps", u"Add Align", None))
        self.stepsAddConfig_pushButton.setText(QCoreApplication.translate("Steps", u"Add Config", None))
        self.stepsAddFit_pushButton.setText(QCoreApplication.translate("Steps", u"Add Fit", None))
        self.stepsDelete_pushButton.setText(QCoreApplication.translate("Steps", u"Delete", None))
    # retranslateUi

