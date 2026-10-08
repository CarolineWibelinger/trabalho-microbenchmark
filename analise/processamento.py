import csv
import statistics


arquivo_linux = "resultados_linux.csv"
arquivo_windows = "resultados_windows.csv"

arquivo_processado = "resultados_processados.csv"
arquivo_resumo = "resumo_estatistico.csv"


colunas_esperadas = [
    "bloco_MB",
    "teste",
    "alloc_ms",
    "write_ms",
    "read_ms",
    "free_ms"
]


arquivos = [
    ("Linux", arquivo_linux),
    ("Windows", arquivo_windows)
]


dados = []


print("Iniciando processamento...")
print()


# --------------------------------------------------
# LEITURA E VALIDAÇÃO DOS CSVs
# --------------------------------------------------

for sistema, nome_arquivo in arquivos:

    print(f"Lendo dados do {sistema}...")

    with open(nome_arquivo, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        # Verifica o cabeçalho
        if leitor.fieldnames != colunas_esperadas:
            print(f"ERRO: cabeçalho incorreto em {nome_arquivo}.")
            print("Cabeçalho encontrado:", leitor.fieldnames)
            raise SystemExit

        quantidade = 0

        for linha in leitor:

            quantidade += 1

            # Converte os valores para os tipos corretos
            bloco = int(linha["bloco_MB"])
            teste = int(linha["teste"])

            alloc = float(linha["alloc_ms"])
            write = float(linha["write_ms"])
            read = float(linha["read_ms"])
            free = float(linha["free_ms"])

            # Verifica se os tempos são válidos
            tempos = [alloc, write, read, free]

            for tempo in tempos:
                if tempo < 0:
                    print(f"ERRO: tempo negativo encontrado em {nome_arquivo}.")
                    raise SystemExit

            # Adiciona o sistema aos dados
            dados.append({
                "sistema": sistema,
                "bloco_MB": bloco,
                "teste": teste,
                "alloc_ms": alloc,
                "write_ms": write,
                "read_ms": read,
                "free_ms": free
            })

        # Cada sistema deve possuir 1000 registros
        if quantidade != 1000:
            print(
                f"ERRO: {nome_arquivo} possui "
                f"{quantidade} registros em vez de 1000."
            )
            raise SystemExit

        print(f"{sistema}: {quantidade} registros OK.")


print()
print(f"Total de registros lidos: {len(dados)}")


# --------------------------------------------------
# SALVA OS DADOS PROCESSADOS
# --------------------------------------------------

with open(
    arquivo_processado,
    "w",
    encoding="utf-8",
    newline=""
) as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow([
        "sistema",
        "bloco_MB",
        "teste",
        "alloc_ms",
        "write_ms",
        "read_ms",
        "free_ms"
    ])

    for linha in dados:

        escritor.writerow([
            linha["sistema"],
            linha["bloco_MB"],
            linha["teste"],
            linha["alloc_ms"],
            linha["write_ms"],
            linha["read_ms"],
            linha["free_ms"]
        ])


print()
print(f"Arquivo criado: {arquivo_processado}")


# --------------------------------------------------
# CÁLCULO DE MÉDIA E DESVIO PADRÃO
# --------------------------------------------------

operacoes = [
    "alloc_ms",
    "write_ms",
    "read_ms",
    "free_ms"
]

resumo = []


for sistema in ["Linux", "Windows"]:

    for bloco in range(100, 1001, 100):

        # Seleciona os 100 testes daquele sistema e tamanho
        grupo = []

        for linha in dados:
            if (
                linha["sistema"] == sistema
                and linha["bloco_MB"] == bloco
            ):
                grupo.append(linha)

        # Verificação
        if len(grupo) != 100:
            print(
                f"ERRO: {sistema} - {bloco} MB possui "
                f"{len(grupo)} testes."
            )
            raise SystemExit

        # Calcula média e desvio padrão
        for operacao in operacoes:

            valores = []

            for linha in grupo:
                valores.append(linha[operacao])

            media = statistics.mean(valores)
            desvio = statistics.stdev(valores)

            resumo.append({
                "sistema": sistema,
                "bloco_MB": bloco,
                "operacao": operacao,
                "media_ms": media,
                "desvio_padrao_ms": desvio
            })


# --------------------------------------------------
# SALVA O RESUMO ESTATÍSTICO
# --------------------------------------------------

with open(
    arquivo_resumo,
    "w",
    encoding="utf-8",
    newline=""
) as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow([
        "sistema",
        "bloco_MB",
        "operacao",
        "media_ms",
        "desvio_padrao_ms"
    ])

    for linha in resumo:

        escritor.writerow([
            linha["sistema"],
            linha["bloco_MB"],
            linha["operacao"],
            f"{linha['media_ms']:.6f}",
            f"{linha['desvio_padrao_ms']:.6f}"
        ])


print(f"Arquivo criado: {arquivo_resumo}")


# --------------------------------------------------
# MOSTRA UM RESUMO NO TERMINAL
# --------------------------------------------------

print()
print("======================================")
print("PROCESSAMENTO CONCLUÍDO")
print("======================================")

print(f"Registros processados: {len(dados)}")
print(f"Arquivo com dados: {arquivo_processado}")
print(f"Arquivo com médias: {arquivo_resumo}")

print()
print("Todos os dados foram processados com sucesso.")