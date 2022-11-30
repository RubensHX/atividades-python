from flask import Flask
from flask_restx import reqparse, abort, Api, Resource

from estoque import Produto, aborta_se_o_produto_nao_existe

app = Flask(__name__)
api = Api(app)

FOLHA_DE_PAGAMENTO = [{'cpf': 0, 'nome': 'João', 'horas_trabalhadas': 12, 'valor_da_hora': 128.55},
                      {'cpf': 1, 'nome': 'João', 'horas_trabalhadas': 12,
                          'valor_da_hora': 49.89},
                      {'cpf': 2, 'nome': 'João', 'horas_trabalhadas': 12,
                          'valor_da_hora': 89.99},
                      {'cpf': 3, 'nome': 'João', 'horas_trabalhadas': 12, 'valor_da_hora': 78.63},]


def aborta_se_a_folha_de_pagamento_nao_existe(cpf):
    if cpf not in [folha['cpf'] for folha in FOLHA_DE_PAGAMENTO]:
        abort(404, message="Folha de pagamento do cpf: {} não existe".format(cpf))


parser = reqparse.RequestParser()
parser.add_argument('cpf', type=int, help="cpfentificador do produto")
parser.add_argument('nome', type=str, required=True, help="Nome do produto")
parser.add_argument('preco', type=float, required=True,
                    help="Preço do produto")


class FolhaDePagamento(Resource):
    def get(self, cpf):
        aborta_se_o_produto_nao_existe(cpf)
        return FOLHA_DE_PAGAMENTO[cpf]

    def delete(self, cpf):
        aborta_se_o_produto_nao_existe(cpf)
        del FOLHA_DE_PAGAMENTO[cpf]
        return '', 204

    def put(self, cpf):
        args = parser.parse_args()
        folha = {'cpf': cpf, 'nome': args['nome'], 'horas_trabalhadas': args['horas_trabalhadas'], 'valor_da_hora': args['valor_da_hora']}
        FOLHA_DE_PAGAMENTO[cpf] = folha
        return folha, 201


class ListaFolhaDePagamento(Resource):
    def get(self):
        return Produto

    def post(self):
        args = parser.parse_args()
        cpf = len(FOLHA_DE_PAGAMENTO)
        folha = {'cpf': cpf, 'nome': args['nome'], 'horas_trabalhadas': args['horas_trabalhadas'], 'valor_da_hora': args['valor_da_hora']}
        FOLHA_DE_PAGAMENTO.append(folha)
        return folha, 201


api.add_resource(ListaFolhaDePagamento, '/folhas-de-pagamento')
api.add_resource(FolhaDePagamento, '/folha-de-pagamento/<cpf>')

if (__name__ == '__main__'):
    app.run(debug=True)
