from allIn import Boy,Girl,Gifts,PeopleAndObjects
from couples import Couple
from datetime import datetime
import operator
import random
import csv
import math

gifts=['essential','luxury','utility']
boys=['Ajit','Abhishek','Rahul','Tussank','Saurav','Tim','Joe','Jimmy','Leonardo','Tom','Eminem','Sam','Lucifer','Dante','Adam','Michael','Light','Kira','Walter']
newBoys=['Rob','Bob','Terry','Jason','Ford','Jack','Ellen','Ethan','Stephen','Robert','Dutch','Marshall','Toll','Frank','Rico','Han','Slim','Mason']
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
boysBudget=[]
percentageOfBudget=[0.75,0.5]
happyCouples={}

#testing utility

#generating a list named B of boy objects and boyslist with respective values of object for writing to csv
for i in range(19):
	b=Boy(boys[i],random.randint(10,100),random.randint(24,100),random.randint(50,5000),random.randint(6,50),random.choice(typ1))
	boyslist.append([b.name,b.attractiveness,b.intelligence,b.budget,b.minattreq,b.typ,b.status])
	B.append(b)
	boysBudget.append(b.budget)

#writing csv file
with open("guys.csv","w") as h:
	writer=csv.writer(h,delimiter=',')
	writer.writerows(boyslist)

#generating a list named G of girl objects and girlslist with respective values of object for writing to csv
for i in range(13):
	g=Girl(girls[i],random.randint(10,100),random.randint(26,100),random.randint(12,5000),random.choice(crit),random.choice(typ2))
	girlslist.append([g.name,g.attractiveness,g.intelligence,g.maintbudget,g.criteria,g.typ,g.status])
	G.append(g)

#making gift-basket

giftBasket=[]

gif=['Portable Charger','Sony Camera','earrings','Book','Chocolate','Teddy','Perfume','Cookies','Speakers','Purse','Bracelet','Novel','Game','earphones']
for item in gif:
	giftBasket.append(Gifts(item,random.randint(50,3500),random.randint(1,100),random.choice(gifts)))

giftBasket.sort(key=operator.attrgetter('price'))
	
#writing csv file
with open("girls.csv","w") as f:
	writer=csv.writer(f,delimiter=',')
	writer.writerows(girlslist)

#budgets are credited every month
def everyMonth():	
	i=0
	for boy in B:
		
		addNow=random.choice(percentageOfBudget)*boysBudget[i]
		boy.budget+=addNow
		for c in couplesList:
			if c.bf==boy.name:
				c.budget+=addNow
				break
		i+=1

#making couples
def makeCouples():
	for boy in B:
		for girl in G:
			#if boy and girls are both ready to pair with each other and are already not commited
			if boy.readytopair(girl) and girl.readytopair(boy) and boy.currStatus()=='S' and girl.currStatus()=='S':
				#change their status
				boy.changeStatus()
				girl.changeStatus()
				c=Couple(boy.name,boy.typ,girl.typ,girl.name,boy.budget,girl.maintbudget,boy.attractiveness,girl.attractiveness,boy.intelligence,girl.intelligence)
				couplesList.append(c)
				s1=boy.name+' proposed '+girl.name
				print(s1)
				commit.append(s1)
				break

j=0

while j<12:	

	#new boys are added to list
	
	b=Boy(random.choice(newBoys),random.randint(10,100),random.randint(24,100),random.randint(50,5000),random.randint(6,50),random.choice(typ1))
	B.append(b)
	boysBudget.append(b.budget)
	newBoys.remove(b.name)

	print('In month '+str(j+1)+" Money has reached every boys' accounts:-------------------------------------")
	#handler
	makeCouples()

	s1='Here starts the process of gift giving:--------------------------------------------------------------'
	commit.append(s1)

	happyCouples=happyCouples.fromkeys(happyCouples,0)# resetting dictionary values

	for c in couplesList:

		h1=0
		before=c.budget
		spent=0
		for item in giftBasket:
			if before<=0 and spent<c.maintbudget:  #breakup event triggered
				print(c.bf+' '+c.gf+' broke up due to less money spent! ')
				for boy in B:
					if c.bf==boy.name:
						boy.changeStatus()
						break
				for girl in G:
					if c.gf==girl.name:
						girl.changeStatus()
						break
				couplesList.remove(c)
				break
				
			if before<=0 or spent>=c.maintbudget: #gifting event trigerred
				break
			before-=item.price
			c.priceTag.append(item.price)
			c.valueTag.append(item.value)
			spent+=item.price
			s1=c.bf+' gifts '+item.name+' '+c.gf
			#print(s1)
			commit.append(s1)
		
		#calculate happiness
		c.Cal(c.budget,spent)
		h1=c.happiness
		
		#dictionary of happiness with corresponding couples
		happyCouples[c]=h1

	#patch-up of broken hearts
	makeCouples()
	
	for c in happyCouples.keys():
		if(happyCouples[c]<1000):  #breakup event trigerred
			print(c.bf+' and '+c.gf+' broke up!')
			for boy in B:
				if c.bf==boy.name:
					boy.changeStatus()
					break
			for girl in G:
				if c.gf==girl.name:
					girl.changeStatus()
					break
	#patch-up of broken hearts
	makeCouples()
			
	j+=1

	#start timer
	everyMonth()


#taking note of all commitments and gift exchanges with time stamps
file=open("log.txt","w")
for item in commit:
	file.write(str(datetime.now()))
	file.write(" %s\n"%item)

