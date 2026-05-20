"""
Aula 05 - Biblioteca Digital.

Implementa os principais casos de uso do sistema: cadastrar usuario,
cadastrar livro, emprestar e devolver exemplar.
"""

from dataclasses import dataclass, field


@dataclass
class Livro:
    titulo: str
    autor: str
    disponivel: bool = True


@dataclass
class Usuario:
    nome: str
    emprestimos: list[str] = field(default_factory=list)


class BibliotecaDigital:
    def __init__(self) -> None:
        self.livros: dict[str, Livro] = {}
        self.usuarios: dict[str, Usuario] = {}

    def cadastrar_usuario(self, nome: str) -> None:
        self.usuarios[nome] = Usuario(nome)

    def cadastrar_livro(self, titulo: str, autor: str) -> None:
        self.livros[titulo] = Livro(titulo, autor)

    def emprestar_livro(self, nome: str, titulo: str) -> str:
        if nome not in self.usuarios:
            return "Usuario nao encontrado."
        if titulo not in self.livros:
            return "Livro nao encontrado."
        if not self.livros[titulo].disponivel:
            return "Livro indisponivel para emprestimo."

        self.livros[titulo].disponivel = False
        self.usuarios[nome].emprestimos.append(titulo)
        return "Emprestimo realizado com sucesso."

    def devolver_livro(self, nome: str, titulo: str) -> str:
        if nome not in self.usuarios or titulo not in self.usuarios[nome].emprestimos:
            return "Emprestimo nao localizado."

        self.usuarios[nome].emprestimos.remove(titulo)
        self.livros[titulo].disponivel = True
        return "Devolucao registrada com sucesso."


def executar_demo() -> None:
    biblioteca = BibliotecaDigital()
    biblioteca.cadastrar_usuario("Marina")
    biblioteca.cadastrar_livro("Engenharia de Software", "Ian Sommerville")

    print("Biblioteca Digital")
    print(biblioteca.emprestar_livro("Marina", "Engenharia de Software"))
    print(biblioteca.emprestar_livro("Marina", "Engenharia de Software"))
    print(biblioteca.devolver_livro("Marina", "Engenharia de Software"))


if __name__ == "__main__":
    executar_demo()
