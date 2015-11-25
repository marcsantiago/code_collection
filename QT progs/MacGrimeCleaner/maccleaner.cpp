#include "maccleaner.h"
#include "ui_maccleaner.h"

macCleaner::macCleaner(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::macCleaner)
{
    ui->setupUi(this);
}

macCleaner::~macCleaner()
{
    delete ui;
}
