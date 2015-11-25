#ifndef MACCLEANER_H
#define MACCLEANER_H

#include <QMainWindow>

namespace Ui {
class macCleaner;
}

class macCleaner : public QMainWindow
{
    Q_OBJECT

public:
    explicit macCleaner(QWidget *parent = 0);
    ~macCleaner();

private:
    Ui::macCleaner *ui;
};

#endif // MACCLEANER_H
