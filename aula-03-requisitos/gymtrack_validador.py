"""
Aula 03 - GymTrack: validador de treino.

O exercício separa requisitos funcionais, como validar os dados do treino,
de requisitos não funcionais, como mensagens claras e regras simples de uso.
"""

from dataclasses import dataclass


@dataclass
class Treino:
    aluno: str
    modalidade: str
    duracao_minutos: int
    intensidade: str
    frequencia_cardiaca: int


INTENSIDADES_VALIDAS = {"leve", "moderada", "alta"}


def validar_treino(treino: Treino) -> list[str]:
    erros = []

    if not treino.aluno.strip():
        erros.append("O nome do aluno e obrigatorio.")

    if not treino.modalidade.strip():
        erros.append("A modalidade do treino e obrigatoria.")

    if treino.duracao_minutos < 10 or treino.duracao_minutos > 180:
        erros.append("A duracao deve ficar entre 10 e 180 minutos.")

    if treino.intensidade.lower() not in INTENSIDADES_VALIDAS:
        erros.append("A intensidade deve ser leve, moderada ou alta.")

    if treino.frequencia_cardiaca < 60 or treino.frequencia_cardiaca > 200:
        erros.append("A frequencia cardiaca deve ficar entre 60 e 200 bpm.")

    return erros


def classificar_treino(treino: Treino) -> str:
    if treino.intensidade.lower() == "alta" and treino.duracao_minutos >= 45:
        return "Treino avancado"
    if treino.intensidade.lower() == "moderada" and treino.duracao_minutos >= 30:
        return "Treino intermediario"
    return "Treino iniciante"


def executar_demo() -> None:
    treinos = [
        Treino("Ana Souza", "Musculacao", 50, "alta", 148),
        Treino("Bruno Lima", "Corrida", 8, "extrema", 215),
    ]

    print("GymTrack - Validacao de Treinos")
    print("-" * 35)

    for treino in treinos:
        print(f"Aluno: {treino.aluno}")
        erros = validar_treino(treino)

        if erros:
            print("Status: treino recusado")
            for erro in erros:
                print(f"- {erro}")
        else:
            print("Status: treino aprovado")
            print(f"Classificacao: {classificar_treino(treino)}")

        print()


if __name__ == "__main__":
    executar_demo()
