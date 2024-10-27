class Wallet:
    payment = "Visa/Mastercard"

    def __init__(self, currency: str, name: str):
        self.balance = 0
        if currency not in ("USD", "EUR", "RUB"):
            raise ValueError("Валюта не поддерживается")
        self.currency = currency
        self.name = name

    def add_balance(self, add: float):
        if add <= 0:
            raise ValueError("Пополнение должно быть положительным")
        self.balance += add
        print(f"Ваш баланс был пополнен на {add} {self.currency}. Текущий баланс: {self.balance}")

    def pay(self, ppay: float):
        if ppay <= 0:
            raise ValueError("Платёж должен быть больше 0")
        self.balance -= ppay
        print(f"Произошла оплата на {ppay} {self.currency}. Текущий баланс: {self.balance} {self.currency}")

    def show_balance(self):
        print(f"Ваш баланс: {self.balance} {self.currency}")

    def delete_balance(self):
        self.balance = 0
        print(f"Счёт {self.name} удалён. Баланс обнулён")


class CryptoWallet(Wallet):
    crypto = {"BTC": 72000, "ETH": 3500}

    def __init__(self, currency: str, name: str, coin: str):
        super().__init__(currency, name)
        if coin not in self.crypto:
            raise ValueError("Криптовалюта не поддерживается")
        self.coin = coin

    def show_balance(self) -> str:
        coin_balance = self.balance / self.crypto[self.coin]
        return f"Баланс в криптовалюте: {coin_balance:.5f} {self.coin}"

    def balance_in_usd(self) -> str:
        usd_balance = self.balance
        return f"Баланс в USD: {usd_balance}"

wallet = Wallet("EUR", "Кошелёк")
wallet.add_balance(2000)
wallet.pay(200)
wallet.show_balance()
wallet.delete_balance()
print("")
crypto = CryptoWallet("USD", "кошелёк", "BTC")
crypto.add_balance(140000)
print(crypto.show_balance())
print(crypto.balance_in_usd())

