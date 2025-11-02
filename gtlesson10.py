import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, rate_usd_to_kzt):
        self.rate_usd_to_kzt = rate_usd_to_kzt

    def kzt_to_usd(self, amount_kzt):
        return amount_kzt / self.rate_usd_to_kzt

def get_usd_kzt_rate():
    url = "https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut"
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    row = soup.find("td", string="1 ДОЛЛАР США, USD / KZT,")

    if not row:
        raise RuntimeError("Не удалось найти курс USD")
    
    rate_td = row.find_next_sibling("td")
    rate = rate_td.text.strip().replace("\u202f", "").replace(",", ".")
    return float(rate)

if __name__ == "__main__":
    try:
        rate = get_usd_kzt_rate()
    except Exception as e:
        print("Ошииибка при получении крса:", e)
        rate = 538.89

    converter = CurrencyConverter(rate)

    user_input = input("Выедите сумму в тенге (KZT): ")
    try:
        amount_kzt = float(user_input)
    except ValueError:
        print("Неверное число")
        exit(1)

    amount_usd = converter.kzt_to_usd(amount_kzt)
    print(f"{amount_kzt:.2f} KZT = {amount_usd:.2f} USD (курс {rate:.2f} KZT за 1USD)")

