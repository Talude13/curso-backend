class ContaBancaria:
    def __init__(self, titular):
        """
        Inicializa uma nova conta bancária.

        Args:
            titular (str): O nome do titular da conta.
        """
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        """
        Adiciona um valor ao saldo da conta.

        Args:
            valor (float): O valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """
        Subtrai um valor do saldo da conta se houver saldo suficiente.

        Args:
            valor (float): O valor a ser sacado.
        """
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de {valor:.2f} realizado com sucesso.")
            else:
                print("Erro: Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def __str__(self):
        """
        Retorna uma representação em string da conta bancária.
        """
        return f"Conta do titular: {self.titular}, Saldo: {self.saldo:.2f}"

# Exemplo de uso:
minha_conta = ContaBancaria("Marcos")
print(minha_conta)

minha_conta.depositar(500)
print(minha_conta)

minha_conta.sacar(200)
print(minha_conta)

minha_conta.sacar(400) # Tentativa de saque com saldo insuficiente
print(minha_conta)