import random

class PeopleAndObjects:
	
	def __init__(self):
		pass

class Boy(PeopleAndObjects):

	#initialising boy object with required attributes
	def __init__(self,name,attractiveness,intelligence,budget,minattreq,typ,status='S'):
		self.name=name
		self.attractiveness=attractiveness
		self.intelligence=intelligence
		self.budget=budget
		self.minattreq=minattreq
		self.typ=typ
		self.status=status

	try:
		#checks if boy can be paired with the girl
		def readytopair(self,girl):
			if self.budget>=girl.maintbudget and self.minattreq<=girl.attractiveness:
				return True
			return False
			
		#return current status of boy
		def currStatus(self):
			return self.status
			
		#changes status 
		def changeStatus(self):
			if self.status=='C':
				self.status='S'
			else:
				self.status='C'
	except SyntaxError:
		print('error in syntax')
	finally:
		pass


class Girl(PeopleAndObjects):
	status='S'

	#initialising girl object with required attributes
	def __init__(self,name,attractiveness,intelligence,maintbudget,criteria,typ,status='S'):
		self.name=name
		self.attractiveness=attractiveness
		self.maintbudget=maintbudget
		self.intelligence=intelligence
		self.criteria=criteria
		self.typ=typ
		self.status=status

	try:
		#checks if girl can be paired with the boy
		def readytopair(self,boy):
			if boy.budget<self.maintbudget or self.status=='C':
				return False
			return True
		#returns current status of girl
		def currStatus(self):
			return self.status

		#changes status 
		def changeStatus(self):
			if self.status=='C':
				self.status='S'
			else:
				self.status='C';
	except SyntaxError:
		print('problem with syntax')
	

class Gifts(PeopleAndObjects):


	util={'A':100,'B':75,'C':50,'D':20}

	def __init__(self,name,price,value,category):
		self.name=name
		self.price=price
		self.value=value
			
		try:
			if category=='Luxury':
				self.difficulty=random.randint(100)
		
			if category=='Utility':
				u=util.popitem()
				self.utilClass=u[0]
				self.utilVal=u[1];

		except SyntaxError:
			print('take care of syntax')
			
		
