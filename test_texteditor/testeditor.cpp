#include "testeditor.h"
#include "ui_testeditor.h"

TestEditor::TestEditor(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TestEditor)
{
    ui->setupUi(this);
}

TestEditor::~TestEditor()
{
    delete ui;
}
