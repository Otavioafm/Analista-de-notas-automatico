from src.PostgreSql.Conector_Sql import Aluno, Session, DadosAulas

def analisar_dados_aulas(arquivo_dados, aluno_id):
    with open(arquivo_dados, 'r') as file:
        linhas = file.readlines()

    lista_coluna_5 = []
    lista_coluna_6 = []
    lista_coluna_7 = []
    lista_coluna_8 = []
    lista_coluna_9 = []
    lista_coluna_10 = []
    lista_coluna_12 = []

    coluna_atual = None

    for linha in linhas:
        linha = linha.strip()
        
        if linha == "Coluna 5:":
            coluna_atual = 'coluna_5'
        elif linha == "Coluna 6:":
            coluna_atual = 'coluna_6'
        elif linha == "Coluna 7:":
            coluna_atual = 'coluna_7'
        elif linha == "Coluna 8:":
            coluna_atual = 'coluna_8'
        elif linha == "Coluna 9:":
            coluna_atual = 'coluna_9'
        elif linha == "Coluna 10:":
            coluna_atual = 'coluna_10'
        elif linha == "Coluna 12:":
            coluna_atual = 'coluna_12'
        
        elif linha: 
            if coluna_atual == 'coluna_5':
                lista_coluna_5.append(linha)
            elif coluna_atual == 'coluna_6':
                lista_coluna_6.append(linha)
            elif coluna_atual == 'coluna_7':
                lista_coluna_7.append(linha)
            elif coluna_atual == 'coluna_8':
                lista_coluna_8.append(linha)
            elif coluna_atual == 'coluna_9':
                lista_coluna_9.append(linha)
            elif coluna_atual == 'coluna_10':
                lista_coluna_10.append(linha)
            elif coluna_atual == 'coluna_12':
                lista_coluna_12.append(linha)

    pontuacao_total = 500

    dias = [data[:2] for data in lista_coluna_5] 
    dias_unicos = set(dias)
    todos_os_dias = set(f"{i:02d}" for i in range(1, 31))  # Dias de 01 a 30
    dias_faltando = todos_os_dias - dias_unicos
    dias_repetidos = [dia for dia in dias if dias.count(dia) > 1]

    if len(dias_faltando) == 0:
        print("Todos os dias do mês estão presentes.")
    else:
        print(f"Faltam os seguintes dias: {sorted(dias_faltando)}")
        pontuacao_total -= len(dias_faltando) * 30

    if len(dias_repetidos) == 0:
        print("Não há dias repetidos.")
    else:
        print(f"Existem dias repetidos: {sorted(set(dias_repetidos))}")

    print(f"Total de dias únicos: {len(dias_unicos)}")

    diferentes = 0
    if len(lista_coluna_9) == len(lista_coluna_10):
        for total, atual in zip(lista_coluna_9, lista_coluna_10):
            if total != atual:
                diferentes += 1
        
        print(f"Aulas faltando completar: {diferentes}")
        pontuacao_total -= diferentes * 50
    else:
        print("As listas 'Aula total do módulo' e 'Aula atual do módulo' têm tamanhos diferentes.")
    
    print(f"Pontos perdidos devido a dias faltando: {len(dias_faltando) * 30}")
    print(f"Pontos perdidos devido a aulas não completadas: {diferentes * 50}")
    print(f"Pontuação final do aluno: {pontuacao_total}")

    # Inserindo no banco de dados
    session = Session()
    dados_aulas = DadosAulas(
        aluno_id=aluno_id,
        pontuacao_final=pontuacao_total,
        pontos_perdidos=500 - pontuacao_total
    )
    session.add(dados_aulas)
    session.commit()
    session.close()

    return pontuacao_total
