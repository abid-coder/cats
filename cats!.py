class Cat(object): #cats and some of their functions
	"""docstring for Cat"""
	def __init__(self, name, age, num_of_whiskers, breed, position, cat_speed):
		self.speed = cat_speed                   # things that 
		self.name = name						 # make a
		self.age = age							 # cat a
		self.num_of_whiskers = num_of_whiskers   # cat
		self.breed = breed						 #
		self.position = position				 #
	def Meow(self): #meow!
		print("meow!")
	def chase_roomba(self, roomba, roomba_speed): # the arts of chasing roombas
		if roomba & cat_speed > roomba_speed: #boolean
			print("roomba chased sucsessfuly")
		elif roomba & roomba_speed >= cat_speed:
			print("roomba too fast")
		else:
			print("no roomba found")

the_squad = ["bob", "timothy", "chunky", "captian cat"] #the cats in the group

def get_squad():
	for memeber in the_squad: #prints all the cats in the squad
		print(name)

def eat_food(food): #how to eat food, by a cat
	num_of_food = food
	while num_of_food > 0:
		print("nom nom")
		num_of_food -= 1

C1 = Cat("bob", 3, 18, "Bengal", "cook", 13) #a description of
C2 = Cat("timothy", 2, 14, "British Shorthair", "chaser", 24) # 2 cats in the squad	
C2.chase_roomba(True, 17)
print(C1.name)		
class Owner_aka_servent(object):
	"""docstring for Owner_aka.servent"""
	def __init__(self, name, age, is_male):
		self.name = name
		self.age = age
		self.is_male = is_male
	def serve_master_cat():
		print("master cat served")
	def put_food(bowl_is_not_full, cat_is_hungry):
		if bowl_is_not_full & cat_is_hungry:
			print("food has been put")
		elif bowl_is_not_full & != cat_is_hungry:
			print("cat is not hungry")
		else cat_is_hungry & != bowl_is_not_full:
			print("bowl is full")
O1 = Owner_aka_servent("jim", 32, True)
O1.serve_master_cat