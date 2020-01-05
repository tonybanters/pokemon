import math

def calc_stats(base, iv, ev, lvl):
	y2 = math.floor(ev/4)
	result = 5 + math.floor(((2*base + iv + y2) * lvl) / 100)
	return result

def calc_hp(base, iv, ev, lvl):
	y2 = math.floor(ev/4)
	result = 10 + lvl + math.floor(((2*base + iv + y2) * lvl) / 100)
	return result

print(calc_stats(35, 31, 252, 100))



basestats = {
		"spa" : 35,
		"spe" : 50,
		"def" : 5,
		"hp"  : 250,
		"atk" : 5,
		"spd" : 105
	}

evs_test = {
		"spa" : 0,
		"spe" : 0,
		"def" : 4,
		"atk" : 0,
		"spd" : 252,
		"hp"  : 252
	}

for stat in basestats.keys():
	if stat == "spa":
		print(evs_test["spa"])
		print(basestats[stat])

ivs = {
		"spa" : 31,
		"spe" : 31,
		"def" : 31,
		"hp"  : 31,
		"atk" : 31,
		"spd" : 31
	}


def calc_all_stats(basestats, evs, ivs, lvl):
	new_stats = {}
	for stat in basestats.keys():
		if stat != "hp":
			new_stat = calc_stats(basestats[stat], ivs[stat], evs_test[stat], lvl)
			new_stats[stat] = new_stat
		else:
			new_stat = calc_hp(basestats[stat], ivs[stat], evs_test[stat], lvl)
			new_stats[stat] = new_stat
	return new_stats

print(calc_all_stats(basestats, evs_test, ivs, lvl=100))




