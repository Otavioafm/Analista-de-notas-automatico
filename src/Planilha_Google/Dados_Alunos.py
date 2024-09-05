import os
from src.Planilha_Google.Conector_Google import conectar_planilhas

def obter_dados_alunos(nome_planilha, nome_aba):
    planilhas = conectar_planilhas()
    
    if planilhas is not None:
        planilha = next((p for p in planilhas if p.title == nome_planilha), None)
        
        if planilha:
            aba = planilha.worksheet(nome_aba)
            colunas = {
                'Nome': [], 'Idade': [], 'Estado': [], 'Cidade': []
            }

            for indice, coluna in enumerate(colunas.keys(), start=1):
                try:
                    dado = aba.cell(2, indice).value
                    colunas[coluna].append(dado)
                except Exception as e:
                    print(f'Erro ao obter dados da coluna {coluna}: {e}')
                    colunas[coluna].append(None)

            
            pasta_base = os.path.dirname(os.path.abspath(__file__))  
            pasta_local = os.path.join(pasta_base, 'Dados_Alunos')
            os.makedirs(pasta_local, exist_ok=True)

            caminho_arquivo = os.path.join(pasta_local, 'Dados_Alunos.txt')

            with open(caminho_arquivo, 'w') as file:
                for coluna, dados in colunas.items():
                    file.write(f'{coluna}:\n')
                    for dado in dados:
                        file.write(f'{dado}\n')
                    file.write('\n')

            print(f'Dados salvos em {caminho_arquivo}.')
        else:
            print(f'Planilha com o nome {nome_planilha} não encontrada.')
    else:
        print('Não foi possível conectar às planilhas.')

if __name__ == "__main__":
    nome_planilha = 'economia'  
    nome_aba = 'Página1'  
    obter_dados_alunos(nome_planilha, nome_aba)
