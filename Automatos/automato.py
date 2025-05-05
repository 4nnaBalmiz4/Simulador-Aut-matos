import json
import sys
import csv
import time

argvs = sys.argv
arquivo_json = argvs[1]
arquivo_entrada = argvs[2]
arquivo_saida = argvs[3]

# Carrega a definição do autômato do arquivo JSON
with open(arquivo_json, 'r') as dados:
    arq_json = json.load(dados)

# Inicializa array para guardar as palavras de entrada e seus resultados esperados
entradas = []

# Extrai dados do arquivo CSV de entrada
with open(arquivo_entrada, "r") as csvfile:
    # Configura o parser CSV com ponto e vírgula como separador
    arq_csv = csv.reader(csvfile, delimiter=";")

    # Coleta cada linha do arquivo
    for linha in arq_csv:
        # Guarda cada entrada com seu resultado esperado
        entradas.append(linha)

# Extrai os componentes do autômato do JSON
estado_inicial = str(arq_json["initial"])
estado_final = list(map(str, arq_json["final"]))
transicoes = arq_json["transitions"]

# Processa as entradas e grava resultados
with open(arquivo_saida, "w") as saida:
    # Analisa cada palavra de entrada
    for entrada in entradas:
        # Marca início da análise para cálculo de tempo
        tempo_inicial = time.time()

        atual_state = estado_inicial
        palavra = entrada[0]
        cont = 0

        # Avalia cada símbolo da palavra
        while cont < len(palavra):
            found_transition = False
            # Busca uma transição válida no estado atual
            for transition in transicoes:
                if transition["from"] == atual_state and transition["read"] == palavra[cont]:
                    atual_state = transition["to"]
                    found_transition = True
                    break

            # Interrompe se não há transição possível
            if not found_transition:
                break

            cont += 1

        # Determina aceitação (1) ou rejeição (0)
        valorFinal = 1 if atual_state in estado_final and cont == len(
            palavra) else 0

        # Finaliza medição do tempo de processamento
        tempo_final = time.time()

        # Prepara dados para gravação
        entrada_str = entrada[0]
        resultado_esperado = entrada[1]

        tempo = f"{tempo_final - tempo_inicial:.5f}"
        saida.write(
            f"{entrada_str};{resultado_esperado};{valorFinal};{tempo}\n")
