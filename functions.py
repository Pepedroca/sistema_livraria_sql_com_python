import mysql.connector
from mysql.connector import errorcode
import random

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
  


# functions extras
def generate_cpf(self):                                                        
    cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                                
    for _ in range(2):                                                          
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                
        cpf.append(11 - val if val > 1 else 0)                                  
                                                                                
    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

def generate_cnpj(self):                                                       
    def calculate_special_digit(l):                                             
        digit = 0                                                               
                                                                                
        for i, v in enumerate(l):                                               
            digit += v * (i % 8 + 2)                                            
                                                                                
        digit = 11 - digit % 11                                                 
                                                                                
        return digit if digit < 10 else 0                                       
                                                                                
    cnpj =  [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]             
                                                                                
    for _ in range(2):                                                          
        cnpj = [calculate_special_digit(cnpj)] + cnpj                           
                                                                                
    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])
# ================================================================
def show_table():
    tabela = input('Qual tabela voce deseja mostrar [livro, cliente_compra_livro, editora, cliente, login]: ')
    cursor.execute(f'SELECT * FROM {tabela}')
    rows = cursor.fetchall()
    print(rows)
    
    
    
def show_table_books():
    cursor.execute(f'SELECT * FROM livro')
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]}\nNome: {row[1]}\nGenero: {row[2]}\nQuantidade: {row[5]}')
        print('=' * 30)
    
def buy_book():
    id = int(input('Por favor selecione o ID do livro para comprar: '))
    nome = input('Nome:')
    sobrenome = input('Sobrenome: ')
    telefone = input('Seu telefone: ')
    cpf = input('Seu cpf: ')
    dados = (nome, sobrenome,telefone, cpf, int(id))
    cursor.execute('INSERT INTO cliente (`nome`,`sobrenome`, `telefone`, `cpf`, `compra`) values ( %s, %s, %s, %s, %s);', dados)
    con.commit()
    




if __name__ == '__main__':
    print(generate_cpf())
    print(generate_cnpj)