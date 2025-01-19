class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.connect_actions()

    def on_start(self):
        self.view.update_button_color(self.model.button_color)
        self.view.set_slider(self.model.slider_value)
        self.view.update_slider_value(self.model.slider_value)
        self.view.set_text_input(self.model.text_content)
        self.view.update_text_output(self.model.text_content)
        self.view.update_element_list(self.model.element_list)

    def connect_actions(self):
        # button color
        self.view.change_color_button.clicked.connect(
            self.on_change_color_button_clicked
        )

        # slider
        self.view.slider.valueChanged.connect(self.on_slider_moved)

        # # text edit
        self.view.text_input.textChanged.connect(self.on_text_changed)

        # # moving buttons
        self.view.left_button.clicked.connect(self.move_button_clicked)
        self.view.right_button.clicked.connect(self.move_button_clicked)

        # # element list
        self.view.element_add_button.clicked.connect(self.on_add_element_button_clicked)
        self.view.element_delete_button.clicked.connect(
            self.on_delete_element_button_clicked
        )
        self.view.element_clear_button.clicked.connect(
            self.on_clear_element_button_clicked
        )

    def on_change_color_button_clicked(self):
        self.model.change_button_color_randomly()
        self.view.update_button_color(self.model.button_color)

    def on_slider_moved(self):
        self.model.set_slider_value(self.view.slider.value())
        self.view.update_slider_value(self.model.slider_value)

    def on_text_changed(self):
        self.model.set_text_content(self.view.text_input.toPlainText())
        self.view.update_text_output(self.model.text_content)

    def move_button_clicked(self):
        self.model.toggle_button_visibilities()
        self.view.update_button_visibilities(
            self.model.is_left_button_visible, self.model.is_right_button_visible
        )

    def on_add_element_button_clicked(self):
        self.model.add_element(self.view.element_text.toPlainText())
        self.view.update_element_list(self.model.element_list)

    def on_delete_element_button_clicked(self):
        current_index = self.view.list_widget.currentRow()
        if current_index >= 0:
            self.model.delete_element(current_index)
            self.view.update_element_list(self.model.element_list)
        else:
            pass

    def on_clear_element_button_clicked(self):
        self.model.clear_elements()
        self.view.update_element_list(self.model.element_list)
