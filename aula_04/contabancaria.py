class contaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para saque.")

class contaBancaria:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero     
        self.__titular = titular  
        self.__saldo = saldo     

    def depositar(self, valor):
        self.__saldo += valor
        print(f" Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f" Saque de R$ {valor:.2f} realizado.")
        else:
            print(" Saldo insuficiente para saque.")

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

if __name__ == "__main__":
    print("Testando Conta Bancária")
    
    minha_conta = contaBancaria("123-4", "João Silva", 1000.0)
    print(f"Titular: {minha_conta.get_titular()}")
    print(f"Saldo Inicial: R$ {minha_conta.get_saldo():.2f}")

    minha_conta.depositar(500.0)
    print(f"Saldo após depósito: R$ {minha_conta.get_saldo():.2f}")

    minha_conta.sacar(200.0)
    print(f"Saldo após saque: R$ {minha_conta.get_saldo():.2f}")

    minha_conta.sacar(2000.0)