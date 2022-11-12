# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/salario
@app.route('/salario', methods=['GET'])
def retornar_todos_os_produtos():
    salario_bruto = 0
    salario_liquido = 0

    if 'hora_normal' in request.headers:
        quantidade = request.headers['hora_normal']
        total = 40.00 * float(quantidade)
        normal = total

    if 'hora_extra' in request.headers:
        quantidade = request.headers['hora_extra']
        total = 50.00 * float(quantidade)
        extra = total

    salario_bruto = normal + extra
    salario_liquido = salario_bruto * 0.9

    return jsonify({'Salario Bruto': salario_bruto, 'Salario Liquido': salario_liquido})

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)