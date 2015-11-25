#ifndef GRIMECLEANER_H
#define GRIMECLEANER_H

#include <QMainWindow>

namespace Ui {
class grimeCleaner;
}

class grimeCleaner : public QMainWindow
{
    Q_OBJECT

public:
    explicit grimeCleaner(QWidget *parent = 0);
    ~grimeCleaner();


private:
    Ui::grimeCleaner *ui;


private slots:

void open_spybots();
void open_ccleaner();
void open_malwarebytes();
void clean_prefetch();
void install_software();
void launch_diskcleanup();
};

#endif // GRIMECLEANER_H
