import json
import operator
from collections import Counter
from pokemon import *

with open('dex.json') as json_file:
	dex = json.load(json_file)

overgrow = Ability("Overgrow", "Does stuff")
info = {
	"evs" : {
		"spa" : 252,
		"spe" : 252,
		"def" : 4
	},
	"nature" : "Modest",
	"item" : "Choice Specs",
	"ability" : overgrow
}

def validate_evs(evs: dict) -> bool:
	validated = True
	total = sum(evs.values())
	print(total)
	if total > 510 or total < 508:
		return False
	else:
		for val in evs.values():
			if val > 252:
				return False
	return validated

evs_test = {
		"spa" : 252,
		"spe" : 252,
		"def" : 4
	}

# print(validate_evs(evs_test))

def add_evs_to_stats(stats: dict, evs: dict):
	a , b = Counter(stats) , Counter(evs)
	return dict(a + b)

# print(dex['bulbasaur']['abilities'])
# print("Overgrow" in dex['bulbasaur']['abilities'].values())
# obj = add_evs_to_stats(dex['bulbasaur']['baseStats'], evs_test)
# print(dict(obj))

# print(add_evs_to_stats(dex['bulbasaur']['baseStats'], evs_test, operator.mul))



def create_mon_from_dex(dex: dict, info: dict, mon: str):
	mon = mon.lower()
	moveset = []
	if info["ability"].get_name() not in dex[mon]['abilities'].values():
		return "{} cannot learn {}.".format(mon, info['ability'])
	pkmn = Pokemon(
		dex[mon]['species'],
		add_evs_to_stats(info["evs"], dex[mon]['baseStats']),
		dex[mon]['types'],
		info['ability'],
		info['item'],
		info['nature'],
		moveset		
		)
	return pkmn

bulbasaur = create_mon_from_dex(dex, info, 'bulbasaur')
bulbasaur.print_mon()
def build_team_from_dex():
	pass

# print(json.dumps(dex['bulbasaur'], indent=4))

# with open("dex.json", "w") as outfile:
# 	json.dump(data, outfile, indent=4)
# # print(type(data))
# # print(json.dumps(data, indent=4))
# pika = data["pikachu"]
# dex = {
# 	"Pikachu" : Pokemon(
# 		pika['species'],
# 		pika['abilities']["H"],
# 		pika['baseStats'],
# 		pika['types'],
# 		"Leftovers",
# 		"Jolly",
# 		["Thunder", "Quick Attack", "Thunder Wave", "Agility"],
# 		)
# }

# print(json.dumps(dex, indent=4))
# # print(data["bulbasaur"])

# team = []
# team.append(data["garchomp"])
# team.append(data["smeargle"])
# for mon in team:
# 	print(json.dumps(mon, indent=4))