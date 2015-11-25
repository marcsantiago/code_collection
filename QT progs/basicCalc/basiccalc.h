#ifndef BASICCALC_H
#define BASICCALC_H

#include <QMainWindow>

namespace Ui {
class basicCalc;
}

class basicCalc : public QMainWindow
{
    Q_OBJECT

public:
    explicit basicCalc(QWidget *parent = 0);
    ~basicCalc();

private:
    Ui::basicCalc *ui;

private slots:
    void add();


};

#endif // BASICCALC_H
