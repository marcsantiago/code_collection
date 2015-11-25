#include "labelchanger.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    labelchanger w;
    w.show();

    return a.exec();
}
