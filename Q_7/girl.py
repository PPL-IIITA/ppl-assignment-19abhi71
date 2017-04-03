class Girl:
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
			self.status='C'