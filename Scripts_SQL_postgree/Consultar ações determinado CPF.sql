SELECT ordem.ticket
	FROM cliente, ordem where cliente.id = ordem.cliente_id AND cliente.cpf='214.213.123-23'; 