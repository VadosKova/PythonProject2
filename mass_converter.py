from converter import Converter

class MassConverter(Converter):
    def __init__(self):
        super().__init__()
        self.mass_units = {
            'kg': 1,
            'g': 0.001,
            'mg': 0.000001,
            'ton': 1000
        }

    def convert(self, value, from_val, to_val):
        return value * self.mass_units[from_val] / self.mass_units[to_val]