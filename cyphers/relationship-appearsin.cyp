MATCH (c:Character), (e:Episode)
	WHERE c.no IN e.characters
MERGE (c)-[:APPEARS_IN]->(e);