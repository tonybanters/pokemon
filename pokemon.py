"""
Author = @tonybanters
A pokemon tool to help beginners
"""
import pprint


#category means special vs physical vs other
ash_greninja = True



class Pokemon:
	def __init__(self , species , stats, type, ability, item, nature, moveset, level = 100, shiny = False):
		self.species = species
		self.stats = stats
		self.type = type
		self.ability = ability
		self.item = item
		self.nature = nature
		self.moveset = moveset
		self.level = level
		self.shiny = shiny

	def get_species(self):
		return self.species
	def get_stats(self) -> dict:
		return self.stats
	def get_type(self) -> list:
		return self.type
	def get_ability(self):
		return self.ability
	def get_item(self) -> str:
		return self.item
	def get_nature(self) -> str:
		return self.nature
	def get_moveset(self) -> list:
		return self.moveset
	def get_level(self) -> int:
		return self.level	

	def print_mon(self):
		print("{} @{}".format(self.get_species(),self.get_item()))
		pprint.pprint(self.stats)
		print("Types = {}".format(self.get_type()))
		print("Ability = {}".format(self.ability.get_name()))
		# print(self.ability.get_description())
		# print(self.ability.get_effect())
		print("Nature = {}".format(self.get_nature()))
		print("Moveset = {}".format(self.get_moveset()))
		



class Move:

	def __init__(
			self, 
			name, 
			type, 
			category, 
			description, 
			priority, 
			pp, 
			accuracy,
			power
			):
		self.name = name
		self.type = type
		self.category = category
		self.description = description
		self.priority = priority
		self.pp = pp
		self.accuracy = accuracy
		self.power = power
	def get_name(self):
		return self.name
	def get_type(self):
		return self.type
	def get_category(self):
		return self.category
	def get_description(self):
		return self.description
	def get_priority(self):
		return self.priority
	def get_pp(self):
		return self.pp
	def get_accuracy(self):
		return self.accuracy
	def get_power(self):
		return self.power

	def print_move(self):
		print(self.get_name())
		print(self.get_type())
		print(self.get_category())
		print(self.get_description())
		print("Priority = {}.".format(self.get_priority()))
		print("PP = {}".format(self.get_pp()))
		print("Accuracy = {}".format(self.get_accuracy()))
		print("Power = {}".format(self.get_power()))






# class Attack(Move):

# 	def __init__(self, name, type, category, description, priority, power):
# 		super().__init__(name, type, category, description, priority)
# 		self.power = power

# 	def get_power(self):
# 		return self.power
# surf.print_move()

class Ability:
	def __init__(self, name, description, effect = None):
		self.name = name
		self.description = description
		self.effect = effect
	def get_name(self):
		return self.name
	def get_description(self):
		return self.description
	def get_effect(self):
		return self.effect

agility = Move("Agility", "Psychic", "Other", "Raises the user's Speed by 2.", 0, 30, "--", "--")
surf = Move("Surf", "Water", "Special", "Hit's adjacent pokemon. Double damage on dive.", 0, 15, "100%", 120)
# print("\n---test---\n")
# print()
# print("Below we will print the agility move:\n")
# agility.print_move()
# print("\n")
# print("Now we will print Surf:\n")
# surf.print_move()
# print("\n")

# intimidate = Ability("Intimidate" , "Lower's enemy's Attack by 1.")


# # class Attack(Move):
# # 	def __init__(self, name, type):
# # 		super().__init__(name, type)


# pikamoves = [
# 	"Quick Attack",
# 	"Thunderbolt",
# 	"Volt Switch",
# 	"Thunder Wave"
# ]

# pikastats = {

# 	"HP"   : 35,
# 	"Atk"  : 55,
# 	"Def"  : 40,
# 	"SpA"  : 50,
# 	"SpD"  : 50,
# 	"Spe"  : 90
# }

# pikatype = ["Electric"]
# pikability = "Static"
# pikaitem = "Leftovers"

# pikachu = Pokemon("Pikachu", pikastats, pikatype, intimidate, pikaitem, "Jolly", pikamoves)
# # pikachu.name = "Pikachu"

# print("---\n")
# print("Now we will print the information for Pikachu.\n")
# pikachu.print_mon()




