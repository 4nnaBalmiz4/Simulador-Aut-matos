# Implementação de Automato Finito 

Este projeto implementa um simulador de autômatos finitos em Python, contendo um arquivo com um diagrama de transição e um arquivo com entrada teste, estes são combinados e excutados, resultando em um arquivo de saída. 

## Tecnologias Utilizadas

- **Python** - Linguagem principal do projeto
- **JSON** - Especificação da Máquina de Estados
- **CSV** - Entradas para Teste e Saída

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `automato.py` - Arquivo principal 
- `arquivo_do_automato.aut.json` - Especificações do autômato
- `arquivo_de_testes.in.csv` - Arquivo de entrada
- `arquivo_de_saida.out.csv` - Arquivo de Saída

## Como Executar

1. **Baixe e instale o Python**, caso ainda não tenha:
     
2. **Execute o simulador**:
   ```sh
   python .\automato.py arquivo_do_automato.aut.json arquivo_de_testes.in.csv arquivo_de_saida.out.csv
   ```

O simulador irá processar o arquivo `automato.py`, verificar as especificações do autômato, e então executar o código.

## Exemplo de JSON (`input.lang`)

```c
{
    "initial": 0,
    "final" : [2],
    "transitions": [
      {
        "from": "0",
        "to": "0",
        "read": "a"
      },
      {
        "from": "2",
        "to": "2",
        "read": "a"
      },
      {
        "from": "1",
        "to": "1",
        "read": "b"
      },
      {
        "from": "1",
        "to": "2",
        "read": "a"
      },
      {
        "from": "0",
        "to": "1",
        "read": "b"
      }
    ]
  }
```

Exemplo de Entrada:
```
ba;1
aaaabbbbbaaaaa;1
abababab;0
bbbbbbbb;0
aaaaaaaaaaaa;0
aaaaabaaaaa;1
```

Saída esperada:
```
ba;1;1;0.00001
aaaabbbbbaaaaa;1;1;0.00001
abababab;0;0;0.00000
bbbbbbbb;0;0;0.00000
aaaaaaaaaaaa;0;0;0.00000
aaaaabaaaaa;1;1;0.00001
```

## Aluna
* Anna Laura Balmiza Soares
