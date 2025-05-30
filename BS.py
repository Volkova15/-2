import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        url = "https://www.deutsche-bank.de/pfb/content/pk-kurse-und-rechner/wechselkurse.html"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            usd_row = soup.find("td", text="978").find_parent("tr")
            exchange_rate = float(usd_row.find_all("td")[4].text.replace(",", "."))
            return exchange_rate
        else:
            raise Exception("Не вдалося отримати курс валют!")

    def eur_to_usd(self, eur_amount):
        return eur_amount / self.exchange_rate

if __name__ == "__main__":
    converter = CurrencyConverter()

    print(f"Курс USD/EUR: {converter.exchange_rate}")

    try:
        uah_amount = float(input("Введіть кількість евро: "))
        usd_amount = converter.eur_to_usd(eur_amount)
        print(f"{eur_amount} евро = {usd_amount:.2f} доларів США")
    except ValueError:
        print("Будь ласка, введіть коректне числове значення.")
