import mysql.connector
from mysql.connector import errorcode
from functions import buy_book, show_table, show_table_books


try:
  con = mysql.connector.connect(host='127.0.0.1', database='livraria', user='root')
  print("Connection established")
  
  cursor = con.cursor

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = con.cursor()


while True:
  question = input('Deseja comprar um livro[s/n]?')
  if question == 'n':
        break
  
  show_table_books()
  buy_book()
  
con.commit()
cursor.close()
con.close()
print("Muito obg! :).")