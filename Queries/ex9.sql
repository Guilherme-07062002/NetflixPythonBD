-- Fazer uma pesquisa dos Vídeos pelo nome da Categoria;
select videos.nome from videos left join categorias on videos.id_categoria = categorias.id 
where categorias.nome = 'Educativo'; 
