#include "mainwindow.h"
#include "ui_mainwindow.h"
 #include <QIntValidator>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    //Create validator that only allows numbers
    QValidator *validator = new QIntValidator(0, 30000, this);


    //Set validator to all QLineEdits on display
    QList<QLineEdit *> diatomCount = ui->centralWidget->findChildren<QLineEdit *>();
    foreach(QLineEdit *box,diatomCount ){
         box->setValidator(validator);
    }


    //set PTI values
    ui->pti->setText("0");
    ui->pti_2->setText("1");
    ui->pti_3->setText("2");
    ui->pti_4->setText("1");

    //Set Pti Values to read only
    QList<QLineEdit *> ptiValue = ui->ptiWidget->findChildren<QLineEdit *>();
    foreach(QLineEdit *box,ptiValue ){
         box->setReadOnly(true);
    }


    //Button connections
    connect(ui->pushButton, SIGNAL(clicked()), this, SLOT(calculatePTI()));

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::calculatePTI() {
    QString count;
    double myCount = 0;
    QList<QLineEdit *> diatomCount = ui->centralWidget->findChildren<QLineEdit *>(); //needs to be fixed in designer section off
    foreach(QLineEdit *dc,diatomCount ){
        count = dc->text();
        myCount += count.toDouble();
    }

    QString stringCount = QString::number(myCount);

    ui->ptiOutput->setText(stringCount);

}
