# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify

# Criar o objeto Flask app:
app = Flask(__name__)

produtos = [{'codigo': 1, 'produto': 'Cachorro Quente', 'preco': 12.00},
            {'codigo': 2, 'produto': 'Sanduiche', 'preco': 23.89},
            {'codigo': 3, 'produto': 'Pastel', 'preco': 3.98},
            {'codigo': 4, 'produto': 'Refrigerante', 'preco': 5.72},
            {'codigo': 5, 'produto': 'Suco', 'preco': 4.35}]

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    return jsonify({'produtos': produtos})

# http://127.0.0.1:5000/produtos/1
@app.route('/produtos/<int:codigo>', methods=['GET'])
def retornar_dados_do_produto_informado(codigo):
    resp = {'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            resp = produto
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/5/misto/45.67
@app.route('/produtos/<int:codigo>/<string:produto>/<float:preco>', methods=['POST'])
def inserir_produto(codigo, produto, preco):
    produtos.append({'codigo': codigo, 'produto': produto, 'preco': preco})
    return jsonify({'codigo': codigo, 'produto': produto, 'preco': preco})

# # http://127.0.0.1:5000/produtos/1/misto/10.00
@app.route('/produtos/<int:codigo>/<string:produto>/<float(signed=True):preco>',
methods=['PATCH'])
def alterar_produto(codigo, produto, preco):
    resp = {'produto': '', 'preco': None}
    for item in produtos:
        if item['codigo'] == codigo:
            item['produto'] = produto 
            if preco < 0: 
                item['preco'] = preco * -1
            else:
                item['preco'] = preco
        resp = produtos
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/1/10.00
# http://127.0.0.1:5000/produtos/1/-10.00
@app.route('/produtos/<int:codigo>/<float(signed=True):preco>',
methods=['PATCH'])
def alterar_preco_do_produto(codigo, preco):
    resp = {'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            if preco < 0: 
                produto['preco'] = preco * -1
            else:
                produto['preco'] = preco
        resp = produtos
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/1/mistoquente
@app.route('/produtos/<int:codigo>/<string:produto>',
methods=['PATCH'])
def alterar_nome_do_produto(codigo, produto):
    resp = {'produto': '', 'produto': None}
    for item in produtos:
        if item['codigo'] == codigo:
           item['produto'] = produto
        resp = produtos 
    return jsonify(resp)

# http://127.0.0.1:5000/produtos/5
@app.route('/produtos/<int:codigo>', methods=['DELETE'])
def remover_produto(codigo):
    for i, produto in enumerate(produtos):
        if produto['codigo'] == codigo:
            del produtos[i]
    return jsonify({'produtos': produtos})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)