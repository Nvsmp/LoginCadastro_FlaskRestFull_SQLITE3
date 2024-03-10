import sqlite3

con = sqlite3.connect('data_base.db')
cursor = con.cursor()

#cursor.execute('DROP TABLE IF EXISTS usuario')

cursor.execute( "CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, login, senha)" )

cursor.execute('INSERT INTO usuarios (login, senha) VALUES ( ?, ?)',('admin', 'admin'))

con.commit()

resposta = cursor.execute('SELECT * FROM usuarios')
print(resposta.fetchall())
