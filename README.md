# Microbenchmark: Windows x Linux

Experimento para comparar o desempenho de operações de memória entre Windows e Linux em condições experimentais equivalentes.

## Objetivo

Comparar o tempo de execução das operações de alocação, escrita, leitura e liberação de memória no Windows e no Linux, utilizando as mesmas condições experimentais.

## Pergunta norteadora

Em condições experimentais equivalentes, qual dos sistemas operacionais apresenta melhor desempenho nas operações de alocação, escrita, leitura e liberação de memória?

## Hipótese

A hipótese do grupo é que o Linux apresentará menor tempo de execução nas operações de memória em comparação com o Windows, considerando as mesmas condições de hardware, código, tamanho dos blocos e número de repetições.

## Configuração experimental

O experimento será realizado utilizando duas máquinas virtuais no mesmo computador físico, mantendo as configurações das máquinas virtuais equivalentes.

### Hardware físico

- Processador: Intel(R) Core(TM) i5-103G1 CPU @ 1.00GHz
- Memória RAM: 8 GB
- Armazenamento: 238 GB

### Máquinas virtuais

| Configuração | Windows | Linux |
|---|---|---|
| Arquitetura | 64 bits | 64 bits |
| vCPUs | 2 | 2 |
| RAM | 3 GB | 3 GB |
| VirtualBox | 7.2.8 | 7.2.8 |
| Python | 3.13.14 | 3.13.14 |

A versão do Linux será definida antes da coleta dos dados.

## Operações avaliadas

As operações serão executadas na seguinte ordem:

1. Alocação
2. Escrita
3. Leitura
4. Liberação

## Protocolo experimental

Serão utilizados blocos de memória de 100 MB a 1000 MB, com incremento de 100 MB.

Cada tamanho de bloco será executado 100 vezes em cada sistema operacional.

Os tempos serão registrados em milissegundos e armazenados em arquivos CSV.

O mesmo código do microbenchmark será utilizado nos dois sistemas.

A execução será realizada com apenas um ambiente em funcionamento por vez, e aplicações desnecessárias serão fechadas antes dos testes.

A ordem de execução definida no protocolo é:

1. Windows
2. Linux

## Dados coletados

Os resultados do Windows serão armazenados em:

`dados/windows/`

Os resultados do Linux serão armazenados em:

`dados/linux/`

O formato dos arquivos CSV será:

```text
bloco_MB,teste,alloc_ms,write_ms,read_ms,free_ms

## Validação dos dados

Cada sistema deverá possuir 1.000 registros.

Serão verificados:

quantidade de registros;
tamanhos dos blocos;
número dos testes;
duplicidades;
valores ausentes;
tipos dos dados;
valores negativos;
identificação correta do sistema.

## Análise

Os registros serão agrupados por sistema operacional, tamanho do bloco e operação.

Para cada grupo serão calculados:

tempo médio;
mediana;
desvio padrão.

Os resultados serão apresentados por meio de tabelas e gráficos comparando Windows e Linux para cada tamanho de bloco e operação.

## Critério de desempenho

Será considerado que um sistema apresentou melhor desempenho quando apresentar menor tempo médio para realizar as operações de memória nas mesmas condições experimentais.

Caso os resultados sejam diferentes entre operações ou tamanhos de bloco, a análise considerará cada situação individualmente, evitando basear a conclusão em apenas um resultado.

## Estrutura do projeto

trabalho-microbenchmark/
│
├── README.md
├── codigo/
├── dados/
│   ├── windows/
│   └── linux/
├── analise/
├── resultados/
│   ├── tabelas/
│   └── graficos/
└── configuracoes/

## Integrantes
Camila Monteiro Mendes Rodrigues
Caroline da Rosa Wibelinger
Nicole Penz
Poliana Pautz Müller
