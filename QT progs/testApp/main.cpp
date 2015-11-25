#include "testapp.h"
#include <QApplication>
#include <QLabel>
#include <QLineEdit>
#include <QVBoxLayout>
#include <QWidget>
#include <QtGui>
#include <QPushButton>

slots void changeText();

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);


    slots void changeText();

    QLabel *label = new QLabel("&Find Cell");
    QLineEdit *lineEdit = new QLineEdit();
    label->setBuddy(lineEdit);

    QPushButton *okButton = new QPushButton("ok");
    QPushButton *cancelButton = new QPushButton("cancel");


   // QObject::connect(okButton, SIGNAL(clicked()), this, SLOT());
    QObject::connect(cancelButton, SIGNAL(clicked()), qApp, SLOT(quit()));

    QVBoxLayout *layout = new QVBoxLayout();
    layout->addWidget(label);
    layout->addWidget(lineEdit);

    layout->addWidget(okButton);
    layout->addWidget(cancelButton);





    QWidget window;
    window.setLayout(layout);

    window.show();

    return a.exec();
}



