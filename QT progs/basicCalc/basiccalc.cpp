#include "basiccalc.h"
#include "ui_basiccalc.h"
int one, two; //set up set up storage values
basicCalc::basicCalc(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::basicCalc)
{

    ui->setupUi(this);
    ui->lineEdit->setText("0"); // set the line edit with a basic value

    connect(ui->addButton, SIGNAL(clicked()), this, SLOT(add()));


}

basicCalc::~basicCalc()
{
    delete ui;
}

void basicCalc::add(){
    int counter = 0;
    QString numberOne;
    numberOne = ui->lineEdit->text();
    int o = numberOne.toInt();
    one = o;
    if(counter == 1){
        QString numberTwo;
        numberTwo = ui->lineEdit->text();
        int t = numberTwo.toInt();
        two = t;
    }
    else if(counter == 2){
        int value = 0;
        value = one + two;
        QString val = QString::number(value);
        ui->lineEdit->setText(val);
    }
    counter++;
}

