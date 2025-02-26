from converter import Converter

class CurrencyConverter(Converter):
    def __init__(self):
        super().__init__()
        self.currency_rates = {
            'UAH': 40,
            'USD': 1,
            'EUR': 0.85
        }

    def convert(self, value, start, result):
        from_rate = self.currency_rates.get(start)
        to_rate = self.currency_rates.get(result)

        if not from_rate or not to_rate:
            return None

        return value * from_rate / to_rate