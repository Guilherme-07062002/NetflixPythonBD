drop database if exists netflix;
create database if not exists netflix;
use netflix;


drop table if exists visualizacoes;
drop table if exists usuarios;
drop table if exists planos;
drop table if exists videos;
drop table if exists categorias;

create table if not exists planos (
	id integer auto_increment,
    nome varchar(50),
    valor numeric(5, 2),
    primary key(id)
);

create table if not exists usuarios (
	id integer auto_increment,
    login varchar(20) not null,
    senha varchar(10) not null,
    email varchar(50) not null,
    id_plano integer not null,
    data_inicio datetime not null,
    foreign key(id_plano) references planos(id),
    primary key (id),
    unique(login)
);

create table if not exists categorias (
	id integer auto_increment,
    nome varchar(50),
    primary key(id)
);

create table if not exists videos (
	id integer auto_increment,
    nome varchar(255) not null,
    ano integer,
    id_categoria integer not null,
	foreign key(id_categoria) references categorias(id),
    primary key(id)
);

create table if not exists visualizacoes (
	id_usuario integer not null,
    id_video integer not null,
    foreign key(id_usuario) references usuarios(id),
    foreign key(id_video) references videos(id)
);

insert into planos (nome, valor) values 
('Basico', 10),
('Master', 30),
('Supreme', 80);

insert into usuarios (login, senha, email, id_plano, data_inicio)
VALUES
('Fulano', '1234', 'sdf@gmail.com', 3, now()),
('Beltrano', 'abcd', "juju@gmail.com", 2, '2023-01-12'),
('Cicrano', 'sdfsd', "kevin@gmail.com", 2, '2022-12-10'),
('Jurema', 'oioi', "seila@gmail.com", 2, '2022-12-08'),
('Jubileu', 'olaoi', "email@gmail.com", 2, '2022-01-20');

insert into categorias (nome) VALUES 
('Educativo'),
('VideoAula');

insert into videos (nome, ano, id_categoria) 
VALUES 
('Video 1', 2023, 1),
('Video 2', 2018, 2),
('Video 3', 2016, 1);

insert into visualizacoes(id_usuario, id_video)
VALUES
(1, 1), 
(1, 3), 
(1, 2),
(2, 1);
