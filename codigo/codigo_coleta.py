import time
import csv
import platform

tamanhos = range(100, 1001, 100)
repeticoes = 100

sistema = platform.system()

if sistema == "Windows":
    nome_arquivo = "resultados_windows.csv"
else:
    nome_arquivo = "resultados_linux.csv"

with open(nome_arquivo, "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow([
        "bloco_MB",
        "teste",
        "alloc_ms",
        "write_ms",
        "read_ms",
        "free_ms"
    ])

    for mb in tamanhos:
        print(f"Iniciando testes com {mb} MB...")

        bloco_bytes = mb * 1024 * 1024

        for teste in range(1, repeticoes + 1):

            # ALLOCAÇÃO
            t0 = time.perf_counter_ns()

            bloco = bytearray(bloco_bytes)

            t1 = time.perf_counter_ns()
            alloc_ms = (t1 - t0) / 1_000_000

            # ESCRITA
            padrao = b'\xAA' * (1024 * 1024)

            t2 = time.perf_counter_ns()

            for inicio in range(0, len(bloco), len(padrao)):
                fim = inicio + len(padrao)
                bloco[inicio:fim] = padrao[:fim-inicio]

            t3 = time.perf_counter_ns()
            write_ms = (t3 - t2) / 1_000_000

            # LEITURA
            t4 = time.perf_counter_ns()

            soma = sum(bloco)

            t5 = time.perf_counter_ns()
            read_ms = (t5 - t4) / 1_000_000

            # LIBERAÇÃO
            t6 = time.perf_counter_ns()

            bloco.clear()
            del bloco

            t7 = time.perf_counter_ns()
            free_ms = (t7 - t6) / 1_000_000

            escritor.writerow([
                mb,
                teste,
                f"{alloc_ms:.6f}",
                f"{write_ms:.6f}",
                f"{read_ms:.6f}",
                f"{free_ms:.6f}"
            ])

            arquivo.flush()

        print(f"{mb} MB concluído.")

print()
print("Experimento concluído!")
print(f"Sistema: {sistema}")
print(f"Arquivo gerado: {nome_arquivo}")