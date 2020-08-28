CALL apoc.load.json("file:///episodes.json")
YIELD value
UNWIND value.results AS episode
MERGE (e:Episode {
	no:			episode.id,
	name:		coalesce(episode.name, 'Unknown'),
	air_date:	coalesce(episode.air_date, 'Unknown'),
	episode:	coalesce(episode.episode, 'Unknown'),
	characters:	coalesce(apoc.convert.toIntList(episode.characters), 'Unknown')
});