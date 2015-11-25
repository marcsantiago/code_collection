/********************************************************************************
** Form generated from reading UI file 'grimecleaner.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GRIMECLEANER_H
#define UI_GRIMECLEANER_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_grimeCleaner
{
public:
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *tab;
    QTextEdit *textEdit;
    QPushButton *backButton;
    QWidget *layoutWidget;
    QVBoxLayout *verticalLayout_2;
    QPushButton *installCleanMyMacButton;
    QPushButton *cleanMyMacButton;
    QPushButton *diskButton;
    QWidget *tab2;
    QTextEdit *textEdit_2;
    QWidget *layoutWidget1;
    QVBoxLayout *verticalLayout;
    QPushButton *malwarebytesButton;
    QPushButton *spybotButton;
    QPushButton *ccleanerButton;
    QPushButton *prefetchButton;
    QPushButton *installsoftwareButton;
    QMenuBar *menuBar;
    QMenu *menuGrime_Cleaner_Pro;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *grimeCleaner)
    {
        if (grimeCleaner->objectName().isEmpty())
            grimeCleaner->setObjectName(QStringLiteral("grimeCleaner"));
        grimeCleaner->resize(542, 414);
        grimeCleaner->setToolButtonStyle(Qt::ToolButtonTextOnly);
        centralWidget = new QWidget(grimeCleaner);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setGeometry(QRect(0, 0, 541, 361));
        tabWidget->setAutoFillBackground(false);
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        textEdit = new QTextEdit(tab);
        textEdit->setObjectName(QStringLiteral("textEdit"));
        textEdit->setGeometry(QRect(220, 0, 311, 321));
        textEdit->setReadOnly(true);
        backButton = new QPushButton(tab);
        backButton->setObjectName(QStringLiteral("backButton"));
        backButton->setGeometry(QRect(220, 290, 114, 32));
        layoutWidget = new QWidget(tab);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(0, 0, 163, 100));
        verticalLayout_2 = new QVBoxLayout(layoutWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        installCleanMyMacButton = new QPushButton(layoutWidget);
        installCleanMyMacButton->setObjectName(QStringLiteral("installCleanMyMacButton"));
        installCleanMyMacButton->setEnabled(true);

        verticalLayout_2->addWidget(installCleanMyMacButton);

        cleanMyMacButton = new QPushButton(layoutWidget);
        cleanMyMacButton->setObjectName(QStringLiteral("cleanMyMacButton"));

        verticalLayout_2->addWidget(cleanMyMacButton);

        diskButton = new QPushButton(layoutWidget);
        diskButton->setObjectName(QStringLiteral("diskButton"));

        verticalLayout_2->addWidget(diskButton);

        tabWidget->addTab(tab, QString());
        tab2 = new QWidget();
        tab2->setObjectName(QStringLiteral("tab2"));
        textEdit_2 = new QTextEdit(tab2);
        textEdit_2->setObjectName(QStringLiteral("textEdit_2"));
        textEdit_2->setGeometry(QRect(220, 0, 311, 321));
        textEdit_2->setReadOnly(true);
        layoutWidget1 = new QWidget(tab2);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(0, 0, 166, 168));
        verticalLayout = new QVBoxLayout(layoutWidget1);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        malwarebytesButton = new QPushButton(layoutWidget1);
        malwarebytesButton->setObjectName(QStringLiteral("malwarebytesButton"));

        verticalLayout->addWidget(malwarebytesButton);

        spybotButton = new QPushButton(layoutWidget1);
        spybotButton->setObjectName(QStringLiteral("spybotButton"));

        verticalLayout->addWidget(spybotButton);

        ccleanerButton = new QPushButton(layoutWidget1);
        ccleanerButton->setObjectName(QStringLiteral("ccleanerButton"));

        verticalLayout->addWidget(ccleanerButton);

        prefetchButton = new QPushButton(layoutWidget1);
        prefetchButton->setObjectName(QStringLiteral("prefetchButton"));

        verticalLayout->addWidget(prefetchButton);

        installsoftwareButton = new QPushButton(layoutWidget1);
        installsoftwareButton->setObjectName(QStringLiteral("installsoftwareButton"));

        verticalLayout->addWidget(installsoftwareButton);

        tabWidget->addTab(tab2, QString());
        grimeCleaner->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(grimeCleaner);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 542, 22));
        menuGrime_Cleaner_Pro = new QMenu(menuBar);
        menuGrime_Cleaner_Pro->setObjectName(QStringLiteral("menuGrime_Cleaner_Pro"));
        grimeCleaner->setMenuBar(menuBar);
        mainToolBar = new QToolBar(grimeCleaner);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        grimeCleaner->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(grimeCleaner);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        grimeCleaner->setStatusBar(statusBar);

        menuBar->addAction(menuGrime_Cleaner_Pro->menuAction());

        retranslateUi(grimeCleaner);

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(grimeCleaner);
    } // setupUi

    void retranslateUi(QMainWindow *grimeCleaner)
    {
        grimeCleaner->setWindowTitle(QApplication::translate("grimeCleaner", "Grame Cleaner Pro", 0));
        backButton->setText(QApplication::translate("grimeCleaner", "Back", 0));
        installCleanMyMacButton->setText(QApplication::translate("grimeCleaner", "Install CleanMyMac", 0));
        cleanMyMacButton->setText(QApplication::translate("grimeCleaner", "Open CleanMyMac", 0));
        diskButton->setText(QApplication::translate("grimeCleaner", "Open Disk Utility", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("grimeCleaner", "Mac User", 0));
        malwarebytesButton->setText(QApplication::translate("grimeCleaner", "Open Malwarebytes", 0));
        spybotButton->setText(QApplication::translate("grimeCleaner", "Open Spybots", 0));
        ccleanerButton->setText(QApplication::translate("grimeCleaner", "Open Ccleaner", 0));
        prefetchButton->setText(QApplication::translate("grimeCleaner", "Clean Prefetch", 0));
        installsoftwareButton->setText(QApplication::translate("grimeCleaner", "Install Software", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab2), QApplication::translate("grimeCleaner", "Windows User", 0));
        menuGrime_Cleaner_Pro->setTitle(QApplication::translate("grimeCleaner", "Grime Cleaner Pro", 0));
    } // retranslateUi

};

namespace Ui {
    class grimeCleaner: public Ui_grimeCleaner {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GRIMECLEANER_H
