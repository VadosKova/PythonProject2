from length_converter import LengthConverter
from mass_converter import MassConverter
from time_converter import TimeConverter
from temp_converter import TemperatureConverter
from currency_converter import CurrencyConverter

while True:
    print("Choose conversion type:")
    print("1. Length")
    print("2. Mass")
    print("3. Time")
    print("4. Temperature")
    print("5. Currency")
    print("6. Exit")

    type = input("Enter choice: ")

    if type == "1":
        units = ['m', 'km', 'cm', 'mm', 'mile']
        converter = LengthConverter()
    elif type == "2":
        units = ['kg', 'g', 'mg', 'ton']
        converter = MassConverter()
    elif type == "3":
        units = ['sec', 'min', 'hour']
        converter = TimeConverter()
    elif type == "4":
        units = ['C', 'F']
        converter = TemperatureConverter()
    elif type == "5":
        units = ['UAH', 'USD', 'EUR']
        converter = CurrencyConverter()
    elif type == "6":
        print("Goodbye")
        break
    else:
        print("Error")
        continue

    from_val = input(f"Enter start unit ({', '.join(units)}): ")
    if from_val not in units:
        print("Error")
        continue

    to_val = input(f"Enter finale unit ({', '.join(units)}): ")
    if to_val not in units:
        print("Error")
        continue

    value = float(input(f"Enter value {from_val}: "))
    result = converter.convert(value, from_val, to_val)

    if result is None:
        print("Error")
    else:
        print(f"{value} {from_val} = {result} {to_val}")