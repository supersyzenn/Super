# fungsi private

class rekening:
    def __init__(self, saldo, nama):
        self.__saldo = saldo
        self.nama = nama

    def nabung(self, uang):
        self.uang = uang
        self.__saldo += uang

    def tarik(self, jmlTarik):
        self.jmlTarik = jmlTarik
        self.__saldo -= jmlTarik

    def printSaldo(self):
        return("Saldo "+self.nama+" sebesar "+str(self.__saldo))

    def printSaldoo(self):
        return("Saldo "+self.nama+" setelah nabung "+str(self.__saldo))

    def printSaldooo(self):
        return("Saldo "+self.nama+" setelah ditarik "+str(self.__saldo))


user = rekening(5000, "syzen")
print(user.printSaldo())
user.nabung(5000)
print(user.printSaldoo())
user.tarik(2000)
print(user.printSaldooo())
user.nama = "supersyzen"
print(user.printSaldo())
