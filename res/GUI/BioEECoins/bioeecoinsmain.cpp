#include "bioeecoinsmain.h"
#include "ui_bioeecoinsmain.h"

BioEECoinsMain::BioEECoinsMain(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::BioEECoinsMain)
{
    ui->setupUi(this);
}

BioEECoinsMain::~BioEECoinsMain()
{
    delete ui;
}
