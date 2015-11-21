#ifndef BIOEECOINSMAIN_H
#define BIOEECOINSMAIN_H

#include <QMainWindow>

namespace Ui {
class BioEECoinsMain;
}

class BioEECoinsMain : public QMainWindow
{
    Q_OBJECT

public:
    explicit BioEECoinsMain(QWidget *parent = 0);
    ~BioEECoinsMain();

private:
    Ui::BioEECoinsMain *ui;
};

#endif // BIOEECOINSMAIN_H
