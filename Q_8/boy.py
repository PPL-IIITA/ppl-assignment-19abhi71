class Boy:

	#initialising boy object with required attributes
	def __init__(self,name,attractiveness,intelligence,budget,minattreq,typ,status='S'):
		self.name=name
		self.attractiveness=attractiveness
		self.intelligence=intelligence
		self.budget=budget
		self.minattreq=minattreq
		self.typ=typ
		self.status=status

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