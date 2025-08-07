# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geometryfitterwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QWidget)

from cmlibs.widgets.basesceneviewerwidget import BaseSceneviewerWidget

class Ui_GeometryFitterWidget(object):
    def setupUi(self, GeometryFitterWidget):
        if not GeometryFitterWidget.objectName():
            GeometryFitterWidget.setObjectName(u"GeometryFitterWidget")
        GeometryFitterWidget.resize(800, 600)
        self.centralwidget = QWidget(GeometryFitterWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.baseSceneviewerWidget = BaseSceneviewerWidget(self.centralwidget)
        self.baseSceneviewerWidget.setObjectName(u"baseSceneviewerWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.baseSceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.baseSceneviewerWidget.setSizePolicy(sizePolicy)
        self.baseSceneviewerWidget.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.baseSceneviewerWidget)

        GeometryFitterWidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(GeometryFitterWidget)

        QMetaObject.connectSlotsByName(GeometryFitterWidget)
    # setupUi

    def retranslateUi(self, GeometryFitterWidget):
        GeometryFitterWidget.setWindowTitle(QCoreApplication.translate("GeometryFitterWidget", u"Geometry Fitter", None))
    # retranslateUi

