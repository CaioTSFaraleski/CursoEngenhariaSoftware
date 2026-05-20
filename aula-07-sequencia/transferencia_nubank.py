"""
Aula 07 - Transferencia Nubank.

Representa a sequencia de chamadas entre cliente, aplicativo, conta e servico
de notificacao durante uma transferencia.
"""

from dataclasses import dataclass


@dataclass
class Conta:
    titular: str
    saldo: float

    def debitar(self, valor: float) -> bool:
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def creditar(self, valor: float) -> None:
        self.saldo += valor


class Notificacao:
    @staticmethod
    def enviar(destinatario: str, mensagem: str) -> None:
        print(f"Notificacao para {destinatario}: {mensagem}")


def transferir(origem: Conta, destino: Conta, valor: float) -> str:
    print(f"Solicitando transferencia de R$ {valor:.2f}")

    if not origem.debitar(valor):
        return "Transferencia recusada: saldo insuficiente ou valor invalido."

    destino.creditar(valor)
    Notificacao.enviar(origem.titular, "Transferencia enviada com sucesso.")
    Notificacao.enviar(destino.titular, "Voce recebeu uma transferencia.")
    return "Transferencia concluida."


def executar_demo() -> None:
    origem = Conta("Caio", 750.00)
    destino = Conta("Fernanda", 120.00)

    print("Transferencia Nubank")
    print(transferir(origem, destino, 250.00))
    print(f"Saldo {origem.titular}: R$ {origem.saldo:.2f}")
    print(f"Saldo {destino.titular}: R$ {destino.saldo:.2f}")


if __name__ == "__main__":
    executar_demo()
