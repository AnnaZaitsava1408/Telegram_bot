import requests
import json
from bot_config import keys
class ConvertionException(Exception):
    pass

class APIException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if int(amount) <= 0 or float(amount) <=0:
            raise APIException('Неверный ввод количества валюты')
        base = base.lower()
        quote = quote.lower()
        try:
            keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        quote_ticker, base_ticker = keys[quote], keys[base]

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        print(total_base, type(total_base))
        total_base = total_base * float(amount)

        return total_base



