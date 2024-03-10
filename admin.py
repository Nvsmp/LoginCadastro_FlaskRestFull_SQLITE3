import sqlite3

con = sqlite3.connect('data_base.db')
cur = con.cursor()

cur.execute("SELECT * FROM usuarios")

for linha in cur.fetchall():
  print(linha)