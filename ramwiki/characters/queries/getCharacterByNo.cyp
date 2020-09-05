MATCH (c:Character)
WHERE c.no = $character_number
RETURN c