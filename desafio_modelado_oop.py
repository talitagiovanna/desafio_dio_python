from datetime import date

class Transacao:
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar(self, conta: 'Conta') -> None:
        raise NotImplementedError("Método deve ser implementado pelas subclasses")

class Deposito(Transacao):
    def registrar(self, conta: 'Conta') -> None:
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)
        print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso!")

class Saque(Transacao):
    def registrar(self, conta: 'Conta') -> None:
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao: Transacao) -> None:
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente: 'Cliente', numero: int, agencia: str):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        cliente.adicionar_conta(self)
    
    def saldo(self) -> float:
        return self.saldo
    
    @staticmethod
    def nova_conta(cliente: 'Cliente', numero: int, agencia: str) -> 'Conta':
        return Conta(cliente, numero, agencia)
    
    def sacar(self, valor: float) -> bool:
        saque = Saque(valor)
        if saque.registrar(self):
            return True
        return False
    
    def depositar(self, valor: float) -> bool:
        deposito = Deposito(valor)
        deposito.registrar(self)
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente: 'Cliente', numero: int, agencia: str, limite: float, limite_saques: int):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0
    
    def sacar(self, valor: float) -> bool:
        if self.saques_realizados < self.limite_saques and self.saldo + self.limite >= valor:
            saque = Saque(valor)
            if saque.registrar(self):
                self.saques_realizados += 1
                return True
        print("Saque não autorizado.")
        return False

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta: Conta) -> None:
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Exemplo de uso
def main():
    cliente = PessoaFisica("Rua das Flores, 123", "123.456.789-00", "João Silva", date(1985, 5, 20))
    conta_corrente = ContaCorrente(cliente, 1234, "0001", 1000.0, 3)
    
    conta_corrente.depositar(1500)
    conta_corrente.sacar(300)
    conta_corrente.sacar(700)
    conta_corrente.sacar(600)  # Este saque deve falhar. 

    print("\nExtrato da conta:")
    for transacao in conta_corrente.historico.transacoes:
        tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
        print(f"{tipo} de R$ {transacao.valor:.2f}")

if __name__ == "__main__":
    main()
