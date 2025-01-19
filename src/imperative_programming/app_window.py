import random

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QPlainTextEdit,
    QMainWindow,
    QSizePolicy,
    QSpacerItem,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSlider,
    QListWidget,
)


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            QCoreApplication.translate(
                "AppWindow", "Imperative Programming Example", None
            )
        )
        self.resize(1000, 600)

        self.central_widget, self.central_widget_layout = self.create_widget(
            parent=self,
            widget_cls=QWidget,
            layout_cls=QGridLayout,
            object_name="central_widget",
        )
        self.central_widget_layout.setSpacing(20)
        self.setCentralWidget(self.central_widget)

        self.create_color_change_button()
        self.create_slider()
        self.create_text_edit()
        self.create_moving_buttons()
        self.create_element_list()

        self.connect_actions()

    def connect_actions(self):
        # button color
        self.change_color_button.clicked.connect(self.on_change_color_button_clicked)

        # slider
        self.slider.valueChanged.connect(self.on_slider_moved)

        # text edit
        self.text_input.textChanged.connect(self.on_text_changed)

        # moving buttons
        self.left_button.clicked.connect(self.left_button_clicked)
        self.right_button.clicked.connect(self.right_button_clicked)

        # element list
        self.element_add_button.clicked.connect(self.on_add_element_button_clicked)
        self.element_delete_button.clicked.connect(
            self.on_delete_element_button_clicked
        )
        self.element_clear_button.clicked.connect(self.on_clear_element_button_clicked)

    def create_color_change_button(self):
        self.change_color_widget, self.change_color_widget_layout = self.create_widget(
            parent=self,
            widget_cls=QWidget,
            layout_cls=QHBoxLayout,
            object_name="change_color_widget",
        )
        self.change_color_button = QPushButton("Change Button Color")
        self.change_color_button.setFixedSize(200, 40)
        self.change_color_button.setCursor(Qt.PointingHandCursor)
        self.change_color_button.setObjectName("change_color_button")
        self.change_color_widget_layout.addWidget(self.change_color_button)
        self.change_color_button.setStyleSheet("background-color: white; color: black;")

        self.central_widget_layout.addWidget(
            self.change_color_widget, 0, 0, 1, 1, alignment=Qt.AlignCenter
        )

    def create_slider(self):
        self.silder_widget, self.slider_widget_layout = self.create_widget(
            parent=self,
            widget_cls=QWidget,
            layout_cls=QHBoxLayout,
            object_name="slider_widget",
        )
        self.slider_widget_layout.setSpacing(20)

        self.slider = QSlider(orientation=Qt.Horizontal)
        self.slider.setFixedSize(200, 20)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_widget_layout.addWidget(self.slider)

        self.slider_label = QLabel(f"{self.slider.value()}")
        self.slider_label.setFixedSize(40, 20)
        self.slider_label.setAlignment(Qt.AlignCenter)
        self.slider_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.slider_label.setObjectName("slider_label")
        self.slider_widget_layout.addWidget(self.slider_label)

        self.central_widget_layout.addWidget(
            self.silder_widget, 0, 1, 1, 1, alignment=Qt.AlignCenter
        )

    def create_text_edit(self):
        self.text_edit_widget, self.text_edit_widget_layout = self.create_widget(
            parent=self,
            widget_cls=QWidget,
            layout_cls=QVBoxLayout,
            object_name="text_edit_widget",
        )
        self.text_edit_widget_layout.setSpacing(20)

        self.text_input = QPlainTextEdit()
        self.text_input.setPlainText("Hello World")
        self.text_input.setFixedSize(200, 100)
        self.text_input.setObjectName("text_input")
        self.text_edit_widget_layout.addWidget(self.text_input)

        self.text_output = QPlainTextEdit()
        self.text_output.setReadOnly(True)
        self.text_output.setPlainText(f"{self.text_input.toPlainText()}"[::-1])
        self.text_output.setFixedSize(200, 100)
        self.text_output.setObjectName("text_output")
        self.text_edit_widget_layout.addWidget(self.text_output)

        self.central_widget_layout.addWidget(
            self.text_edit_widget, 1, 0, 1, 1, alignment=Qt.AlignCenter
        )

    def create_moving_buttons(self):
        self.button_moving_widget, self.button_moving_widget_layout = (
            self.create_widget(
                parent=self,
                widget_cls=QWidget,
                layout_cls=QHBoxLayout,
                object_name="button_moving_widget",
            )
        )
        self.left_button = QPushButton(">>>")
        self.left_button.setFixedSize(40, 40)
        self.left_button.setCursor(Qt.PointingHandCursor)
        self.left_button.setObjectName("left_button")
        self.button_moving_widget_layout.addWidget(self.left_button)

        self.button_moving_spacer = QSpacerItem(
            100, 20, QSizePolicy.Fixed, QSizePolicy.Fixed
        )
        self.button_moving_widget_layout.addItem(self.button_moving_spacer)

        self.right_button = QPushButton("<<<")
        self.right_button.setFixedSize(40, 40)
        self.right_button.setCursor(Qt.PointingHandCursor)
        self.right_button.setObjectName("right_button")
        self.button_moving_widget_layout.addWidget(self.right_button)

        # set initial state
        self.right_button.hide()

        self.central_widget_layout.addWidget(
            self.button_moving_widget, 1, 1, 1, 1, alignment=Qt.AlignCenter
        )

    def create_element_list(self):
        self.element_list_widget, self.element_list_widget_layout = self.create_widget(
            parent=self,
            widget_cls=QWidget,
            layout_cls=QHBoxLayout,
            object_name="element_list_widget",
        )

        # element interface
        self.element_config_widget, self.element_config_widget_layout = (
            self.create_widget(
                parent=self,
                widget_cls=QWidget,
                layout_cls=QVBoxLayout,
                object_name="element_config_widget",
            )
        )
        self.element_config_widget_layout.setAlignment(Qt.AlignTop)
        self.element_config_widget_layout.setSpacing(5)
        self.element_list_widget_layout.addWidget(self.element_config_widget)

        # element text
        self.element_text = QPlainTextEdit()
        self.element_text.setPlainText("Type Here")
        self.element_text.setFixedSize(200, 40)
        self.element_text.setObjectName("element_text")
        self.element_config_widget_layout.addWidget(self.element_text)

        # add button
        self.element_add_button = QPushButton("Add")
        self.element_add_button.setFixedSize(200, 40)
        self.element_add_button.setCursor(Qt.PointingHandCursor)
        self.element_add_button.setObjectName("element_add_button")
        self.element_config_widget_layout.addWidget(self.element_add_button)

        # delete button
        self.element_delete_button = QPushButton("Delete")
        self.element_delete_button.setFixedSize(200, 40)
        self.element_delete_button.setCursor(Qt.PointingHandCursor)
        self.element_delete_button.setObjectName("element_delete_button")
        self.element_config_widget_layout.addWidget(self.element_delete_button)

        # clear button
        self.element_clear_button = QPushButton("Clear")
        self.element_clear_button.setFixedSize(200, 40)
        self.element_clear_button.setCursor(Qt.PointingHandCursor)
        self.element_clear_button.setObjectName("element_clear_button")
        self.element_config_widget_layout.addWidget(self.element_clear_button)

        # list
        self.list_widget = QListWidget()
        self.list_widget.setFixedSize(200, 175)
        self.list_widget.setObjectName("list_widget")
        self.element_list_widget_layout.addWidget(self.list_widget)

        self.central_widget_layout.addWidget(
            self.element_list_widget, 2, 0, 1, 2, alignment=Qt.AlignCenter
        )

    def on_change_color_button_clicked(self):
        random_color = QColor(
            random.randint(0, 255),  # Red
            random.randint(0, 255),  # Green
            random.randint(0, 255),  # Blue
        )
        self.change_color_button.setStyleSheet(
            f"background-color: {random_color.name()};" f"color: black;"
        )

    def on_slider_moved(self, value):
        self.slider_label.setText(f"{self.slider.value()}")

    def on_text_changed(self):
        text = self.text_input.toPlainText()
        self.text_output.setPlainText(text[::-1])

    def left_button_clicked(self):
        self.right_button.show()
        self.left_button.hide()

    def right_button_clicked(self):
        self.right_button.hide()
        self.left_button.show()

    def on_add_element_button_clicked(self):
        self.list_widget.addItem(self.element_text.toPlainText())

    def on_delete_element_button_clicked(self):
        self.list_widget.takeItem(self.list_widget.currentRow())

    def on_clear_element_button_clicked(self):
        self.list_widget.clear()

    def create_widget(self, parent, widget_cls, layout_cls, object_name):
        widget = widget_cls(parent)
        widget.setObjectName(object_name)
        layout = layout_cls(widget)
        layout.setObjectName(f"{object_name}Layout")
        return widget, layout
