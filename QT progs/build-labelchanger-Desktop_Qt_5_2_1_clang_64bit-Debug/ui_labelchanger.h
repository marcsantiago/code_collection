/********************************************************************************
** Form generated from reading UI file 'labelchanger.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LABELCHANGER_H
#define UI_LABELCHANGER_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_labelchanger
{
public:
    QWidget *centralWidget;
    QPushButton *setButton;
    QPushButton *cancelButton;
    QLabel *label;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *labelchanger)
    {
        if (labelchanger->objectName().isEmpty())
            labelchanger->setObjectName(QStringLiteral("labelchanger"));
        labelchanger->resize(486, 300);
        centralWidget = new QWidget(labelchanger);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        setButton = new QPushButton(centralWidget);
        setButton->setObjectName(QStringLiteral("setButton"));
        setButton->setGeometry(QRect(60, 110, 114, 32));
        cancelButton = new QPushButton(centralWidget);
        cancelButton->setObjectName(QStringLiteral("cancelButton"));
        cancelButton->setGeometry(QRect(210, 110, 114, 32));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(0, 0, 481, 91));
        labelchanger->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(labelchanger);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 486, 22));
        labelchanger->setMenuBar(menuBar);
        mainToolBar = new QToolBar(labelchanger);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        labelchanger->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(labelchanger);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        labelchanger->setStatusBar(statusBar);

        retranslateUi(labelchanger);

        QMetaObject::connectSlotsByName(labelchanger);
    } // setupUi

    void retranslateUi(QMainWindow *labelchanger)
    {
        labelchanger->setWindowTitle(QApplication::translate("labelchanger", "labelchanger", 0));
        setButton->setText(QApplication::translate("labelchanger", "Set Label", 0));
        cancelButton->setText(QApplication::translate("labelchanger", "Cancel", 0));
        label->setText(QApplication::translate("labelchanger", "TextLabel", 0));
    } // retranslateUi

};

namespace Ui {
    class labelchanger: public Ui_labelchanger {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LABELCHANGER_H
