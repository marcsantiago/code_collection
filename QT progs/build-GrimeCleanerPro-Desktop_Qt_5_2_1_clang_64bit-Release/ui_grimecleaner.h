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
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_grimeCleaner
{
public:
    QWidget *centralWidget;
    QPlainTextEdit *plainTextEdit;
    QWidget *verticalLayoutWidget;
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
        plainTextEdit = new QPlainTextEdit(centralWidget);
        plainTextEdit->setObjectName(QStringLiteral("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(180, 0, 371, 361));
        verticalLayoutWidget = new QWidget(centralWidget);
        verticalLayoutWidget->setObjectName(QStringLiteral("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(0, 0, 181, 361));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        malwarebytesButton = new QPushButton(verticalLayoutWidget);
        malwarebytesButton->setObjectName(QStringLiteral("malwarebytesButton"));

        verticalLayout->addWidget(malwarebytesButton);

        spybotButton = new QPushButton(verticalLayoutWidget);
        spybotButton->setObjectName(QStringLiteral("spybotButton"));

        verticalLayout->addWidget(spybotButton);

        ccleanerButton = new QPushButton(verticalLayoutWidget);
        ccleanerButton->setObjectName(QStringLiteral("ccleanerButton"));

        verticalLayout->addWidget(ccleanerButton);

        prefetchButton = new QPushButton(verticalLayoutWidget);
        prefetchButton->setObjectName(QStringLiteral("prefetchButton"));

        verticalLayout->addWidget(prefetchButton);

        installsoftwareButton = new QPushButton(verticalLayoutWidget);
        installsoftwareButton->setObjectName(QStringLiteral("installsoftwareButton"));

        verticalLayout->addWidget(installsoftwareButton);

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

        QMetaObject::connectSlotsByName(grimeCleaner);
    } // setupUi

    void retranslateUi(QMainWindow *grimeCleaner)
    {
        grimeCleaner->setWindowTitle(QApplication::translate("grimeCleaner", "Grame Cleaner Pro", 0));
        malwarebytesButton->setText(QApplication::translate("grimeCleaner", "Open Malwarebytes", 0));
        spybotButton->setText(QApplication::translate("grimeCleaner", "Open Spybots", 0));
        ccleanerButton->setText(QApplication::translate("grimeCleaner", "Open Ccleaner", 0));
        prefetchButton->setText(QApplication::translate("grimeCleaner", "Clean Prefetch", 0));
        installsoftwareButton->setText(QApplication::translate("grimeCleaner", "Install All Software", 0));
        menuGrime_Cleaner_Pro->setTitle(QApplication::translate("grimeCleaner", "Grime Cleaner Pro", 0));
    } // retranslateUi

};

namespace Ui {
    class grimeCleaner: public Ui_grimeCleaner {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GRIMECLEANER_H
