def bush_farm(world_size):
	for i in range(get_world_size()):
		quick_print("i = ",i)
		for j in range(get_world_size()):
			quick_print("j = ",j)
			#harvest
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			#check water
			while get_water() < 0.8:
				if num_items(Items.Water) > 0:
					use_item(Items.water)
				else:
					break
			move(North)
		move(East)
	return
	