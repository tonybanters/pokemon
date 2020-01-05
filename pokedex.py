import json
import operator
from collections import Counter
from pokemon import *
from natures import *

with open('dex.json') as json_file:
	dex = json.load(json_file)



overgrow = Ability("Overgrow", "Does stuff")
info = {
	"evs" : {
		"spa" : 252,
		"spe" : 252,
		"def" : 4
	},
	"nature" : natures["Modest"],
	"item" : "Choice Specs",
	"ability" : overgrow
}

def validate_evs(evs: dict) -> bool:
	validated = True
	total = sum(evs.values())
	# print(total)
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

def nature_modify(stats: dict, nature):
	stats [ nature.get_plus() ] = int(1.1 *stats[nature.get_plus()])
	stats [ nature.get_minus() ] = int(0.9*stats[nature.get_minus()])
	return stats



# print(dex['bulbasaur']['abilities'])
# print("Overgrow" in dex['bulbasaur']['abilities'].values())
# obj = add_evs_to_stats(dex['bulbasaur']['baseStats'], evs_test)
# print(dict(obj))

# print(add_evs_to_stats(dex['bulbasaur']['baseStats'], evs_test, operator.mul))



def create_mon_from_dex(dex: dict, info: dict, mon: str):
	mon = mon.lower()
	moveset = []
	if validate_evs(info['evs']) == False:
		print("Please validate your EVs.")
		return
	if info["ability"].get_name() not in dex[mon]['abilities'].values():
		return "{} cannot learn {}.".format(mon, info['ability'])
	stats = add_evs_to_stats(info["evs"], dex[mon]['baseStats'])
	stats = nature_modify(stats, info['nature'])
	pkmn = Pokemon(
		dex[mon]['species'],
		stats,
		dex[mon]['types'],
		info['ability'],
		info['item'],
		info['nature'],
		moveset		
		)
	return pkmn


def build_team_from_dex(mons: dict, dex: dict):
	team = []
	for key in mons.keys():
		team.append(create_mon_from_dex(dex, mons[key], key))

	return team


intimidate = Ability("Intimidate", "Lower's enemy attack by 1.")
landorus_info = {
	"evs" : {
		"atk" : 252,
		"spe" : 252,
		"def" : 4
	},
	"nature" : natures["Jolly"],
	"item" : "Choice Scarf",
	"ability" : intimidate
}

regenerator = Ability("Regenerator", "Heal's 1/2 of total HP on switch out.")
toxapex_info = {
	"evs" : {
		"spd" : 252,
		"hp" : 252,
		"def" : 4
	},
	"nature" : natures["Calm"],
	"item" : "Toxic Sludge",
	"ability" : regenerator
}
tangrowth_info = {
	"evs" : {
		"spd" : 252,
		"hp" : 252,
		"def" : 4
	},
	"nature" : natures["Calm"],
	"item" : "Assault Vest",
	"ability" : regenerator
}
natural_cure = Ability("Natural Cure", "Cure's status on switch-out.")
chansey_info = {
	"evs" : {
		"spd" : 252,
		"hp" : 252,
		"def" : 4
	},
	"nature" : natures["Calm"],
	"item" : "Eviolite",
	"ability" : natural_cure
}
unaware = Ability("Unaware", "This pokemon ignore's enemy boosts.")
clefable_info = {
	"evs" : {
		"spd" : 4,
		"hp" : 252,
		"def" : 252
	},
	"nature" : natures["Calm"],
	"item" : "Leftovers",
	"ability" : unaware
}
pure_power = Ability("Pure Power", "This Pokemon's Attack is doubled.")
medicham_mega_info = {
	"evs" : {
		"def" : 4,
		"spe" : 252,
		"atk" : 252
	},
	"nature" : natures["Jolly"],
	"item" : "Medichamite",
	"ability" : pure_power
}

tony_team = {
	"medichammega" : medicham_mega_info,
	"clefable" : clefable_info,
	"tangrowth" : tangrowth_info,
	"landorustherian" : landorus_info,
	"toxapex" : toxapex_info,
	"chansey" : chansey_info
}

main_team = build_team_from_dex(tony_team, dex)


for mon in main_team:
	mon.print_mon()
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