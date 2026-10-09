# Microbenchmark: Windows x Linux

Experimento para comparar o desempenho de operações de memória entre Windows e Linux, utilizando máquinas virtuais com configurações equivalentes.

## Objetivo

Comparar o tempo de execução das operações de alocação, escrita, leitura e liberação de memória no Windows e no Linux, utilizando as mesmas condições experimentais.

## Pergunta norteadora

Em condições experimentais equivalentes, qual dos sistemas operacionais apresenta melhor desempenho nas operações de alocação, escrita, leitura e liberação de memória?

## Hipótese

A hipótese inicial do grupo foi que o Linux apresentaria menores tempos de execução nas operações de memória em comparação com o Windows, considerando as mesmas condições de hardware, código, tamanho dos blocos e número de repetições.

## Configuração experimental

O experimento foi realizado em duas máquinas virtuais no mesmo computador físico, utilizando configurações equivalentes.

### Hardware físico

* Processador: Intel(R) Core(TM) i5-103G1 CPU @ 1.00GHz
* Memória RAM: 8 GB
* Armazenamento: 238 GB

### Configuração das máquinas virtuais

| Configuração        | Windows    | Linux       |
| ------------------- | ---------- | ----------- |
| Sistema operacional | Windows 10 | Ubuntu      |
| Versão              | 10.0.19045 | 24.04.5 LTS |
| Arquitetura         | 64 bits    | 64 bits     |
| vCPUs               | 2          | 2           |
| Memória RAM         | 3 GB       | 3 GB        |
| Python              | 3.13.14    | 3.13.14     |
| VirtualBox          | 7.2.20     | 7.2.20      |

## Operações avaliadas

Em cada repetição, foram realizadas as seguintes operações, nesta ordem:

1. Alocação de memória.
2. Escrita de dados.
3. Leitura dos dados.
4. Liberação da memória.

## Protocolo experimental

Foram utilizados blocos de memória de 100 MB a 1000 MB, com incrementos de 100 MB. Cada tamanho foi testado 100 vezes em cada sistema operacional, totalizando 1000 registros por sistema e 2000 registros no conjunto completo.

O mesmo código do microbenchmark foi utilizado nos dois ambientes. Na escrita, foi utilizado um padrão de dados de 1 MB repetido até preencher o bloco, evitando a criação de uma segunda estrutura de memória muito grande.

Os tempos foram medidos com `perf_counter_ns()` e convertidos para milissegundos. Os resultados foram registrados em arquivos CSV separados para Windows e Linux.

Os testes foram executados em um ambiente por vez, mantendo as configurações das máquinas virtuais equivalentes e fechando aplicações desnecessárias sempre que possível.

## Dados coletados

Os arquivos originais gerados pelo experimento foram:

* `resultados_windows.csv`
* `resultados_linux.csv`

O formato utilizado foi:

`bloco_MB,teste,alloc_ms,write_ms,read_ms,free_ms`

Após a coleta, os dados foram reunidos em um arquivo processado, preservando os arquivos originais.

## Validação dos dados

Os arquivos foram conferidos quanto à quantidade de registros, aos tamanhos dos blocos, ao número de repetições, à presença de valores ausentes ou duplicados, aos tipos dos dados e à existência de tempos negativos.

Cada sistema apresentou 1000 registros válidos, totalizando 2000 registros no arquivo combinado.

## Análise

Os dados foram agrupados por sistema operacional, tamanho do bloco e operação. Para cada grupo, foram calculados a média e o desvio padrão dos tempos.

Os resultados foram organizados em uma tabela estatística e em quatro gráficos, um para cada operação, permitindo comparar os tempos médios do Windows e do Linux nos diferentes tamanhos de bloco.

## Critério de desempenho

Foi considerado melhor o desempenho do sistema que apresentou menor tempo médio para realizar determinada operação nas mesmas condições experimentais. Quando os resultados variaram entre operações ou tamanhos de bloco, cada situação foi analisada separadamente.

## Integrantes

Camila Monteiro Mendes Rodrigues, Caroline da Rosa Wibelinger, Nicole Penz e Poliana Pautz Müller.

## Instruções para reprodução

Para reproduzir o experimento:

1. Configurar duas máquinas virtuais no VirtualBox, uma com Windows e outra com Linux, ambas com 2 vCPUs e 3 GB de RAM.
2. Instalar o Python 3.13.14 nos dois sistemas.
3. Utilizar a mesma versão do código do microbenchmark nos dois ambientes.
4. Executar o programa separadamente em cada sistema operacional.
5. Realizar 100 repetições para cada tamanho de bloco, de 100 MB a 1000 MB.
6. Salvar os resultados de cada sistema em arquivos CSV separados, seguindo o formato definido neste projeto.
7. Executar o código de processamento para validar, reunir e analisar os resultados.
8. Gerar a tabela estatística e os gráficos para comparar os sistemas operacionais.
