import random

class Gifts:

	util={'A':100,'B':75,'C':50,'D':20} #utility class as key while utility value as value

	def __init__(self,name,price,value,category):
		self.name=name
		self.price=price
		self.value=value
		self.category=category
		
		if category=='Luxury':
			self.difficulty=random.randint(100)
		
		if category=='Utility':
			u=util.popitem()
			self.utilClass=u[0]
			self.utilVal=u[1]

	

