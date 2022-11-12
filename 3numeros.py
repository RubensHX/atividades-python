# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)
# http://127.0.0.1:5000/3numeros/1
# Aceita requisições com os métodos GET e POST.
# GET: gera um formulário em HTML para o usuário
# enviar dados para o servidor.
# POST: lê os dados enviados pelo usuário através
# do furmulário HTML.
@app.route('/3numeros/1', methods=['GET', 'POST'])
def teste_dados_formulario_html():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        a = request.form.get('num1')
        b = request.form.get('num2')
        c = request.form.get('num3')

        media = (float(a) + float(b) + float(c)) / 3
    
        a = int(a)
        b = int(b)
        c = int(c)

    
        if a > b and a > c:
            maior = a
        elif b > c:
            maior = b
        else:
            maior = c

        if a < b and a < c:
            menor = a
        elif  b < c:
            menor = b
        else:
            menor = c

        return '''<h1>Números: </h1>
              <h2>Menor: {}</h2>
              <h2>Maior: {}</h2>
              <h2>Média: {}</h2>'''.format(menor, maior, media)

    # Caso contrário, trata a requisição com método GET:
    return '''

    <form method="POST">
    <div><label>Numero 1: <input type="text"

    name="num1"></label></div>

    <div><label>Numero 2: <input type="text"

    name="num2"></label></div>

    <div><label>Numero 3: <input type="text"

    name="num3"></label></div>

    <input type="submit" value="Enviar">
    </form>'''

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)