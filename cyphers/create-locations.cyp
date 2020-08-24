CALL apoc.load.json("file:///locations.json")
YIELD value
UNWIND value.results AS location
MERGE (l:Location {
	no:			location.id,
	name:		coalesce(location.name, 'Unknown'),
	type:		coalesce(location.type, 'Unknown'),
	dimension:	coalesce(location.dimension, 'Unknown'),
	residents:	coalesce(apoc.convert.toIntList(location.residents), 'Unknown')
});