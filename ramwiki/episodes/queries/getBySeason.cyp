MATCH (e:Episode)
WHERE e.episode STARTS WITH 'S0' + $season_number
RETURN e