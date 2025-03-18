import mysql.connector
import datetime
# Importando classe que cria a conexao
from data.conexao import Conexao


class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        dataHora = datetime.datetime.today()

        # Cadastrando informações no banco de dados
        conexao = Conexao.criar_conexao()

        cursorDb = conexao.cursor()
        # Comando do sql que sera executado
        sql = """INSERT INTO tb_comentarios (nome, comentario, data_hora) 
                VALUES (%s, %s, %s)"""
        # Valores que serao inseridos no sql
        valores = (usuario, mensagem, dataHora)
        # Executando o comando (sql (comando), valores(valores))
        cursorDb.execute(sql, valores)
        # completando a inserção no banco de dados
        conexao.commit()
        # fechando a conexao
        conexao.close()
        cursorDb.close()
    
    def recuperar_mensagens():
        # Criar Conexao
        conexao = Conexao.criar_conexao()
        cursorDb = conexao.cursor(dictionary=True)
        # Codigo SQL
        sql = """select nome, comentario, cod_comentario, curtidas from tb_comentarios;"""
        # Executando o comando 
        cursorDb.execute(sql)
        # Recuperando os dados e guardando em uma variavel
        resultado = cursorDb.fetchall()
        # Fechando a conexao
        conexao.close()
        cursorDb.close()
        return resultado
    
# Teste
    
    def excluir_mensagem(codigo):
                # Cadastrando informações no banco de dados
        conexao = Conexao.criar_conexao()

        cursorDb = conexao.cursor()
        # Comando do sql que sera executado
        sql = """DELETE FROM tb_comentarios 
                WHERE cod_comentario = %s"""
        valor = (codigo,)
        # Executando o comando (sql (comando), valores(valores))
        cursorDb.execute(sql, valor)
        # completando a inserção no banco de dados
        conexao.commit()
        # fechando a conexao
        conexao.close()
        cursorDb.close()
        
    def add_likes(codigo):
        conexao = Conexao.criar_conexao()
        
        cursorDb = conexao.cursor()
        # Comando do sql que sera executado
        sql = """UPDATE     tb_comentarios
                SET curtidas = curtidas +1 
                WHERE cod_comentario = %s"""
        valor = (codigo,)
        # Executando o comando (sql (comando), valores(valores))
        cursorDb.execute(sql, valor)
        # completando a inserção no banco de dados
        conexao.commit()
        # fechando a conexao
        conexao.close()
        cursorDb.close()