drop database if exists pobreflix;
create database if not exists pobreflix;

use pobreflix;

create table planos (
	id integer auto_increment,
    nome varchar(50),
    valor numeric(5, 2),
    primary key(id)
);

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
);

create table videos (
	id integer auto_increment,
    nome varchar(255) not null,
    ano integer,
    primary key(id)
);

create table visualizacoes (
	id_usuario integer not null,
    id_video integer not null,
    foreign key(id_usuario) references usuarios(id),
    foreign key(id_video) references videos(id)
);

create table categorias (
	id integer auto_increment,
    nome varchar(50),
    primary key(id)
);


insert into planos (nome, valor) values 
('Basico', 10),
('Master', 30),
('Supreme', 82.35);

insert into usuarios (login, senha, email, id_plano, data_inicio)
VALUES
('Heribert', '1234', 'sdf@gmail.com', 3, now()),
('Juliany', 'abcd', "juju@gmail.com", 2, '2023-01-12'),
('Kevin', 'sdfsd', "kevin@gmail.com", 2, '2022-12-10');

select * from usuarios;
