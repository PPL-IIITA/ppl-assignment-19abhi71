from boy import Boy
from girl import Girl
from gift import Gifts
from couples import Couple
from datetime import datetime
import operator
import random
import csv
import math
import sys

gifts=['essential','luxury','utility']
boys=['Ajit','Abhishek','Rahul','Tussank','Saurav','Tim','Joe','Jimmy','Leonardo','Tom','Eminem','Sam','Lucifer','Dante','Adam','Michael','Light','Kira','Walter']
girls=['Amanda','Guliston','Nina','Veronica','Sansa','Anjali','Pooja','Ankita','Neha','Anny','Ozge','Ecenaz','Jesse']
typ1=['miser','generous','geeks']
typ2=['choosy','normal','desperate']
crit=['most rich','most intelligent','most attractive']

commit=[]
B=[]
G=[]
boyslist=[]
girlslist=[]
couplesList=[]
giftsList=[]
daysForGifting=[]

t=10 #defined by programmer (can be changed)
for i in range(3,30,3):
	if t==0:
		break
	daysForGifting.append(i)
	t-=1

s1='-------------------Days for Gifting are:-------------------------------------------------'
commit.append(s1)
print(s1)
for item in daysForGifting:
	s1=item
	commit.append(s1)
	print(s1)

#testing utility
def utility():
	#generating a list named B of boy objects and boyslist with respective values of object for writing to csv
	for i in range(19):
		b=Boy(boys[i],random.randint(10,18),random.randint(12,24),random.randint(1,30),random.randint(5,25),random.choice(typ1))
		boyslist.append([b.name,b.attractiveness,b.intelligence,b.budget,b.minattreq,b.typ,b.status])
		B.append(b)

	#writing csv file

	with open("guys.csv","w") as h:
		writer=csv.writer(h,delimiter=',')
		writer.writerows(boyslist)

	#generating a list named G of girl objects and girlslist with respective values of object for writing to csv
	for i in range(13):
		g=Girl(girls[i],random.randint(10,18),random.randint(15,25),random.randint(1,26),random.choice(crit),random.choice(typ2))
		girlslist.append([g.name,g.attractiveness,g.intelligence,g.maintbudget,g.criteria,g.typ,g.status])
		G.append(g)

	#writing csv file
	with open("girls.csv","w") as f:
		writer=csv.writer(f,delimiter=',')
		writer.writerows(girlslist)

utility()

def findDates():
	for boy in B:
		for girl in G:
			#if boy and girls are both ready to pair with each other and are already not commited
			if boy.readytopair(girl) and girl.readytopair(boy) and boy.currStatus()=='S' and girl.currStatus()=='S':
				#change their status
				boy.changeStatus()
				girl.changeStatus()
				c=Couple(boy.name,boy.typ,girl.typ,girl.name,boy.budget,girl.maintbudget,boy.attractiveness,girl.attractiveness,boy.intelligence,girl.intelligence,0)
				couplesList.append(c)
				s1=boy.name+' is gonna date '+girl.name
				print(s1)
				commit.append(s1)
				break
findDates()


s1='-------------------Here starts the Valentine week of February:-------------------------------------------------'
commit.append(s1)


#making gift-basket

giftBasket=[]

gif=['Portable Charger','Sony Camera','earrings','Book','Chocolate','Teddy','Perfume','Cookies','Speakers','Purse','Bracelet','Novel','Game','earphones']
for item in gif:
	giftBasket.append(Gifts(item,random.randint(1,16),random.randint(1,11),random.choice(gifts)))

giftBasket.sort(key=operator.attrgetter('price'))

fate=[]

compatibleCouples={}  

#time to break-up after each gifting day

for item1 in daysForGifting:
	boysSingleAgain=[]
	girlsSingleAgain=[]
	happyCouples={}
	s1='-------------------On date '+str(item1)+', gifting process takes place as follows:---------------------------------'
	commit.append(s1)

	for c in couplesList:
	
		before=c.budget
		spent=0
		for item in giftBasket:
			if before<=0 or spent>=c.maintbudget:
				break
			before-=item.price
			c.priceTag.append(item.price)
			c.valueTag.append(item.value)
			spent+=item.price
			s1=c.bf+' gifts '+item.name+' '+c.gf
			commit.append(s1)
		
		#calculate happiness
		c.Cal(c.budget,spent)
		#dictionary of happiness with corresponding couples
		happyCouples.update({c:c.happiness})

	s1='-------------------Break-up period starts------------------------------------------------------------------------'
	commit.append(s1)
	cnt=0
	
	for k,v in happyCouples.items():
		if v<item1:
			boysSingleAgain.append(k.bf)
			girlsSingleAgain.append(k.gf)
			couplesList.remove(k)
			s1=k.bf +' and '+k.gf+' broke up! on date '+str(item1+1)
			print(s1)
			commit.append(s1)
			cnt+=1
	
	s1='-------------------Total '+str(cnt)+' couples broke up on date ' + str(item1+1)+'!-----------------------------------'
	print(s1)
	commit.append(s1)

	for item in boysSingleAgain:
		for b in B:
			if b.name==item:
				b.changeStatus()
				break

	for item in girlsSingleAgain:
		for g in G:
			if g.name==item:
				g.changeStatus()
				break

	s1='-------------------Patch-up period starts------------------------------------------------------------------------'
	print(s1)
	commit.append(s1)

	findDates()
	
		
#taking note of all commitments and gift exchanges with time stamps3

file=open("log.txt","w")
for item in commit:
	file.write(str(datetime.now()))
	file.write(" %s\n"%item)