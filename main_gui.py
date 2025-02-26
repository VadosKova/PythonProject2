from tkinter import *
from tkinter import ttk
from length_converter import LengthConverter
from mass_converter import MassConverter
from time_converter import TimeConverter
from temp_converter import TemperatureConverter
from currency_converter import CurrencyConverter

class Conversion:
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

        self.type_combo = ttk.Combobox(self.root, textvariable=self.type, values=["Length", "Mass", "Time", "Temperature", "Currency"])
        self.type_combo.grid(row=0, column=1, padx=10, pady=10)
        self.type_combo.bind("<<ComboboxSelected>>", self.selected_units)

        self.value = Label(self.root, text="Enter Value:")
        self.value.grid(row=1, column=0, padx=10, pady=10)

        self.value_entry = Entry(self.root)
        self.value_entry.grid(row=1, column=1, padx=10, pady=10)

        self.result = Label(self.root, text="Result:")
        self.result.grid(row=2, column=0, padx=10, pady=10)

        self.show_res = Label(self.root, text="")
        self.show_res.grid(row=2, column=1, padx=10, pady=10)

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

    def selected_units(self, event=None):
        type = self.type.get()
        if type == "Length":
            units = ['m', 'km', 'cm', 'mm', 'mile']
            self.update_combo_options(units)
            self.converter = self.length_converter
        elif type == "Mass":
            units = ['kg', 'g', 'mg', 'ton']
            self.update_combo_options(units)
            self.converter = self.mass_converter
        elif type == "Time":
            units = ['sec', 'min', 'hour']
            self.update_combo_options(units)
            self.converter = self.time_converter
        elif type == "Temperature":
            units = ['C', 'F']
            self.update_combo_options(units)
            self.converter = self.temp_converter
        elif type == "Currency":
            units = ['UAH', 'USD', 'EUR']
            self.update_combo_options(units)
            self.converter = self.currency_converter
        else:
            units = []
            self.update_combo_options(units)

    def update_combo_options(self, units):
        self.from_combo['values'] = units
        self.to_combo['values'] = units
        self.from_combo.set('')
        self.to_combo.set('')

    def show_conversion(self):
        try:
            value = float(self.value_entry.get())
            from_val = self.from_combo.get()
            to_val = self.to_combo.get()

            if from_val and to_val:
                result = self.converter.convert(value, from_val, to_val)
                if result is not None:
                    self.show_res.config(text=f"{result} {to_val}")
                else:
                    self.show_res.config(text="Error")
        except ValueError:
            self.show_res.config(text="Error")


root = Tk()
app = Conversion(root)
root.mainloop()