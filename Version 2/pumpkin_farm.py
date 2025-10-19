# Code not completed,need a way to tell main page that carrot is low
def pumpkin_farm(world_size):
	trigger = True
	for i in range(get_world_size()):
#		quick_print("i = ",i)
		for j in range(get_world_size()):
#			quick_print("j = ",j)
			#harvest
			if can_harvest():
				harvest()
			#check water
			while get_water() < 0.8:
				if num_items(Items.Water) > 0:
					use_item(Items.water)
				else:
					break
			#plant pumpkin
			if num_items(Items.Carrot) >= world_size:
				if get_ground_type() == Grounds.Soil:
					plant(Entities.Pumpkin)
				else:
					till()
					plant(Entities.Pumpkin)
			else:
				trigger = False
				return trigger
		return trigger
			
			
			
			
			