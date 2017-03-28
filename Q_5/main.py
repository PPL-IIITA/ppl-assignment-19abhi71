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

#testing utility

#generating a list named B of boy objects and boyslist with respective values of object for writing to csv
for i in range(19):
	b=Boy(boys[i],random.randint(10,100),random.randint(24,100),random.randint(50,5000),random.randint(6,50),random.choice(typ1))
	boyslist.append([b.name,b.attractiveness,b.intelligence,b.budget,b.minattreq,b.typ,b.status])
	B.append(b)

B.sort(key=lambda x:x.attractiveness) #ordered by attractiveness

#writing csv file

with open("guys.csv","w") as h:
	writer=csv.writer(h,delimiter=',')
	writer.writerows(boyslist)

#generating a list named G of girl objects and girlslist with respective values of object for writing to csv

girlsSortedByAttractiveness=[]
for i in range(13):
	g=Girl(girls[i],random.randint(10,100),random.randint(26,100),random.randint(12,5000),random.choice(crit),random.choice(typ2))
	girlslist.append([g.name,g.attractiveness,g.intelligence,g.maintbudget,g.criteria,g.typ,g.status])
	G.append(g)
	girlsSortedByAttractiveness.append(g)

G.sort(key=lambda x:x.maintbudget) #ordered by maintenance budget
girlsSortedByAttractiveness.sort(key=lambda x:x.attractiveness,reverse=True)

#writing csv file
with open("girls.csv","w") as f:
	writer=csv.writer(f,delimiter=',')
	writer.writerows(girlslist)

def findDates():	
	for i in range(0,30):
		if i%2==0:			
			for boy in B:
				for girl in girlsSortedByAttractiveness:
					#if boy and girls are both ready to pair with each other and are already not commited
					if boy.readytopair(girl) and girl.readytopair(boy) and boy.currStatus()=='S' and girl.currStatus()=='S':
						#change their status
						boy.changeStatus()
						girl.changeStatus()
						c=Couple(boy.name,boy.typ,girl.typ,girl.name,boy.budget,girl.maintbudget,boy.attractiveness,girl.attractiveness,boy.intelligence,girl.intelligence)
						couplesList.append(c)
						s1=boy.name+' is gonna date '+girl.name+" with girl's attraction value: "+str(girl.attractiveness)
						commit.append(s1)
						i+=1
						break
				if i%2!=0:
					break
				
		else:
			for girl in G:
				for boy in B:
					#if boy and girls are both ready to pair with each other and are already not commited
					if boy.readytopair(girl) and girl.readytopair(boy) and boy.currStatus()=='S' and girl.currStatus()=='S':
						#change their status
						boy.changeStatus()
						girl.changeStatus()
						c=Couple(boy.name,boy.typ,girl.typ,girl.name,boy.budget,girl.maintbudget,boy.attractiveness,girl.attractiveness,boy.intelligence,girl.intelligence)
						couplesList.append(c)
						s1=girl.name+' is gonna date '+boy.name
						commit.append(s1)
						i+=1
						break
				if i%2==0:
					break	
										
findDates()


s1='Here starts the Valentine week of February:-------------------------------------------------'
commit.append(s1)


#making gift-basket

giftBasket=[]

gif=['Portable Charger','Sony Camera','earrings','Book','Chocolate','Teddy','Perfume','Cookies','Speakers','Purse','Bracelet','Novel','Game','earphones']
for item in gif:
	giftBasket.append(Gifts(item,random.randint(50,3500),random.randint(1,100),random.choice(gifts)))

giftBasket.sort(key=operator.attrgetter('price'))

fate=[]
happyCouples={}


for c in couplesList:

	h1=0
	c1=0
	
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
	h1=c.happiness
	c1=c.compatibility
	z=(h1,c1)
	fate.append(z) #fate of relationship depends upon this

	#dictionary of happiness with corresponding couples
	happyCouples.update({(c.bf,c.gf):h1})  #storing tuple as key

	
#print k most happiest couples

k=3 #defined by programmer

fate.sort(key=lambda x:x[0],reverse=True)
s1=str(k)+' happiest couples are given below:--------------------------------------------------'
commit.append(s1)
print(s1)

hi=[x[0] for x in fate]
topk=hi[:k]
for item in topk:
	s1=list(happyCouples.keys())[list(happyCouples.values()).index(item)][0]
	s2=list(happyCouples.keys())[list(happyCouples.values()).index(item)][1]
	s3= s1+' and '+ s2+' with happiness value: '+str(item)
	commit.append(s3)
	print(s3)	
	
print('\n')

#taking note of all commitments and gift exchanges with time stamps3
file=open("log.txt","w")
for item in commit:
	file.write(str(datetime.now()))
	file.write(" %s\n"%item)
