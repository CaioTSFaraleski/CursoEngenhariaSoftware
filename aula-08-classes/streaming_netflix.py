"""
Aula 08 - Sistema de Streaming.

Implementa classes para usuario, conteudo e plataforma, alinhadas ao diagrama
de classes do exercicio.
"""

from dataclasses import dataclass, field


@dataclass
class Conteudo:
    titulo: str
    genero: str
    duracao_minutos: int
    classificacao: int


@dataclass
class Usuario:
    nome: str
    idade: int
    favoritos: list[str] = field(default_factory=list)

    def pode_assistir(self, conteudo: Conteudo) -> bool:
        return self.idade >= conteudo.classificacao


class PlataformaStreaming:
    def __init__(self) -> None:
        self.catalogo: dict[str, Conteudo] = {}

    def adicionar_conteudo(self, conteudo: Conteudo) -> None:
        self.catalogo[conteudo.titulo] = conteudo

    def recomendar_por_genero(self, genero: str) -> list[Conteudo]:
        return [
            conteudo
            for conteudo in self.catalogo.values()
            if conteudo.genero.lower() == genero.lower()
        ]

    def assistir(self, usuario: Usuario, titulo: str) -> str:
        conteudo = self.catalogo.get(titulo)
        if conteudo is None:
            return "Conteudo nao encontrado."
        if not usuario.pode_assistir(conteudo):
            return "Conteudo bloqueado pela classificacao indicativa."

        usuario.favoritos.append(titulo)
        return f"{usuario.nome} esta assistindo {titulo}."


def executar_demo() -> None:
    plataforma = PlataformaStreaming()
    plataforma.adicionar_conteudo(Conteudo("Stranger Things", "Ficcao", 50, 14))
    plataforma.adicionar_conteudo(Conteudo("Planeta Terra", "Documentario", 45, 0))

    usuario = Usuario("Rafael", 16)

    print("Sistema de Streaming")
    print(plataforma.assistir(usuario, "Stranger Things"))
    print("Recomendacoes de Ficcao:")
    for item in plataforma.recomendar_por_genero("Ficcao"):
        print(f"- {item.titulo} ({item.duracao_minutos} min)")


if __name__ == "__main__":
    executar_demo()
