MATCH (c:Character)
WHERE c.name = $character_name
RETURN c