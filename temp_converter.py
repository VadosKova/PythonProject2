from converter import Converter

class TemperatureConverter(Converter):
    def __init__(self):
        super().__init__()

    def convert(self, value, from_val, to_val):
        if from_val == "C" and to_val == "F":
            return (value * 9/5) + 32
        elif from_val == "F" and to_val == "C":
            return (value - 32) * 5/9
        else:
            return "Error"