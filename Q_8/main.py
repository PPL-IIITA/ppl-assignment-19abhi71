from boy import Boy
from girl import Girl
from gift import Gifts
from couples import Couple
from basket import GiftBasket,GiftSelector1,GiftSelector2
from datetime import datetime
import operator
import random
import csv
import math
import sys


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

#testing utility

#generating a list named B of boy objects and boyslist with respective values of object for writing to csv
for i in range(19):
	b=Boy(boys[i],random.randint(10,100),random.randint(24,100),random.randint(1,20),random.randint(6,50),random.choice(typ1))
	boyslist.append([b.name,b.attractiveness,b.intelligence,b.budget,b.minattreq,b.typ,b.status])
	B.append(b)

#writing csv file

with open("guys.csv","w") as h:
	writer=csv.writer(h,delimiter=',')
	writer.writerows(boyslist)

#generating a list named G of girl objects and girlslist with respective values of object for writing to csv
for i in range(13):
	g=Girl(girls[i],random.randint(10,100),random.randint(26,100),random.randint(1,20),random.choice(crit),random.choice(typ2))
	girlslist.append([g.name,g.attractiveness,g.intelligence,g.maintbudget,g.criteria,g.typ,g.status])
	G.append(g)

#writing csv file
with open("girls.csv","w") as f:
	writer=csv.writer(f,delimiter=',')
	writer.writerows(girlslist)

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
				commit.append(s1)
				break
findDates()


s1='Here starts the Valentine week of February:-------------------------------------------------'
commit.append(s1)

choice=random.randint(0,2)

if choice==0:
	s1='Gift Selector 1 starts now-------------------------------------------------'
	commit.append(s1)
	#taking note of all commitments and gift exchanges with time stamps3

	file=open("log.txt","w")
	for item in commit:
		file.write(str(datetime.now()))
		file.write(" %s\n"%item)
	file.close()
	g1=GiftSelector1(couplesList)
	g1.assign()
	g1.writ()

else:
	s1='Gift Selector 2 starts now-------------------------------------------------'
	commit.append(s1)
	#taking note of all commitments and gift exchanges with time stamps3

	file=open("log.txt","w")
	for item in commit:
		file.write(str(datetime.now()))
		file.write(" %s\n"%item)
	file.close()
	g2=GiftSelector2(couplesList)
	g2.assign()
	g2.writ()


