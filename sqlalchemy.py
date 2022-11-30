from flask import Flask
from flask_restx import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/empresa'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class FolhaDePagamento(db.Model):
    __tablename__ = 'folha_de_pagamento'
    cpf = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    horas_trabalhadas = db.Column(db.Float)
    valor_da_hora = db.Column(db.Float)

    def __init__(self, cpf, nome, horas_trabalhadas, valor_da_hora):
        self.cpf = cpf
        self.nome = nome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_da_hora = valor_da_hora

    def __create__(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self) -> str:
        return f'Folha de pagamento do cpf: {self.cpf, self.nome, self.horas_trabalhadas, self.valor_da_hora}'

class FolhaDePagamentoSchema(ma.Schema):
    class Meta:
        model = FolhaDePagamento
        sqla_session = db.session
    
    cpf = fields.String()
    nome = fields.String(required=True)
    horas_trabalhadas = fields.Float(required=True)
    valor_da_hora = fields.Float(required=True)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('cpf', type=int, help="cpfentificador do produto")
parser.add_argument('nome', type=str, required=True, help="Nome do produto")
parser.add_argument('horas_trabalhadas', type=float, required=True, help="Horas trabalhadas")
parser.add_argument('valor_da_hora', type=float, required=True, help="Valor da hora")


class Estoque(db.Model) :
    __tablename__ = 'estoque'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)

    def __init__(self, id, nome, quantidade, valor):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def __create__(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self) -> str:
        return f'Estoque do id: {self.id, self.nome, self.quantidade, self.valor}'

class EstoqueSchema(ma.Schema):
    class Meta:
        model = Estoque
        sqla_session = db.session
    
    id = fields.Integer()
    nome = fields.String(required=True)
    quantidade = fields.Integer(required=True)
    valor = fields.Float(required=True)

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help="identificador do produto")
parser.add_argument('nome', type=str, required=True, help="Nome do produto")
parser.add_argument('quantidade', type=int, required=True, help="Quantidade do produto")
parser.add_argument('valor', type=float, required=True, help="Valor do produto")