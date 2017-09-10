# 2 ways of finding key, pseudo code! (Code will not work for now.)

def look_for_key1(main_box):
	pile = main_box.make_a_pile_to_look_through()
	while pile is not empty:
		box = pile.grab_a_box()
		for item in box:
			if item.is_a_box():
				pile.append(item)
			elif item.is_a_key():
				print("열쇠를 찾았어요!")

def look_for_key2(box):
	for item in box:
		if item.is_a_box():
			look_for_key2(item)    # 반복!!
		elif item.is_a_key():
			print("열쇠를 찾았어요!")
