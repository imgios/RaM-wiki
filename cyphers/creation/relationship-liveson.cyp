MATCH (c:Character), (l:Location)
	WHERE c.no IN l.residents
MERGE (c)-[:LIVES_ON]->(l);
