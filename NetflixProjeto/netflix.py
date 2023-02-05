import mysql.connector
from time import sleep


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
        create table IF NOT EXISTS planos (
	    id integer auto_increment,
        nome varchar(50),
        valor numeric(5, 2),
        primary key(id)
    )
        '''
        self.cursor.execute(tabela_planos)
        # Tabela de usuários
        tabela_usuarios = '''
        create table IF NOT EXISTS usuarios (
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
        create table IF NOT EXISTS videos (
        id integer auto_increment,
        nome varchar(255) not null,
        ano integer,
        primary key(id)
    )
        '''
        self.cursor.execute(tabela_videos)
        # Tabela de visualizações
        tabela_visualizacoes = '''
        create table IF NOT EXISTS visualizacoes (
        id_usuario integer not null,
        id_video integer not null,
        foreign key(id_usuario) references usuarios(id),
        foreign key(id_video) references videos(id)
    )
        '''
        self.cursor.execute(tabela_visualizacoes)
        # Tabela de categorias
        tabela_categorias = '''
        create table IF NOT EXISTS categorias (
        id integer auto_increment,
        nome varchar(50),
        primary key(id)
    )
        '''
        self.cursor.execute(tabela_categorias)

    # Metodos:

    def cadastrarPlano(self):
        sql = 'insert into planos (nome, valor) values (%s, %s)'
        print('-'*30)
        nomePlano = input('Informe o nome do plano: ')
        valorPlano = int(input('Informe o valor do plano: '))
        try:
            self.cursor.execute(sql, (nomePlano, valorPlano))
            self.conexao.commit()
        except:
            print('Algo deu errado, tente novamente...')
            sleep(3)
        else:
            print(f'Plano {nomePlano} cadastrado.')
            sleep(3)

    def cadastrarUsuario(self):
        sql = '''insert into usuarios (login, senha, email, id_plano, data_inicio)
        VALUES
        (%s, %s, %s, %s, now())'''
        print('-'*30)
        login = input('Informe o login: ')
        senha = int(input('Informe a senha: '))
        email = input('Informe o email: ')
        id_plano = int(input('ID do plano do usuário: '))
        try:
            self.cursor.execute(sql, (login, senha, email, id_plano))
            self.conexao.commit()
        except:
            print('Algo deu errado, tente novamente...')
            sleep(3)
        else:
            print(f'Usuário {login} cadastrado.')
            sleep(3)

    def cadastrarVideo(self):
        sql = 'insert into videos (nome, ano, id_categoria) VALUES (%s, %s, %s)'
        print('-'*30)
        nome = input('Informe o nome do vídeo: ')
        ano = int(input('Informe o ano do vídeo: '))
        id_categoria = int(input('Informe o id da categoria do vídeo: '))
        try:
            self.cursor.execute(sql, (nome, ano, id_categoria))
            self.conexao.commit()
        except:
            print('Algo deu errado, tente novamente...')
            sleep(3)
        else:
            print(f'Vídeo cadastrado.')
            sleep(3)

    def assistirVideo(self):
        sql = 'insert into visualizacoes(id_usuario, id_video) values (%s, %s)'
        print('-'*30)
        id_usuario = int(input('Informe o id do usuário que vai assistir: '))
        id_video = int(input(f'Id do video que será assistido: '))
        try:
            self.cursor.execute(sql, (id_usuario, id_video))
            self.conexao.commit()
        except:
            print('Algo deu errado, tente novamente...')
            sleep(3)
        else:
            print(f'O usuário {id_usuario} assistiu o video {id_video}.')
            sleep(3)
