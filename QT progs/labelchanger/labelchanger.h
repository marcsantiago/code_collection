#ifndef LABELCHANGER_H
#define LABELCHANGER_H

#include <QMainWindow>

namespace Ui {
class labelchanger;
}

class labelchanger : public QMainWindow
{
    Q_OBJECT

public:
    explicit labelchanger(QWidget *parent = 0);
    ~labelchanger();

private:
    Ui::labelchanger *ui;
private slots:
    void textChanger();
};

#endif // LABELCHANGER_H
