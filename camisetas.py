# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

produtos = [{'tamanho': 'pequenas', 'preco': 10.00},
            {'tamanho': 'medias', 'preco': 12.00},
            {'tamanho': 'grandes', 'preco': 15.00}]



# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    resp = produtos
    pequenas = 0
    medias = 0
    grandes = 0

    if 'pequenas' in request.headers:
        quantidade = request.headers['pequenas']
        total = 10.00 * float(quantidade)
        pequenas = total

    if 'medias' in request.headers:
        quantidade = request.headers['medias']
        total = 12.00 * float(quantidade)
        medias = total

    if 'grandes' in request.headers:
        quantidade = request.headers['grandes']
        total = 15.00 * float(quantidade)
        grandes = total

    resultado = pequenas + medias + grandes

    return jsonify({'Preço das grandes': grandes, 'Preço das medias': medias, 'Preço das pequenas': pequenas, 'total': resultado})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)