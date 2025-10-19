def carrot_farm(world_size):
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
			#plant carrot
			if num_items(Items.Hay) >= world_size and num_items(Items.Wood) >= world_size :
				if get_ground_type() == Grounds.Soil:
					plant(Entities.Carrot)
				else:
					till()
					plant(Entities.Carrot)
			#plant hay
			elif num_items(Items.Hay) < world_size :
				if get_ground_type() == Grounds.Soil:
					till()
			#plant wood
			elif num_items(Items.Wood) < world_size :
				plant(Entities.Bush)
			#for debugging
			else:
				quick_print("Something Wrong")
			#check for unlocking
			move(North)
		move(East)
	return
		