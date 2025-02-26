from converter import Converter

class LengthConverter(Converter):
    def __init__(self):
        super().__init__()
        self.length_units = {
            'm': 1,
            'km': 1000,
            'cm': 0.01,
            'mm': 0.001,
            'mile': 1609.34
        }

    def convert(self, value, from_val, to_val):
        return value * self.length_units[from_val] / self.length_units[to_val]