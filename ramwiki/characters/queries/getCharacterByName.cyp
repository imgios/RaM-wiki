MATCH (c:Character)
WHERE c.name = {characterName}
RETURN c