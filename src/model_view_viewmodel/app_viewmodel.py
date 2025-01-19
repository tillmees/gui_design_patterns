from PySide6.QtCore import QObject, Signal


class AppViewModel(QObject):
    button_color_changed = Signal(str)
    slider_set = Signal(int)
    slider_moved = Signal(int)
    text_input_set = Signal(str)
    text_changed = Signal(str)
    button_visibility_changed = Signal(bool, bool)
    element_list_changed = Signal(list)

    def __init__(self, model):
        super().__init__()
        self.model = model

    def on_start(self):
        self.button_color_changed.emit(self.model.button_color)
        self.slider_set.emit(self.model.slider_value)
        self.slider_moved.emit(self.model.slider_value)
        self.text_input_set.emit(self.model.text_content)
        self.text_changed.emit(self.model.text_content)
        self.element_list_changed.emit(self.model.element_list)

    def on_change_color_button_clicked(self):
        self.model.change_button_color_randomly()
        self.button_color_changed.emit(self.model.button_color)

    def on_slider_moved(self, value):
        self.model.set_slider_value(value)
        self.slider_moved.emit(self.model.slider_value)

    def on_text_changed(self, text):
        self.model.set_text_content(text)
        self.text_changed.emit(self.model.text_content)

    def move_button_clicked(self):
        self.model.toggle_button_visibilities()
        self.button_visibility_changed.emit(
            self.model.is_left_button_visible, self.model.is_right_button_visible
        )

    def on_add_element_button_clicked(self, text):
        self.model.add_element(text)
        self.element_list_changed.emit(self.model.element_list)

    def on_delete_element_button_clicked(self, index):
        if index >= 0:
            self.model.delete_element(index)
            self.element_list_changed.emit(self.model.element_list)
        else:
            pass

    def on_clear_element_button_clicked(self):
        self.model.clear_elements()
        self.element_list_changed.emit(self.model.element_list)
