import sys

from PySide6.QtWidgets import QApplication

from app_viewmodel import AppViewModel
from app_model import AppModel
from app_view import AppView


def main():

    app = QApplication(sys.argv)
    app_model = AppModel()
    app_view_model = AppViewModel(app_model)
    app_view = AppView()
    app_view.bind(app_view_model)

    app_view_model.on_start()

    with open("src/common/style.qss", "r") as f:
        stylesheet_content = f.read()
        app.setStyleSheet(stylesheet_content)

    app_view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
