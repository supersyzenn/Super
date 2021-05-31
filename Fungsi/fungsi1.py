# fungsi biasa

class rekening:
    def __init__(self, saldo):
        self.saldo = saldo

    def nabung(self, uang):
        self.uang = uang
        self.saldo += uang


ahmad = rekening(1000)
print(ahmad.saldo)
ahmad.nabung(5000)
print(ahmad.saldo)

zen = rekening(2000)
print(zen.saldo)
