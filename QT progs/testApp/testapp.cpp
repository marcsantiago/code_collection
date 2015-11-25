#include "testapp.h"
#include "ui_testapp.h"

testapp::testapp(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::testapp)
{
    ui->setupUi(this);
}

testapp::~testapp()
{
    delete ui;
}
