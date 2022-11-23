import mysql.connector

# conexao com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='leone16tuf@',
    database='banco',


)
cursor = conexao.cursor()


def Cadastro(CPF, Nome, Senha, Agencia, Conta, RG, SaldoConta):
    Pessoa = [CPF, Nome, Senha, Agencia, Conta, RG, SaldoConta]
    comando = "INSERT INTO pessoa (CPF, Nome, Senha, Agencia, Conta, RG, SaldoConta) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(comando, Pessoa)


def Verificacao(CPF, senha):
    comando = f'SELECT Senha FROM banco.pessoa where CPF={CPF};'
    cursor.execute(comando)
    Dado = cursor.fetchall()
    if senha != Dado[0][0]:
        print('sua senha esta errada!')
    else:
        print('bem vindo ao seu banco')


def Consulta(nome):
    comando = f'SELECT * FROM banco.pessoa where Nome="{nome}";'
    cursor.execute(comando)
    Dados = cursor.fetchall()
    print(Dados)


#Consulta('Leone')
#Cadastro(735335, 'NOME', 333, 223125, 21312, 3459932, 1288723)
