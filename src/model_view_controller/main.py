import sys

from PySide6.QtWidgets import QApplication

from app_controller import AppController
from app_model import AppModel
from app_view import AppView


def main():

    app = QApplication(sys.argv)
    app_view = AppView()
    app_model = AppModel()
    app_controller = AppController(app_model, app_view)

    app_controller.on_start()

    with open("src/common/style.qss", "r") as f:
        stylesheet_content = f.read()
        app.setStyleSheet(stylesheet_content)

    app_view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
