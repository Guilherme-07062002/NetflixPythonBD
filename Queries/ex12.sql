-- Pesquisar o login de todos os Usuários que estão com o pagamento da assinatura atrasado;
select login from usuarios 
where date_add(data_inicio, interval 1 month) < now();
