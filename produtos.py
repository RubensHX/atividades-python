# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/produtos/1
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {"codigo" : "1"}

@app.route('/produtos/1', methods=['POST'])
def teste_json():
    objeto_json = request.get_json()
    mensagem = ""
    codigo = 0
    produto = ""
    preco = ""

    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'codigo' in objeto_json:
            codigo = int(objeto_json['codigo'])
    
    match codigo:
        case 1:
            produto = "Sapato"
            preco = "R$ 99,99"
        
        case 2:
            produto = "Bolsa"
            preco = "R$ 103,89"

        case 3:
            produto = "Camisa"
            preco = "R$ 49,98"

        case 4:
            produto = "Calça"
            preco = "R$ 89,72"

        case 5:
            produto = "Blusa"
            preco = "R$ 97,35"


    return '''
        codigo: {} | produto: {} | preco: {}
        '''.format(codigo, produto, preco)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)