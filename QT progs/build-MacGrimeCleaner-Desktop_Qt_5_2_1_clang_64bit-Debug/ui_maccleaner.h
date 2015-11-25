/********************************************************************************
** Form generated from reading UI file 'maccleaner.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MACCLEANER_H
#define UI_MACCLEANER_H

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

class Ui_macCleaner
{
public:
    QWidget *centralWidget;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *macCleaner)
    {
        if (macCleaner->objectName().isEmpty())
            macCleaner->setObjectName(QStringLiteral("macCleaner"));
        macCleaner->resize(529, 393);
        QFont font;
        font.setFamily(QStringLiteral("Helvetica Neue"));
        macCleaner->setFont(font);
        centralWidget = new QWidget(macCleaner);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        macCleaner->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(macCleaner);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 529, 22));
        macCleaner->setMenuBar(menuBar);
        mainToolBar = new QToolBar(macCleaner);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        macCleaner->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(macCleaner);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        macCleaner->setStatusBar(statusBar);

        retranslateUi(macCleaner);

        QMetaObject::connectSlotsByName(macCleaner);
    } // setupUi

    void retranslateUi(QMainWindow *macCleaner)
    {
        macCleaner->setWindowTitle(QApplication::translate("macCleaner", "Mac Grime Cleaner", 0));
    } // retranslateUi

};

namespace Ui {
    class macCleaner: public Ui_macCleaner {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MACCLEANER_H
