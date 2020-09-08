MATCH (c:Character)
WHERE c.name =~ '(?i).*' + $search_name + '.*' 
RETURN c