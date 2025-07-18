from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class SavedDataWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        serial_obj = self.get_serial_obj()
        info = f"serial_obj: {serial_obj}"
        layout.addWidget(QLabel("Saved Data"))
        layout.addWidget(QLabel(info))
        self.setLayout(layout)

    def get_serial_obj(self):
        return self.main_window.serial_obj
