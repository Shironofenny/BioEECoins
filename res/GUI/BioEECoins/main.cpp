#include "bioeecoinsmain.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    BioEECoinsMain w;
    w.show();

    return a.exec();
}
