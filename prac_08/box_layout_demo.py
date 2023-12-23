from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box layout demo app system."""
    def build(self):
        """Build Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handler for pressing the greet button."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def press_clear(self):
        """Clear any buttons that have been selected (visually) and reset status text."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
