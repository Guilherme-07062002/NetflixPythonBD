-- Pesquisar qual o faturamento do mês atual da Plataforma de Stream. O faturamento é calculado através 
-- do somatório do valor da assinatura de todos os Usuários que estão com o pagamento da Assinatura em dia.
select sum(valor) from usuarios left join planos on usuarios.id_plano = planos.id 
where date_add(usuarios.data_inicio, interval 1 month) > now();

