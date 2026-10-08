import csv
import matplotlib.pyplot as plt

dados = []

with open("resumo_estatistico.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        dados.append({
            "sistema": linha["sistema"],
            "bloco": int(linha["bloco_MB"]),
            "operacao": linha["operacao"],
            "media": float(linha["media_ms"])
        })

operacoes = {
    "alloc_ms": "Alocação",
    "write_ms": "Escrita",
    "read_ms": "Leitura",
    "free_ms": "Liberação"
}

for operacao in operacoes:

    tamanhos = []
    linux = []
    windows = []

    for tamanho in range(100, 1001, 100):

        tamanhos.append(tamanho)

        for linha in dados:

            if linha["bloco"] == tamanho and linha["operacao"] == operacao:

                if linha["sistema"] == "Linux":
                    linux.append(linha["media"])

                elif linha["sistema"] == "Windows":
                    windows.append(linha["media"])

    plt.plot(tamanhos, linux, marker="o", label="Linux")
    plt.plot(tamanhos, windows, marker="o", label="Windows")

    plt.title("Tempo médio - " + operacoes[operacao])
    plt.xlabel("Tamanho do bloco (MB)")
    plt.ylabel("Tempo (ms)")
    plt.xticks(tamanhos)
    plt.legend()
    plt.grid()

    plt.savefig("grafico_" + operacao + ".png", dpi=300)
    plt.close()

print("Gráficos criados com sucesso!")