from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth=HTTPBasicAuth()

app = Flask(__name__)
api = Api(app)

#USUARIOS = {'marcos':'123',
#            'henrique':'321'}

#@auth.verify_password
#def verificacao(login, senha):
#    print('validando usuarios.')
#    if not (login, senha):
#        return False#

#    return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    print('validando usuarios.')
    if not (login, senha):
        return False#

    return Usuarios.query.filter_by(login=login,senha=senha).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response = {
                'status':'error',
                'mensagem':'Pessoa nao encontrada.'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).fist()
        mensagem = 'Pessoa {} exclida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso','mensagem':mensagem}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        #response = [i for i in pessoas]
        response = [{'nome': i.nome, 'idade': i.idade, 'id': i.id} for i in pessoas]
        return response
        #print(response)
        #for i in pessoas:
            #lista.append('nome':i.nome)
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'nome': i.nome, 'id': i.id, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'nome': atividade.nome,
            'pessoa':atividade.pessoa.nome,
            'id': atividade.id
        }
        return response
api.add_resource(Pessoa,'/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoas/')
api.add_resource(ListaAtividades,'/atividades/')

if __name__ == '__main__':
    app.run(debug=True)