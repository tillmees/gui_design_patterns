import random

from PySide6.QtGui import QColor


class AppModel:
    def __init__(self):
        self.button_color = "white"
        self.slider_value = 50
        self.text_content = "Hello World"
        self.is_left_button_visible = True
        self.is_right_button_visible = not self.is_left_button_visible
        self.element_list = []

    def change_button_color_randomly(self):
        random_color = QColor(
            random.randint(0, 255),  # Red
            random.randint(0, 255),  # Green
            random.randint(0, 255),  # Blue
        )
        self.button_color = random_color.name()

    def set_slider_value(self, value):
        self.slider_value = value

    def set_text_content(self, text):
        self.text_content = text[::-1]

    def toggle_button_visibilities(self):
        self.is_left_button_visible = not self.is_left_button_visible
        self.is_right_button_visible = not self.is_right_button_visible

    def add_element(self, text):
        self.element_list.append(text)

    def delete_element(self, index):
        self.element_list.pop(index)

    def clear_elements(self):
        self.element_list = []
