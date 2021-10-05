import sys

from PySide6.QtGui import QFontDatabase, QFont, QIcon
from PySide6.QtCore import QFile, QTextStream, QTranslator, QLocale
from PySide6.QtWidgets import QApplication

from .MainWindow import MainWindow

from ._ui import resources_rc  # noqa


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(':/icons/app.svg'))

    QFontDatabase.addApplicationFont(':/fonts/Roboto-Regular.ttf')
    app.setFont(QFont('Roboto'))

    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    translator.load(':/translations/' + QLocale.system().name() + '.qm')
    app.installTranslator(translator)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
