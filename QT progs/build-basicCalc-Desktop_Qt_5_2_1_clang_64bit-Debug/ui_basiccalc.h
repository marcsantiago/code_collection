/********************************************************************************
** Form generated from reading UI file 'basiccalc.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BASICCALC_H
#define UI_BASICCALC_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_basicCalc
{
public:
    QWidget *centralWidget;
    QLineEdit *lineEdit;
    QPushButton *addButton;
    QMenuBar *menuBar;
    QMenu *menuBasic_Calc;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *basicCalc)
    {
        if (basicCalc->objectName().isEmpty())
            basicCalc->setObjectName(QStringLiteral("basicCalc"));
        basicCalc->resize(164, 177);
        centralWidget = new QWidget(basicCalc);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(10, 10, 91, 21));
        addButton = new QPushButton(centralWidget);
        addButton->setObjectName(QStringLiteral("addButton"));
        addButton->setGeometry(QRect(10, 40, 41, 32));
        basicCalc->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(basicCalc);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 164, 22));
        menuBasic_Calc = new QMenu(menuBar);
        menuBasic_Calc->setObjectName(QStringLiteral("menuBasic_Calc"));
        basicCalc->setMenuBar(menuBar);
        mainToolBar = new QToolBar(basicCalc);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        basicCalc->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(basicCalc);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        basicCalc->setStatusBar(statusBar);

        menuBar->addAction(menuBasic_Calc->menuAction());

        retranslateUi(basicCalc);

        QMetaObject::connectSlotsByName(basicCalc);
    } // setupUi

    void retranslateUi(QMainWindow *basicCalc)
    {
        basicCalc->setWindowTitle(QApplication::translate("basicCalc", "basicCalc", 0));
        addButton->setText(QApplication::translate("basicCalc", "+", 0));
        menuBasic_Calc->setTitle(QApplication::translate("basicCalc", "Basic Calc", 0));
    } // retranslateUi

};

namespace Ui {
    class basicCalc: public Ui_basicCalc {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BASICCALC_H
