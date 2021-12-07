from models import Pessoas #, db_session

def insere_pessoas():
    #pessoa = Pessoas(nome='Marcos', idade=55)
    pessoa = Pessoas(nome='Denise', idade=56)
    print(pessoa)
    #db_session.add(pessoa)
    #db_session.commit()
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all() # filter_by(nome='Marcos')
    print(pessoas)
    #for i in pessoa:
    #    print(i.nome)
    pessoa = Pessoas.query.filter_by(nome='Deise').first()
    #print(pessoa.idade)
    #for p in pessoa:
    #    print(p)
    #print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Denise").first()
    #pessoa.idade = 57
    pessoa.nome = 'Deise'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Deise").first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
