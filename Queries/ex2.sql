-- Cadastrar / remover / atualizar usuario

-- Cadastrando usuario
insert into usuarios (login, senha, email, id_plano, data_inicio)
VALUES
('Jubileu', '5567', 'email@gmail.com', 2, now());

-- Removendo usuário
DELETE FROM usuarios WHERE id = 4;

-- Atualizar usuário 
UPDATE usuarios SET login = 5555 WHERE id = 1;
select * from usuarios;
