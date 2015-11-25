/********************************************************************************
** Form generated from reading UI file 'gotocelldialog.ui'
**
** Created by: Qt User Interface Compiler version 5.2.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GOTOCELLDIALOG_H
#define UI_GOTOCELLDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_gotocelldialog
{
public:
    QVBoxLayout *verticalLayout;
    QSplitter *splitter_2;
    QLabel *label;
    QLineEdit *lineEdit;
    QSplitter *splitter;
    QPushButton *okButton;
    QPushButton *cancelButton;

    void setupUi(QDialog *gotocelldialog)
    {
        if (gotocelldialog->objectName().isEmpty())
            gotocelldialog->setObjectName(QStringLiteral("gotocelldialog"));
        gotocelldialog->resize(246, 93);
        verticalLayout = new QVBoxLayout(gotocelldialog);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        splitter_2 = new QSplitter(gotocelldialog);
        splitter_2->setObjectName(QStringLiteral("splitter_2"));
        splitter_2->setOrientation(Qt::Horizontal);
        label = new QLabel(splitter_2);
        label->setObjectName(QStringLiteral("label"));
        splitter_2->addWidget(label);
        lineEdit = new QLineEdit(splitter_2);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        splitter_2->addWidget(lineEdit);

        verticalLayout->addWidget(splitter_2);

        splitter = new QSplitter(gotocelldialog);
        splitter->setObjectName(QStringLiteral("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        okButton = new QPushButton(splitter);
        okButton->setObjectName(QStringLiteral("okButton"));
        okButton->setEnabled(false);
        splitter->addWidget(okButton);
        cancelButton = new QPushButton(splitter);
        cancelButton->setObjectName(QStringLiteral("cancelButton"));
        splitter->addWidget(cancelButton);

        verticalLayout->addWidget(splitter);

#ifndef QT_NO_SHORTCUT
        label->setBuddy(lineEdit);
#endif // QT_NO_SHORTCUT

        retranslateUi(gotocelldialog);

        QMetaObject::connectSlotsByName(gotocelldialog);
    } // setupUi

    void retranslateUi(QDialog *gotocelldialog)
    {
        gotocelldialog->setWindowTitle(QApplication::translate("gotocelldialog", "Go to Cell", 0));
        label->setText(QApplication::translate("gotocelldialog", "&Cell Location", 0));
        okButton->setText(QApplication::translate("gotocelldialog", "Ok", 0));
        cancelButton->setText(QApplication::translate("gotocelldialog", "Cancel", 0));
    } // retranslateUi

};

namespace Ui {
    class gotocelldialog: public Ui_gotocelldialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GOTOCELLDIALOG_H
