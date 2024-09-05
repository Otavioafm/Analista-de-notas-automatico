from src.PostgreSql.Conector_Sql import Aluno, Session
from src.PostgreSql.Manipulacao_Dados_Aulas import analisar_dados_aulas

def inserir_dados_alunos():
    with open('src\\Planilha_Google\\Dados_Alunos\\Dados_Alunos.txt', 'r') as file:
        linhas = file.readlines()

    coluna_nome = []
    coluna_idade = []
    coluna_estado = []
    coluna_cidade = []

    coluna_atual = None

    for linha in linhas:
        linha = linha.strip()
        
        if linha == "Nome:":
            coluna_atual = 'nome'
        elif linha == "Idade:":
            coluna_atual = 'idade'
        elif linha == "Estado:":
            coluna_atual = 'estado'
        elif linha == "Cidade:":
            coluna_atual = 'cidade'
        
        elif linha:  
            if coluna_atual == 'nome':
                coluna_nome.append(linha)
            elif coluna_atual == 'idade':
                coluna_idade.append(linha)
            elif coluna_atual == 'estado':
                coluna_estado.append(linha)
            elif coluna_atual == 'cidade':
                coluna_cidade.append(linha)

    print("Nome:", coluna_nome,     "\n")
    print("Idade:", coluna_idade,   "\n")
    print("Estado:", coluna_estado, "\n")
    print("Cidade:", coluna_cidade, "\n")

    session = Session()
    
    if len(coluna_nome) == len(coluna_idade) == len(coluna_estado) == len(coluna_cidade):
        for i in range(len(coluna_nome)):
            aluno = Aluno(
                nome=coluna_nome[i],
                idade=int(coluna_idade[i]),
                estado=coluna_estado[i],
                cidade=coluna_cidade[i]
            )
            session.add(aluno)
            session.commit()

            
            arquivo_dados = 'C:\\Users\\otavi\\OneDrive\\Área de Trabalho\\SqlAlchemy\\src\\Planilha_Google\\Dados_Aulas\\Dados_colunas.txt'
            pontuacao_final = analisar_dados_aulas(arquivo_dados, aluno.id)
            print(f"Pontuação final do aluno {aluno.nome}: {pontuacao_final}")

        session.close()
        print("Dados inseridos com sucesso!")
    else:
        print("Erro: As listas de dados têm tamanhos diferentes. Verifique os dados antes de inserir.")

if __name__ == "__main__":
    inserir_dados_alunos()
