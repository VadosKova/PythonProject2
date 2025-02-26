from tkinter import *
from length_converter import LengthConverter
from mass_converter import MassConverter
from time_converter import TimeConverter
from temp_converter import TemperatureConverter
from currency_converter import CurrencyConverter

class Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("Converter")
        self.root.geometry("400x300")

        self.length_converter = LengthConverter()
        self.mass_converter = MassConverter()
        self.time_converter = TimeConverter()
        self.temp_converter = TemperatureConverter()
        self.currency_converter = CurrencyConverter()

        self.type = StringVar()

        self.tools()
