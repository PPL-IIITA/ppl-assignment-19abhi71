import math
class Couple:

	def __init__(self,bf,bfType,gfType,gf,budget,maintbudget,bfatt,gfatt,bfint,gfint):
		self.bf=bf
		self.bfType=bfType
		self.gfType=gfType
		self.gf=gf
		self.budget=budget
		self.maintbudget=maintbudget
		self.bfatt=bfatt
		self.gfatt=gfatt
		self.bfint=bfint
		self.gfint=gfint

	priceTag=[]
	valueTag=[]
	happiness=0
	compatibility=0

	def Cal(self,before,spent):

		self.happiness=(before-spent)
		self.compatibility=(before-spent)+abs(self.bfatt-self.gfatt)+abs(self.bfint-self.gfint)
		
		if self.bfType=='miser':
			if self.gfType=='choosy':
				self.happiness+=math.log(sum(self.priceTag),2)			
			elif self.gfType=='normal':
				self.happiness+=sum(self.priceTag)+sum(self.valueTag)
			else:
				self.happiness+=(sum(self.priceTag))**2
		
		elif self.bfType=='generous':
			if self.gfType=='choosy':
				self.happiness+=math.log(sum(self.priceTag),2)
			elif self.gfType=='normal':
				self.happiness+=sum(self.priceTag)+sum(self.valueTag)
			else:
				self.happiness+=(sum(self.priceTag))**2
		
		else:
			if self.gfType=='choosy':
				self.happiness+=math.log(sum(self.priceTag),2)
				
			elif self.gfType=='normal':
				self.happiness+=sum(self.priceTag)+sum(self.valueTag)
			else:
				self.happiness+=(sum(self.priceTag))**2

		