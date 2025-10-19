#Dict of Entities and Items
def items_pick():
	items_pick = {
			Entities.Grass:Items.Hay,
			Entities.Tree:Items.Wood,
			Entities.Bush:Items.Wood,
			Entities.Carrot:Items.Carrot,
			Entities.Pumpkin:Items.Pumpkin,
			Entities.Cactus:Items.Cactus,
			Entities.Sunflower:Items.Power,
		}
	return items_pick 
	
	
	
#List of upgradable unlocks
def unlock_list():	
	unlock_list = [
			Unlocks.Speed,
			Unlocks.Grass,
			Unlocks.Expand,
			Unlocks.Carrots,
			Unlocks.Watering,
			Unlocks.Trees,
			Unlocks.Fertilizer,
			Unlocks.Pumpkins,
			Unlocks.Mazes,
			Unlocks.Cactus,
			Unlocks.Polyculture,
			Unlocks.Megafarm,
			Unlocks.Dinosaurs,
		]
	return unlock_list

#Upgradable unlocks with their max levels
def unlock_level():
	level_unlock = {
		Unlocks.Speed:5,
		Unlocks.Grass:10,
		Unlocks.Expand:9,
		Unlocks.Carrots:10,
		Unlocks.Watering:9,
		Unlocks.Trees:10,
		Unlocks.Fertilizer:4,
		Unlocks.Pumpkins:10,
		Unlocks.Mazes:6,
		Unlocks.Cactus:6,
		Unlocks.Polyculture:5,
		Unlocks.Megafarm:5,
		Unlocks.Dinosaurs:6,
	}
	
	return level_unlock 

def unlock_dict():	
	unlock_dict = {
				Items.hay:[Unlocks.Speed, Unlocks.Trees],
				Items.Wood:[Unlocks.Carrots, Unlocks.Watering, Unlocks.Fertilizer],
				Items.Carrot:Unlocks.Pumpkins, 
				Items.Pumpkin:[Unlocks.Expand, Unlocks.Cactus],
				Items.Cactus:[Unlocks.Mazes, Unlocks.Dinosaurs],
				Items.Bone:Unlocks.Polyculture,
				Items.Gold:Unlocks.Megafarm,
			}
	return unlock_dict 
		
def inventory_dict():
	inventory_list = {
		Items.Hay:0,
		Items.Wood:0,
		Items.Carrot:0,
		Items.Pumpkin:0,
		Items.Cactus:0,
		Items.Power:0,
		#Items.Bone:0,
		}
	return inventory_list

def items_list():
	items_list = [
		Items.Hay,
		Items.Wood,
		Items.Carrot,
		Items.Pumpkin,
		Items.Cactus,
		Items.Power,
		#Items.Bone,
		]
	return items_list

	
		
		