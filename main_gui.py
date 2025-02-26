from tkinter import *
from tkinter import ttk
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

    def tools(self):
        self.type_label = Label(self.root, text="Choose conversion type:")
        self.type_label.grid(row=0, column=0, padx=10, pady=10)

        self.type_combo = ttk.Combobox(self.root, textvariable=self.conversion_type, values=["Length", "Mass", "Time", "Temperature", "Currency"])
        self.type_combo.grid(row=0, column=1, padx=10, pady=10)
        self.type_combo.bind("<<ComboboxSelected>>", self.selected_units)

        self.value = Label(self.root, text="Enter Value:")
        self.value.grid(row=1, column=0, padx=10, pady=10)

        self.value_entry = Entry(self.root)
        self.value_entry.grid(row=1, column=1, padx=10, pady=10)

        self.result = Label(self.root, text="Result:")
        self.result.grid(row=2, column=0, padx=10, pady=10)

        self.result_value = Label(self.root, text="")
        self.result_value.grid(row=2, column=1, padx=10, pady=10)

        self.from_label = Label(self.root, text="From:")
        self.from_label.grid(row=3, column=0, padx=10, pady=10)

        self.from_combo = ttk.Combobox(self.root)
        self.from_combo.grid(row=3, column=1, padx=10, pady=10)

        self.to_label = Label(self.root, text="To:")
        self.to_label.grid(row=4, column=0, padx=10, pady=10)

        self.to_combo = ttk.Combobox(self.root)
        self.to_combo.grid(row=4, column=1, padx=10, pady=10)

        self.convert_btn = Button(self.root, text="Convert", command=self.show_conversion)
        self.convert_btn.grid(row=5, column=0, columnspan=2, pady=10)