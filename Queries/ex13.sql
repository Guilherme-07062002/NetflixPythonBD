-- Pesquisar a quantidade de Usuários ativos para cada Plano (Um Usuário é considerado ativo quando a sua mensalidade ainda não venceu);
select planos.id as id_plano, count(usuarios.id) as quantAtivos from usuarios left join planos on usuarios.id_plano = planos.id
where date_add(usuarios.data_inicio, interval 1 month) > now() group by(planos.id);
