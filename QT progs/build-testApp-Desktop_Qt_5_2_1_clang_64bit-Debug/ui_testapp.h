/********************************************************************************
** Form generated from reading UI file 'testapp.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TESTAPP_H
#define UI_TESTAPP_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_testapp
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *testapp)
    {
        if (testapp->objectName().isEmpty())
            testapp->setObjectName(QStringLiteral("testapp"));
        testapp->resize(400, 300);
        menuBar = new QMenuBar(testapp);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        testapp->setMenuBar(menuBar);
        mainToolBar = new QToolBar(testapp);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        testapp->addToolBar(mainToolBar);
        centralWidget = new QWidget(testapp);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        testapp->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(testapp);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        testapp->setStatusBar(statusBar);

        retranslateUi(testapp);

        QMetaObject::connectSlotsByName(testapp);
    } // setupUi

    void retranslateUi(QMainWindow *testapp)
    {
        testapp->setWindowTitle(QApplication::translate("testapp", "testapp", 0));
    } // retranslateUi

};

namespace Ui {
    class testapp: public Ui_testapp {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TESTAPP_H
