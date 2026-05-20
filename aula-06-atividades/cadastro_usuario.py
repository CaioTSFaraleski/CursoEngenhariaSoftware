"""
Aula 06 - Cadastro e aprovacao de usuario.

Simula o fluxo de atividades com validacao dos dados, analise do moderador
e notificacao final ao usuario.
"""

from dataclasses import dataclass


@dataclass
class Cadastro:
    nome: str
    email: str
    idade: int
    documentos_enviados: bool


def validar_dados(cadastro: Cadastro) -> list[str]:
    erros = []

    if len(cadastro.nome.strip()) < 3:
        erros.append("Nome deve ter pelo menos 3 caracteres.")
    if "@" not in cadastro.email or "." not in cadastro.email:
        erros.append("E-mail invalido.")
    if cadastro.idade < 18:
        erros.append("Usuario deve ser maior de idade.")
    if not cadastro.documentos_enviados:
        erros.append("Documentos obrigatorios nao enviados.")

    return erros


def analisar_cadastro(cadastro: Cadastro) -> str:
    erros = validar_dados(cadastro)

    if erros:
        return "Cadastro reprovado: " + "; ".join(erros)

    return "Cadastro aprovado: usuario liberado para acessar a plataforma."


def executar_demo() -> None:
    cadastros = [
        Cadastro("Lucas Pereira", "lucas@email.com", 22, True),
        Cadastro("Bia", "bia-email.com", 17, False),
    ]

    print("Fluxo de Cadastro de Usuario")
    print("-" * 32)

    for cadastro in cadastros:
        print(f"Solicitante: {cadastro.nome}")
        print(analisar_cadastro(cadastro))
        print()


if __name__ == "__main__":
    executar_demo()
