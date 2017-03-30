from gift import Gifts
from couples import Couple
import random
import operator
from datetime import datetime

class GiftBasket:
	def __init__(self):
		print("Let's search for comitted boys:")

	#making gift-basket

	giftBasket=[]
	cat=['essential','luxury','utility']
	gifts=['Portable Charger','Sony Camera','earrings','Book','Chocolate','Teddy','Perfume','Cookies','Speakers','Purse','Bracelet','Novel','Game','earphones']
	for item in gifts:
		giftBasket.append(Gifts(item,random.randint(1,20),random.randint(1,20),random.choice(cat)))

	giftBasket.sort(key=operator.attrgetter('price'))



class GiftSelector1(GiftBasket):
	
	def __init__(self,couplesList):
		super(GiftSelector1,self).__init__()
		print('Gift Selector 1 starts now-------------------------------------------------')
		self.couplesList=couplesList
		self.commit=[]
		
	
	def assign(self):

		for c in self.couplesList:
			
			self.before=c.budget
			self.spent=0
			for Gifts.item in GiftBasket.giftBasket:
				if self.before<=0 or self.spent>=c.maintbudget:
					break
				self.before-=Gifts.item.price
				self.spent+=Gifts.item.price
				self.s1=str(c.bf)+' gifts '+str(Gifts.item.name)+' '+str(c.gf)+' of category: '+str(Gifts.item.category)
				self.commit.append(self.s1)

	#taking note of all commitments and gift exchanges with time stamps3
	def writ(self):

		file=open("log.txt","a+")
		for item in self.commit:
			file.write(str(datetime.now()))
			file.write(" %s\n"%item)
		file.close()



class GiftSelector2(GiftBasket):
	
	def __init__(self,couplesList):
		super(GiftSelector2,self).__init__()
		print('Gift Selector 2 starts now-------------------------------------------------')
		self.couplesList=couplesList
		self.commit=[]
		


	def assign(self):
				
		for c in self.couplesList:
			self.a=[]
			self.before=c.budget
			self.spent=0
			self.cnt=1
			for Gifts.item in GiftBasket.giftBasket:
				if self.before<=0 and self.cnt>3:
					break
				if Gifts.item.category not in self.a or self.cnt>3:
					self.before-=Gifts.item.price
					self.s1=str(c.bf)+' gifts '+str(Gifts.item.name)+' '+str(c.gf)+' of category: '+str(Gifts.item.category)
					self.commit.append(self.s1)
					self.a.append(Gifts.item.category)
					self.cnt+=1
	#taking note of all commitments and gift exchanges with time stamps3

	def writ(self):

		file=open("log.txt","a+")
		for item in self.commit:
			file.write(str(datetime.now()))
			file.write(" %s\n"%item)
		file.close()