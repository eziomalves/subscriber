
import psycopg
import IQAr

def salvar_indice(data):
    conexao = inicia_conexao()
    mycursor = conexao.cursor()
    mycursor.execute("SELECT c_mp10, c_mp25 FROM smqar_concentracao WHERE data>=(%s) ORDER BY data ASC",[data])

    #pegando todos os dados retornados para data selecionada
    concentracoes = mycursor.fetchall()
    #Verifica se existe algum registro na tabela
    if mycursor.rowcount>0:
      #Calcula o média das concentrações
      soma_mp10 = 0
      soma_mp25 = 0

      for concentracao in concentracoes:
        soma_mp10 += float(concentracao[0])
        soma_mp25 += float(concentracao[1])

      media_mp10 = soma_mp10/mycursor.rowcount
      media_mp25 = soma_mp25/mycursor.rowcount

      #Cálculo do Indice e arredondamento
      indice_mp10 = round(IQAr.MP10(media_mp10))
      indice_mp25 = round(IQAr.MP25(media_mp25))

      #verifica o maior indice
      maior_indice = indice_mp10 if indice_mp10 > indice_mp25 else indice_mp25 
      #classificação
      classificacao = IQAr.classificacao(maior_indice)

      #salva o índice no banco de dados
      mycursor.execute("INSERT INTO smqar_indice (data, indice_mp25, indice_mp10, classificacao) VALUES (%s, %s, %s, %s)", [data, indice_mp25, indice_mp10, classificacao])
      conexao.commit()
      mycursor.close()
      conexao.close()

def salvar_concentracao(dados, data):
    conexao = inicia_conexao()
    mycursor = conexao.cursor()
    mycursor.execute("INSERT INTO smqar_concentracao (data, c_mp10, c_mp25) VALUES (%s, %s, %s)",[data, dados["MP10"],dados["MP25"]])
    conexao.commit()
    mycursor.close()
    conexao.close()

def inicia_conexao():
    #dados de conexão com o mysql
    try:
        conexao = psycopg.connect(
                        host='localhost',
                        user='smqar_user',
                        password='FXE-82au',
                        dbname='smqar_banco',
                        port='5432'
                    )
        return conexao

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

