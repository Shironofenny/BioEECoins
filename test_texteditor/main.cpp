#include "testeditor.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    TestEditor w;
    w.show();

    return a.exec();
}
