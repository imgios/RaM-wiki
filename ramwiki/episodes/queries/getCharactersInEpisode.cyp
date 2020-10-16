MATCH (c:Character)-[:APPEARS_IN]->(e:Episode {no:$episode_number})
RETURN c.name, c.no