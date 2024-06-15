import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MyForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a button
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_click)

        # Create a label
        self.label = QLabel('Hello, PyQt5!', self)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout on the application's window
        self.setLayout(layout)

        # Set window title and size
        self.setWindowTitle('My First PyQt5 App')
        self.setGeometry(100, 100, 300, 200)

    def on_click(self):
        self.label.setText('Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())