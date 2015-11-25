#include "labelchanger.h"
#include "ui_labelchanger.h"
#include <string>
#include <stdlib.h>

labelchanger::labelchanger(QWidget *parent) :  //conctructor
    QMainWindow(parent),
    ui(new Ui::labelchanger)
{
    ui->setupUi(this);

    ui->label->setText("Hello World");
    connect(ui->cancelButton, SIGNAL(clicked()), this, SLOT(close()));
    connect(ui->setButton, SIGNAL(clicked()), this, SLOT(textChanger()));
}

labelchanger::~labelchanger() //deconstructor
{
    delete ui;
}
 void labelchanger::textChanger(){ //label changer is the class to call a function within this class use  ::
 ui->label->setText("<p style=color:red>Can't wait to have your pussy on my dick and mouth on my cock</p>");

 }
