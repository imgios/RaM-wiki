CALL apoc.load.json("file:///characters.json")
YIELD value
UNWIND value.results AS characters
MERGE (c:Character {
	no:			characters.id,
	name:		coalesce(characters.name, 'Unknown'),
	status:		coalesce(characters.status, 'Unknown'),
	species:	coalesce(characters.species, 'Unknown'),
	type:		coalesce(characters.type, 'Unknown'),
	gender:		coalesce(characters.gender, 'Unknown'),
	origin:		coalesce(characters.origin.name, 'Unknown'),
	location:	coalesce(characters.location.name, 'Unknown'),
	image:		coalesce(characters.image, 'N/A'),
	episode:	apoc.convert.toIntList(characters.episode)
});