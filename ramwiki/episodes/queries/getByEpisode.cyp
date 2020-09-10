MATCH (e:Episode)
WHERE e.episode = $episode
RETURN e