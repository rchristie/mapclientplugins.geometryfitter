# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorstatisticswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_ErrorStatistics(object):
    def setupUi(self, ErrorStatistics):
        if not ErrorStatistics.objectName():
            ErrorStatistics.setObjectName(u"ErrorStatistics")
        ErrorStatistics.resize(400, 300)
        self.formLayout = QFormLayout(ErrorStatistics)
        self.formLayout.setObjectName(u"formLayout")
        self.displayRMSError_label = QLabel(ErrorStatistics)
        self.displayRMSError_label.setObjectName(u"displayRMSError_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.displayRMSError_label)

        self.displayRMSError_lineEdit = QLineEdit(ErrorStatistics)
        self.displayRMSError_lineEdit.setObjectName(u"displayRMSError_lineEdit")
        self.displayRMSError_lineEdit.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.displayRMSError_lineEdit)

        self.displayMaxError_label = QLabel(ErrorStatistics)
        self.displayMaxError_label.setObjectName(u"displayMaxError_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.displayMaxError_label)

        self.displayMaxError_lineEdit = QLineEdit(ErrorStatistics)
        self.displayMaxError_lineEdit.setObjectName(u"displayMaxError_lineEdit")
        self.displayMaxError_lineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.displayMaxError_lineEdit)

        self.displayMinimumJacobianDeterminant_label = QLabel(ErrorStatistics)
        self.displayMinimumJacobianDeterminant_label.setObjectName(u"displayMinimumJacobianDeterminant_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.displayMinimumJacobianDeterminant_label)

        self.displayMinimumJacobianDeterminant_lineEdit = QLineEdit(ErrorStatistics)
        self.displayMinimumJacobianDeterminant_lineEdit.setObjectName(u"displayMinimumJacobianDeterminant_lineEdit")
        self.displayMinimumJacobianDeterminant_lineEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.displayMinimumJacobianDeterminant_lineEdit)


        self.retranslateUi(ErrorStatistics)

        QMetaObject.connectSlotsByName(ErrorStatistics)
    # setupUi

    def retranslateUi(self, ErrorStatistics):
        ErrorStatistics.setWindowTitle(QCoreApplication.translate("ErrorStatistics", u"Error Statistics", None))
        self.displayRMSError_label.setText(QCoreApplication.translate("ErrorStatistics", u"RMS error:", None))
        self.displayMaxError_label.setText(QCoreApplication.translate("ErrorStatistics", u"Maximum error:", None))
        self.displayMinimumJacobianDeterminant_label.setText(QCoreApplication.translate("ErrorStatistics", u"Min. Jacobian determinant:", None))
#if QT_CONFIG(tooltip)
        self.displayMinimumJacobianDeterminant_lineEdit.setToolTip(QCoreApplication.translate("ErrorStatistics", u"<html><head/><body><p>The value shown here is the minimum ratio of differential fitted over reference volumes in the model. If this value is near zero or negative, in general, this indicates a bad element in the model.</p><p>This calculation is only valid for 3-D volumetric elements. For 2-D and 1-D elements the calculation returns zero.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

