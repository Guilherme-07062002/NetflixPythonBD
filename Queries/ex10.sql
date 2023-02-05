-- Pesquisar quais as Categorias de Vídeo mais assistidas pelo Usuário. Apresentar o resultado em ordem decrescente;
select categorias.nome from (select id_categoria, count(videos.id_categoria) from visualizacoes
left join videos
on visualizacoes.id_video = videos.id
where id_usuario = 1
group by videos.id_categoria
order by(id_categoria) desc) as tabela1
left join categorias 
on tabela1.id_categoria = categorias.id;
