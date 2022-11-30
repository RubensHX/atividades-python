from flask import Flask
from flask_restx import reqparse, abort, Api, Resource, fields

app = Flask(__name__)
api = Api(app)

ESTOQUE = [{'codigo': 0, 'nome': 'Patinete', 'quantidade': 12, 'preco': 128.55},
           {'codigo': 1, 'nome': 'Bicicleta', 'quantidade': 12, 'preco': 49.89},
           {'codigo': 2, 'nome': 'Skate', 'quantidade': 12, 'preco': 89.99},]

def aborta_se_o_produto_nao_existe(codigo):
    if codigo not in [produto['codigo'] for produto in ESTOQUE]:
        abort(404, message="Produto {} não existe".format(codigo))

parser = reqparse.RequestParser()
parser.add_argument('codigo', type=int, help="Código do produto")
parser.add_argument('nome', type=str, required=True, help="Nome do produto")
parser.add_argument('quantidade', type=int, required=True, help="Quantidade do produto")
parser.add_argument('preco', type=float, required=True, help="Preço do produto")

campos_obrigatorios_para_atualizacao = api.model('Atualização estoque', {
    'quantidade': fields.Integer(required=True, description='Quantidade do produto'),
    'preco': fields.Float(required=True, description='Preço do produto'),
})

campos_obrigatorios_para_insercao = api.model('Inserção estoque', {
    'nome': fields.String(required=True, description='Nome do produto'),
    'quantidade': fields.Integer(required=True, description='Quantidade do produto'),
    'preco': fields.Float(required=True, description='Preço do produto'),
})

@api.route('/estoque/<codigo>')
@api.doc(params={'codigo': 'Código do produto'})
class Produto(Resource):

    @api.doc(responses={200: 'OK', 400: 'Erro de validação'})
    def get(self, codigo):
        aborta_se_o_produto_nao_existe(codigo)
        return ESTOQUE[codigo]

    @api.doc(responses={204: 'Estoque removido', 400: 'Erro de validação'})
    def delete(self, codigo):
        aborta_se_o_produto_nao_existe(codigo)
        del ESTOQUE[codigo]
        return '', 204

    @api.doc(responses={200: 'Estoque alterado com sucesso', 400: 'Erro na requisição'})
    @api.expects(campos_obrigatorios_para_atualizacao)
    def put(self, codigo):
        args = parser.parse_args()
        produto = {'codigo': codigo, 'nome': args['nome'], 'quantidade': args['quantidade'], 'preco': args['preco']}
        ESTOQUE[codigo] = produto
        return produto, 201

@api.route('/estoque')
class ListaProdutos(Resource):
    @api.doc(responses={200: 'OK', 400: 'Erro de validação'})
    def get(self):
        return ESTOQUE

    @api.doc(responses={201: 'Estoque criado com sucesso', 400: 'Erro na requisição'})
    @api.expect(campos_obrigatorios_para_insercao)
    def post(self):
        args = parser.parse_args()
        codigo = len(ESTOQUE)
        produto = {'codigo': codigo, 'nome': args['nome'], 'quantidade': args['quantidade'], 'preco': args['preco']}
        ESTOQUE.append(produto)
        return produto, 201

if (__name__ == '__main__'):
    app.run(debug=True)
