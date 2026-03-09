import itertools

# poderes dos cavaleiros
poderes = [1.5, 1.4, 1.3, 1.2, 1.1]
nomes = ["Seiya", "Shiryu", "Hyoga", "Shun", "Ikki"]

# energia inicial de cada um
energia = 5

# dificuldade das 12 casas
casas = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100, 110, 120]

# dicionário para guardar resultados já calculados
memo = {}

def todos_sobreviveram(lista_energia):
    for e in lista_energia:
        if e < 1:
            return False
    return True


def resolver(casa_atual, e0, e1, e2, e3, e4):

    # se já passou por todas as casas
    if casa_atual == 12:
        if todos_sobreviveram([e0, e1, e2, e3, e4]):
            return 0, []
        else:
            return float("inf"), []

    chave = (casa_atual, e0, e1, e2, e3, e4)

    if chave in memo:
        return memo[chave]

    energias = [e0, e1, e2, e3, e4]

    # ver quem ainda tem energia
    vivos = []
    for i in range(5):
        if energias[i] > 0:
            vivos.append(i)

    melhor_tempo = float("inf")
    melhor_caminho = None

    # testar várias combinações possíveis de cavaleiros
    for tam in range(1, len(vivos) + 1):
        for grupo in itertools.combinations(vivos, tam):

            soma = 0
            for i in grupo:
                soma += poderes[i]

            tempo_luta = casas[casa_atual] / soma

            novas = energias[:]
            for i in grupo:
                novas[i] -= 1

            resto_tempo, resto_seq = resolver(
                casa_atual + 1,
                novas[0],
                novas[1],
                novas[2],
                novas[3],
                novas[4]
            )

            total = tempo_luta + resto_tempo

            if total < melhor_tempo and resto_tempo != float("inf"):
                melhor_tempo = total
                melhor_caminho = [grupo] + resto_seq

    memo[chave] = (melhor_tempo, melhor_caminho)
    return memo[chave]


# executa o programa
tempo_final, sequencia = resolver(0, energia, energia, energia, energia, energia)

if tempo_final == float("inf"):
    print("Não achei uma solução onde todos sobrevivem.")
else:
    print(f"Tempo mínimo: {tempo_final:.2f} minutos\n")

    print("Equipes usadas em cada casa:")

    for i in range(len(sequencia)):
        equipe = sequencia[i]

        nomes_equipe = []
        soma = 0

        for j in equipe:
            nomes_equipe.append(nomes[j])
            soma += poderes[j]

        tempo = casas[i] / soma

        print(
            f"Casa {i+1} (dif {casas[i]}): "
            f"{', '.join(nomes_equipe)} | "
            f"poder = {soma:.2f} | "
            f"tempo = {tempo:.2f} min"
        )