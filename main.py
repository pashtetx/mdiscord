import sys
import json
import time
import os

from queries import change_custom_status, token_validate

from PySide6 import QtCore, QtWidgets, QtGui

class DiscordWorker(QtCore.QObject):
    finished = QtCore.Signal()
    
    def __init__(
        self, 
        token: QtWidgets.QLineEdit, 
        text_widget: QtWidgets.QTextEdit,
        delay: int = 3
    ):
        super().__init__()
        self.token = token
        self.text = text_widget
        self.delay = delay

    def save(self):
        token = self.token.text()
        changes = self.text.toPlainText().split("\n")
        with open("data.json", "w") as f:
            print({"token":token, "changes":changes})
            json.dump({"token":token, "changes":changes}, f)

    def load(self):
        if not os.path.isfile("data.json"):
            return
        with open("data.json") as f:
            return json.load(f)

    def run(self):
        self.save()
        token = self.token.text()
        changes = self.text.toPlainText().split("\n")
        while True:
            QtCore.QCoreApplication.processEvents()
            for change in changes:
                change_custom_status(token, change)
                time.sleep(self.delay)

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.delay = 3
        self.button = QtWidgets.QPushButton(text="Start")
        self.token_label = QtWidgets.QLabel("Token:")
        self.token = QtWidgets.QLineEdit(
            placeholderText="Your discord token"
        )
        self.text_label = QtWidgets.QLabel("Text (Enter is separate)")
        self.text = QtWidgets.QTextEdit()
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.token_label)
        self.layout.addWidget(self.token)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon("icon.png"))
        self.tray.setVisible(True)
        
        self.menu = QtWidgets.QMenu()
        self.open_action = QtGui.QAction("Open")
        self.quit_action = QtGui.QAction("Quit")
        self.menu.addActions([self.open_action, self.quit_action])
        self.tray.setContextMenu(self.menu)

        self.open_action.triggered.connect(self.toggle)
        self.quit_action.triggered.connect(lambda: sys.exit())

        self.worker = DiscordWorker(self.token, self.text)

        self.data = self.worker.load()
        if self.data:
            self.token.setText(self.data["token"])
            self.text.setText("\n".join(self.data["changes"]))
            self.hide()
            self.start_thread()
        
        self.button.clicked.connect(self.start)

    @QtCore.Slot()
    def toggle(self):
        if self.isHidden:
            self.show()

    def start_thread(self):
        self.thread = QtCore.QThread()
        self.worker = DiscordWorker(self.token, self.text)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.exit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        
        self.thread.start()
        self.button.setText("Off")

    @QtCore.Slot()
    def start(self):
        self.token_label.setText("Token")
        if self.button.text() == "Off":
            self.button.setText("Start")
            return self.thread.terminate()
        
        if not token_validate(self.token.text()):
            return self.token_label.setText("Token\n(Token is incorrect!)")
        self.start_thread()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setQuitOnLastWindowClosed(False)

    widget = MainWidget()
    widget.resize(800, 600)

    sys.exit(app.exec())
