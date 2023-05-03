# sparse_matrix_generator
# Gerador de matrizes aleatórias

Este é um pequeno programa em Python que gera matrizes aleatórias de números inteiros e as salva em arquivos de texto com nomes baseados em hashes SHA-256.

## Requisitos

- Python 3.x
- Bibliotecas `hashlib`, `secrets` e `random`

## Utilização

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde se encontra o arquivo `gerador_matrizes.py`.
3. Execute o comando `python gerador_matrizes.py`.
4. Digite o número de matrizes que deseja gerar quando solicitado.
5. Digite o número de linhas e colunas de cada matriz quando solicitado.

O programa irá gerar as matrizes aleatórias e salvá-las em arquivos de texto com nomes baseados em hashes SHA-256. Cada arquivo conterá as dimensões da matriz na primeira linha, seguidas pelos valores dos elementos na matriz em linhas subsequentes.

## Observações

- O tamanho das matrizes geradas é definido pelo usuário.
- Os elementos das matrizes são números inteiros aleatórios entre 1 e 9, exceto quando gerados valores aleatórios maiores ou iguais a 4, nesse caso o valor 0 é inserido.
- O hash gerado é baseado em uma string aleatória gerada pela biblioteca `secrets`.
- Apenas os primeiros 20 caracteres do hash são utilizados como nome do arquivo de texto gerado.
- Este código é fornecido apenas como exemplo e não é otimizado para desempenho ou segurança em aplicações reais.
