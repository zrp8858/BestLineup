import tkinter as tk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MVC Example")

        self.label = tk.Label(self, text="")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Update")
        self.button.pack(pady=10)

    def set_label_text(self, text):
        self.label.config(text=text)

    def get_entry_text(self):
        return self.entry.get()

    def set_button_command(self, command):
        self.button.config(command=command)
