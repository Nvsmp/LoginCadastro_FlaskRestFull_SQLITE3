from flask import Flask
from flask_restful import Api, Resource
import sqlite3
from decouple import config

# FLASK RESTFUL
app = Flask(__name__)
api = Api(app)


# FUNCOES
# CONFERE SE O LOGIN JA ESTA NO SISTEMA
def no_sistema(login):
  con = sqlite3.connect('data_base.db')
  cursor = con.cursor()
  cursor.execute("SELECT * FROM usuarios WHERE login=?", (login, ))
  if cursor.fetchone() is None:
    return False
  else:
    return True


# CONFERE SE A SENHA ESTA CORRETA
def senha_correta(login, senha):
  if no_sistema(login):
    con = sqlite3.connect('data_base.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE login=? AND senha=?",
                   (login, senha))
    result = cursor.fetchone()
    #print(result)
    #print(f" R[1] == { result[1] } /n R[2] == { result[2] } ")
    if result != None and result[2] == senha:
      return True
    else:
      return False
  else:
    return False


# CADASTRA USUARIO
def cadastrar_usuario(login, senha):
  if no_sistema(login):
    return False
  else:
    con = sqlite3.connect('data_base.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO usuarios (login, senha) VALUES ( ?, ?)',
                   (login, senha))
    con.commit()
    return True


#######################################################################7


# SISTEMA DE CADASTRO E LOGIN #
class LoginRegister(Resource):
  # LOGIN
  def get(self, login, senha):
    return senha_correta(login, senha)

  # CADASTRO
  def post(self, login, senha):
    return cadastrar_usuario(login, senha)

api.add_resource(LoginRegister, f"/{config('link_api_3')}/<login>,<senha>")

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', port=8080)
