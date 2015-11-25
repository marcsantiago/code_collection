#ifndef TESTAPP_H
#define TESTAPP_H

#include <QMainWindow>

namespace Ui {
class testapp;
}

class testapp : public QMainWindow
{
    Q_OBJECT

public:
    explicit testapp(QWidget *parent = 0);
    ~testapp();

private:
    Ui::testapp *ui;



};

#endif // TESTAPP_H
