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

### Configuração das máquinas virtuais

| Configuração | Windows | Linux |
|---|---|---|
| Sistema operacional | Windows 10 | Ubuntu |
| Versão | 10.0.19045 | 24.04.5 LTS (Noble Numbat) |
| Arquitetura | 64 bits | 64 bits |
| vCPUs | 2 | 2 |
| Memória RAM | 3 GB | 3 GB |
| Python | 3.13.14 | 3.13.14 |
| VirtualBox | 7.2.20 | 7.2.20 |

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

## Integrantes
Camila Monteiro Mendes Rodrigues, 
Caroline da Rosa Wibelinger, 
Nicole Penz, 
Poliana Pautz Müller

## Instruções para reprodução

Para reproduzir o experimento, é necessário configurar os dois ambientes virtuais com as mesmas condições definidas neste projeto.

1. Configurar uma máquina virtual com Windows e outra com Linux, utilizando 2 vCPUs e 3 GB de RAM em cada ambiente.
2. Instalar o Python 3.13.14 nos dois sistemas.
3. Utilizar a mesma versão do código do microbenchmark disponível na pasta `codigo/`.
4. Executar o microbenchmark no Windows e no Linux, seguindo a ordem definida no protocolo: Windows primeiro e Linux depois.
5. Realizar os testes com blocos de 100 MB a 1000 MB, aumentando 100 MB por vez, com 100 repetições para cada tamanho.
6. Salvar os resultados de cada sistema em arquivos CSV, utilizando o formato definido no projeto.
7. Armazenar os resultados do Windows em `dados/windows/` e os resultados do Linux em `dados/linux/`.
8. Executar o código de análise disponível na pasta `analise/` para validar e comparar os resultados.
9. Os resultados das tabelas e dos gráficos devem ser armazenados nas respectivas pastas em `resultados/`.
