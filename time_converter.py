from converter import Converter

class TimeConverter(Converter):
    def __init__(self):
        super().__init__()
        self.time_units = {
            'sec': 1,
            'min': 60,
            'hour': 3600
        }

    def convert(self, value, from_val, to_val):
        return value * self.time_units[from_val] / self.time_units[to_val]