import json

with open('moveset.json') as json_file:
	typechart = json.load(json_file)

with open("moves.json", "w") as f:
	json.dump(typechart, f, indent = 4)