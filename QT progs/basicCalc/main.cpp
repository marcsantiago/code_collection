#include "basiccalc.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    basicCalc w;
    w.show();

    return a.exec();
}
