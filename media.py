# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/media/1?nota1=10&nota2=7&nota3=8
@app.route('/media/1')
def teste_query_string_1_agurmento_get():
  nota1 = request.args.get('nota1')
  nota2 = request.args.get('nota2')
  nota3 = request.args.get('nota3')
  mensagem = ""

  media = (float(nota1) + float(nota2) + float(nota3)) / 3

  if media >= 0 and media < 3:
    mensagem = "<h1 style='color:red'>REPROVADO</h1>"
  elif media >= 3 and media < 7:
    mensagem = "<h1 style='color:yellow'>EXAME</h1>"
  elif media >= 7 and media <= 10:
    mensagem = "<h1 style='color:green'>APROVADO</h1>"
  
  return '''<h1>Notas: </h1>
            <h2>1: {}</h2>
            <h2>2: {}</h2>
            <h2>3: {}</h2>
            <h2>Média: {}</h2>
            
            {}'''.format(nota1, nota2, nota3, media, mensagem)

if __name__ == '__main__':
  app.run(debug = True, port = 5000)