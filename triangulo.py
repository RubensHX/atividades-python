# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/triangulo/1
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {
# "x" : "10",
# "y" : "21",
# "z" : "30"
# }

@app.route('/triangulo/1', methods=['POST'])
def teste_json():
    objeto_json = request.get_json()
    mensagem = ""

    # Verificar se o ojeto no formato JSON é NULL.
    if objeto_json is not None:
        if 'x' in objeto_json:
            x = int(objeto_json['x'])

        if 'y' in objeto_json:
            y = int(objeto_json['y'])
        
        if 'z' in objeto_json:
            z = int(objeto_json['z'])

    if (z < (x + y)) and ((x + z) > y) and ((y + z) > x): # 
        mensagem = 'Esses valores podem ser os comprimentos dos lados de um triangulo'
    else:
        mensagem = 'Esses valores não podem ser os comprimentos dos lados de um triangulo'

    return '''
        x informado: {}
        y informado: {}
        z informado: {}
        {}
        '''.format(x, y, z, mensagem)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)