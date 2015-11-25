#include "mainwindow.h"
#include <QApplication>
#include <QTextEdit>
#include <QPushButton>  //Every Widget has a header named after it
#include <QVBoxLayout>
#include <QWidget>
#include <QtGui>



int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    //As a side note the html tags can be used to change program style
    QTextEdit *textEdit = new QTextEdit("<h1 style=color:red >Hello world</h1>"); //need to be pointers to send and receive signals
    QPushButton *quitButton = new QPushButton("&Quit");

    //As a rule of thumb you should always place QObjects on the heap (pointers) and never on the stack, which is why
    // textedut and quit button are on the heap
    QObject::connect(quitButton, SIGNAL(clicked()), qApp, SLOT(quit())); //connects button quitButton to an event





    //QString myString();

    QVBoxLayout *layout = new QVBoxLayout;
    layout->addWidget(textEdit);
    layout->addWidget(quitButton);
    QWidget window;
    window.setLayout(layout);

    window.show();
    return a.exec();

}
