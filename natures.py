"""This will be a list of natures, and how they affect EVS"""


natures = {
    "adamant": {
        "name": "Adamant",
        "plus": "atk",
        "minus": "spa"
    },
    "bashful": {
        "name": "Bashful",
        "plus": None,
        "minus": None
    },
    "bold": {
        "name": "Bold",
        "plus": "def",
        "minus": "atk"
    },
    "brave": {
        "name": "Brave",
        "plus": "atk",
        "minus": "spe"
    },
    "calm": {
        "name": "Calm",
        "plus": "spd",
        "minus": "atk"
    },
    "careful": {
        "name": "Careful",
        "plus": "spd",
        "minus": "spa"
    },
    "docile": {
        "name": "Docile",
        "plus": None,
        "minus": None
    },
    "gentle": {
        "name": "Gentle",
        "plus": "spd",
        "minus": "def"
    },
    "hardy": {
        "name": "Hardy",
        "plus": None,
        "minus": None
    },
    "hasty": {
        "name": "Hasty",
        "plus": "spe",
        "minus": "def"
    },
    "impish": {
        "name": "Impish",
        "plus": "def",
        "minus": "spa"
    },
    "jolly": {
        "name": "Jolly",
        "plus": "spe",
        "minus": "spa"
    },
    "lax": {
        "name": "Lax",
        "plus": "def",
        "minus": "spd"
    },
    "lonely": {
        "name": "Lonely",
        "plus": "atk",
        "minus": "def"
    },
    "mild": {
        "name": "Mild",
        "plus": "spa",
        "minus": "def"
    },
    "modest": {
        "name": "Modest",
        "plus": "spa",
        "minus": "atk"
    },
    "naive": {
        "name": "Naive",
        "plus": "spe",
        "minus": "spd"
    },
    "naughty": {
        "name": "Naughty",
        "plus": "atk",
        "minus": "spd"
    },
    "quiet": {
        "name": "Quiet",
        "plus": "spa",
        "minus": "spe"
    },
    "quirky": {
        "name": "Quirky",
        "plus": None,
        "minus": None
    },
    "rash": {
        "name": "Rash",
        "plus": "spa",
        "minus": "spd"
    },
    "relaxed": {
        "name": "Relaxed",
        "plus": "def",
        "minus": "spe"
    },
    "sassy": {
        "name": "Sassy",
        "plus": "spd",
        "minus": "spe"
    },
    "serious": {
        "name": "Serious",
        "plus": None,
        "minus": None
    },
    "timid": {
        "name": "Timid",
        "plus": "spe",
        "minus": "atk"
    }
}

class Nature:
	def __init__(self, name, plus = None, minus = None):
		self.name = name
		self.plus = plus
		self.minus = minus

	def get_name(self):
		return self.name
	def get_plus(self):
		return self.get_plus
	def get_minus(self):
		return self.get_minus

nature_list = []

for nature in natures.values():
	nature_list.append(Nature(nature['name'], nature['plus'], nature['minus']))
# for nat in nature_list:
# 	print (nat.get_name())