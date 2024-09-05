import os
from src.Planilha_Google.Conector_Google import conectar_planilhas

def obter_dados_como_listas(nome_planilha, nome_aba):
    planilhas = conectar_planilhas()
    
    if planilhas is not None:
        print("Conexão com a planilha Google estabelecida.")
        planilha = next((p for p in planilhas if p.title == nome_planilha), None)
        
        if planilha:
            aba = planilha.worksheet(nome_aba)
            dados = aba.get_all_values()
            
            lista_coluna_5 = [linha[4] for linha in dados if len(linha) > 4]  
            lista_coluna_6 = [linha[5] for linha in dados if len(linha) > 5]  
            lista_coluna_7 = [linha[6] for linha in dados if len(linha) > 6]
            lista_coluna_8 = [linha[7] for linha in dados if len(linha) > 7]
            lista_coluna_9 = [linha[8] for linha in dados if len(linha) > 8]  
            lista_coluna_10 = [linha[9] for linha in dados if len(linha) > 9]
            lista_coluna_12 = [linha[11] for linha in dados if len(linha) > 11]

            pasta_base = os.path.dirname(os.path.abspath(__file__))
            pasta_dados = os.path.join(pasta_base, 'Dados_Aulas')
            os.makedirs(pasta_dados, exist_ok=True)
            print(f"Diretório para salvar dados: {pasta_dados}")

            caminho_arquivo = os.path.join(pasta_dados, 'Dados_colunas.txt')
            print(f"Tentando escrever no arquivo: {caminho_arquivo}")

            try:
                with open(caminho_arquivo, 'w') as file:
                    file.write("Coluna 5:\n")
                    file.write('\n'.join(lista_coluna_5) + '\n\n')

                    file.write("Coluna 6:\n")
                    file.write('\n'.join(lista_coluna_6) + '\n\n')

                    file.write("Coluna 7:\n")
                    file.write('\n'.join(lista_coluna_7) + '\n\n')

                    file.write("Coluna 8:\n")
                    file.write('\n'.join(lista_coluna_8) + '\n\n')

                    file.write("Coluna 9:\n")
                    file.write('\n'.join(lista_coluna_9) + '\n\n')

                    file.write("Coluna 10:\n")
                    file.write('\n'.join(lista_coluna_10) + '\n\n')

                    file.write("Coluna 12:\n")
                    file.write('\n'.join(lista_coluna_12) + '\n\n')

                print(f'Dados das colunas salvos em {caminho_arquivo}.')
            except Exception as e:
                print(f"Erro ao tentar escrever no arquivo: {e}")
        else:
            print(f'Planilha com o nome {nome_planilha} não encontrada.')
    else:
        print('Não foi possível conectar às planilhas.')
