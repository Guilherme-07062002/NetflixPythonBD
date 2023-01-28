import mysql.connector


# Criando classe Netflix
class Netflix:
    def __init__(self):
        conf = {
            "host": "localhost",
            "user": "gui",
            "password": "12345"
        }
        # Estabelecendo conexão com o banco de dados
        self.conexao = mysql.connector.connect(**conf)
        self.cursor = self.conexao.cursor()

        # Criando base de dados
        sql_criarBanco = '''CREATE DATABASE IF NOT EXISTS netflix'''
        self.cursor.execute(sql_criarBanco)
        self.cursor.execute('USE netflix')

        # Criando tabelas

        # Tabela de planos
        tabela_planos = '''
        create table planos (
	    id integer auto_increment,
        nome varchar(50),
        valor numeric(5, 2),
        primary key(id)
    )
        '''
        self.cursor.execute(tabela_planos)
        # Tabela de usuários
        tabela_usuarios = '''
        create table usuarios (
        id integer auto_increment,
        login varchar(20) not null,
        senha varchar(10) not null,
        email varchar(50) not null,
        id_plano integer not null,
        data_inicio datetime not null,
        foreign key(id_plano) references planos(id),
        primary key (id),
        unique(login)
    )
        '''
        self.cursor.execute(tabela_usuarios)
        # Tabela de videos
        tabela_videos = '''
        create table videos (
        id integer auto_increment,
        nome varchar(255) not null,
        ano integer,
        primary key(id)
    )
        '''
        self.cursor.execute(tabela_videos)
        # Tabela de visualizações
        tabela_visualizacoes = '''
        create table visualizacoes (
        id_usuario integer not null,
        id_video integer not null,
        foreign key(id_usuario) references usuarios(id),
        foreign key(id_video) references videos(id)
    )
        '''
        self.cursor.execute(tabela_visualizacoes)
        # Tabela de categorias
        tabela_categorias = '''
        create table categorias (
        id integer auto_increment,
        nome varchar(50),
        primary key(id)
    )
        '''
        self.cursor.execute(tabela_categorias)
