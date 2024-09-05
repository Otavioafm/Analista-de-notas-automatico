from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


DATABASE_URI = ''
engine = create_engine(DATABASE_URI)

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    estado = Column(String)
    cidade = Column(String)

 
    dados_aulas = relationship("DadosAulas", back_populates="aluno")


class DadosAulas(Base):
    __tablename__ = 'dados_aulas'
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    pontuacao_final = Column(Integer)
    pontos_perdidos = Column(Integer)

    aluno = relationship("Aluno", back_populates="dados_aulas")


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
