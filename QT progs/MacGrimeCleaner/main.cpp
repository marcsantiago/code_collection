#include "maccleaner.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    macCleaner w;
    w.show();

    return a.exec();
}
