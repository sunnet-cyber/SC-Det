from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QLineEdit
from detUI import Ui_Dialog
import sys

from detect import detect

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('簡中掃描')
        # Set Window Icon
        # self.setWindowIcon(QtGui.QIcon(''))

        self.ui.selectDirButton.clicked.connect(self.getDir)
        self.ui.selectFileButton.clicked.connect(self.getFile)
        self.ui.startScanButton.clicked.connect(self.detectInit)

        self.ui.textBrowser.setAcceptRichText(True)
        self.ui.textBrowser.setOpenExternalLinks(True)


    def getDir(self):
        directory = QFileDialog.getExistingDirectory(self, "select")
        directory = QtCore.QDir.toNativeSeparators(directory)
        self.ui.scanFilePrompt.setText("{}".format(directory))

    def getFile(self):
        filename, filetype = QFileDialog.getOpenFileName(self, 'select')
        filename = QtCore.QDir.toNativeSeparators(filename)
        self.ui.scanFilePrompt.setText("{}".format(filename))

    def detectInit(self):
        self.ui.textBrowser.clear()

        for value in detect(self.ui.scanFilePrompt.toPlainText()):
            self.ui.textBrowser.append(value)

        if len(self.ui.textBrowser.toPlainText()) == 0:
            self.ui.textBrowser.append("未檢測到簡體中文內容")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())