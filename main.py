from src.PostgreSql.Conector_Sql import Aluno, Session
from src.PostgreSql.Manipulacao_Dados_Alunos import inserir_dados_alunos
from src.PostgreSql.Manipulacao_Dados_Aulas import analisar_dados_aulas

from src.Planilha_Google.Conector_Google import conectar_planilhas
from src.Planilha_Google.Dados_Aulas import obter_dados_como_listas
from src.Planilha_Google.Dados_Alunos import obter_dados_alunos

def main():
    print("Tentando conectar às planilhas...")
    planilhas = conectar_planilhas()  
    
    if planilhas is not None:
        print("Conexão bem-sucedida!")
        nome_planilha = ''
        nome_aba_dados = ''
        
        print("Obtendo dados como listas...")
        obter_dados_como_listas(nome_planilha, nome_aba_dados)
        
        print("Obtendo dados dos alunos...")
        obter_dados_alunos(nome_planilha, nome_aba_dados)
        
        print("Inserindo dados dos alunos no banco de dados...")
        inserir_dados_alunos()
        
    else:
        print("Erro ao conectar às planilhas. Verifique as credenciais e a conexão.")

if __name__ == "__main__":
    main()
