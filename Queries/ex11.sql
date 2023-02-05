-- Pesquisar qual o Vídeo mais assistido em toda a plataforma de Stream;
select id_video , count(id_video) as views from visualizacoes 
group by(id_video) limit 1;
