MATCH (c:Character {no:$character_number})-[:APPEARS_IN]->(e:Episode)
RETURN e.episode
ORDER BY e.episode