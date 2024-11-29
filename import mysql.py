import mysql.connector #biblioteca permite conexão do código com o BD
user="root" #variáveis puxando valores do BD
senha=""
host="localhost"
database="lanchonete"

#tentará puxar a conexão com o DB
try:
    conexao = mysql.connector.connect( #comando de puxar a conexão
        host=host,#igualando os parâmetros com as variáveis acima
        password=senha,
        user=user,
        database=database
    )
    if conexao.is_connected(): #testa se tem conexão
        print("Conexão estabelecida!")

        cursor = conexao.cursor() #cria um cursor

        cursor.execute("SHOW TABLES") #chama um comando de BD
        retorno = cursor.fetchall() #varíavel que iguala o cursor acima

        print("Banco de dados:",retorno)

except mysql.connector.Error as e: #caso falhe, isso acontece
    print(f"Erro ao conectar com o BD: {e}")

finally: 
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")