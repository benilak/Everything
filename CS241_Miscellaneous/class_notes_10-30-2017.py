class Money:
    def __init__(self):
        self._dollars = 0
        self._cents = 0

    def display(self):
        print("${}.{}".format(self._dollars, self._cents))

    def get_dollars(self):
        return self._dollars

    def get_cents(self):
        return self._cents

    def set_dollars(self, dollars):
        self._dollars = dollars

    def set_cents(self, cents):
        if cents >= 100:
            self._dollars += 1
            self._cents = cents - 100
        self._cents = cents


wallet = Money()
wallet.set_dollars = 20
wallet.set_cents = 199


wallet.display()