class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Initialize View with model data
        self.view.set_label_text(self.model.get_data())
        # Bind button to handler
        self.view.set_button_command(self.update_model)

    def update_model(self):
        new_data = self.view.get_entry_text()
        self.model.set_data(new_data)
        self.view.set_label_text(self.model.get_data())
