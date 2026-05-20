"""
Aula 04 - SRS do FIAP Marketplace.

O programa organiza requisitos em uma estrutura simples inspirada em um
documento SRS, com identificador, prioridade, tipo e criterio de aceite.
"""

from dataclasses import dataclass


@dataclass
class Requisito:
    codigo: str
    titulo: str
    tipo: str
    prioridade: str
    criterio_aceite: str


def listar_requisitos(requisitos: list[Requisito]) -> None:
    print("SRS - FIAP Marketplace")
    print("=" * 24)

    for requisito in requisitos:
        print(f"{requisito.codigo} | {requisito.tipo} | {requisito.prioridade}")
        print(f"Titulo: {requisito.titulo}")
        print(f"Criterio de aceite: {requisito.criterio_aceite}")
        print("-" * 60)


def filtrar_por_tipo(requisitos: list[Requisito], tipo: str) -> list[Requisito]:
    return [item for item in requisitos if item.tipo.lower() == tipo.lower()]


def executar_demo() -> None:
    requisitos = [
        Requisito(
            "RF-001",
            "Cadastrar produto academico",
            "Funcional",
            "Alta",
            "Dado um vendedor autenticado, quando cadastrar dados validos, entao o produto fica disponivel para revisao.",
        ),
        Requisito(
            "RF-002",
            "Pesquisar produtos por categoria",
            "Funcional",
            "Media",
            "Dado um visitante, quando escolher uma categoria, entao o sistema lista os produtos correspondentes.",
        ),
        Requisito(
            "RNF-001",
            "Tempo de resposta da busca",
            "Nao funcional",
            "Alta",
            "As buscas devem responder em ate 2 segundos para ate 500 produtos cadastrados.",
        ),
    ]

    listar_requisitos(requisitos)
    funcionais = filtrar_por_tipo(requisitos, "Funcional")
    print(f"Total de requisitos funcionais: {len(funcionais)}")


if __name__ == "__main__":
    executar_demo()
