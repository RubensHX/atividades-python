# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)
# http://127.0.0.1:5000/imc/1
# Aceita requisições com os métodos GET e POST.
# GET: gera um formulário em HTML para o usuário
# enviar dados para o servidor.
# POST: lê os dados enviados pelo usuário através
# do furmulário HTML.
@app.route('/imc/1', methods=['GET', 'POST'])
def teste_dados_formulario_html():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        peso = request.form.get('peso')
        altura = request.form.get('altura')
        mensagem = ""

        imc = float(peso) / (float(altura) * float(altura))
    
        if imc < 18.5:
            mensagem = "Você está abaixo do peso."
        elif imc > 18.5 and imc <= 24.9:
            mensagem = "Você está no peso ideial."
        elif imc > 25.0 and imc <= 29.9:
            mensagem = "Você está levimente acima do peso."
        elif imc > 29.9 and imc <= 34.9:
            mensagem = "Você está com Obesidade grau I."
        elif imc > 34.9 and imc <= 39.9:
            mensagem = "Você está Obesidade grau II (Severa)."
        elif imc > 34.9 and imc <= 39.9:
            mensagem = "Você está Obesidade grau III (Mórbida)."

        return '''<h1>IMC: </h1>
              <h2>Seu IMC: {}</h2>
              <h2>{}</h2>'''.format(imc, mensagem)

    # Caso contrário, trata a requisição com método GET:
    return '''

    <form method="POST">
    <div>
        <label>Peso: <input type="text" name="peso"></label>
    </div>

    <div>
        <label>Altura: <input type="text" name="altura"></label>
    </div>

    <input type="submit" value="Enviar">
    </form>'''

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)