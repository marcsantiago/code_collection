#include "gotocelldialog.h"
#include "ui_gotocelldialog.h"

gotocelldialog::gotocelldialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::gotocelldialog)
{
    ui->setupUi(this);


    QRegExp regExp("[A-Za-z][1-9][0-9]{0,2}");
    ui->lineEdit->setValidator(new QRegExpValidator(regExp, this));

    connect(ui->okButton, SIGNAL(clicked()), this, SLOT(accept()));
    connect(ui->cancelButton, SIGNAL(clicked()),this, SLOT(reject()));
}

gotocelldialog::~gotocelldialog()
{
    delete ui;
}

void gotocelldialog::on_lineEdit_textChanged(){
    ui->okButton->setEnabled(ui->lineEdit->hasAcceptableInput());
    connect(ui->lineEdit, SIGNAL(textChanged(const QString &)), this, SLOT(on_lineEdit_textChanged()));
}
