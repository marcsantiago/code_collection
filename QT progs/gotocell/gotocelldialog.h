#ifndef GOTOCELLDIALOG_H
#define GOTOCELLDIALOG_H

#include <QDialog>

namespace Ui {
class gotocelldialog;
}

class gotocelldialog : public QDialog
{
    Q_OBJECT

public:
    explicit gotocelldialog(QWidget *parent = 0);
    ~gotocelldialog();

private:
    Ui::gotocelldialog *ui;

private slots:
    void on_lineEdit_textChanged();
};

#endif // GOTOCELLDIALOG_H
