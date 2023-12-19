from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Calculate miles to km"""
        result = float(self.get_valid_miles()) * MILES_TO_KM
        self.root.ids.output_number.text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        value = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Get text input from text entry widget, convert to float."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
