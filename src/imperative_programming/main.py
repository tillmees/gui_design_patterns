import sys

from PySide6.QtWidgets import QApplication

from app_window import AppWindow


def main():

    app = QApplication(sys.argv)
    app_window = AppWindow()

    with open("src/common/style.qss", "r") as f:
        stylesheet_content = f.read()
        app.setStyleSheet(stylesheet_content)

    app_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
