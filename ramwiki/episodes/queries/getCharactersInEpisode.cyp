MATCH (c:Character {no:$character_number})-[:APPEARS_IN]->(e:Episode {episode:$episode_abbr})
RETURN c.name, c.no