SELECT cliente.nome, cliente.cpf, ordem.ticket, ordem.valor_compra, ordem.quantidade_compra, data_compra, cliente_id
	FROM cliente, ordem where cliente.id = ordem.cliente_id; 