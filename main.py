
from PySide6.QtWidgets import QApplication
import sys
from interact import ControlUiWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlUiWidget()
    window.show()
    sys.exit(app.exec())