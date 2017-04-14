from allIn import Boy,Girl,Gifts,PeopleAndObjects
from couples import Couple
try:
	from boy import Boy
	from girl import Girl
	from gift import Gifts
	
	from magic import awesome
except ImportError:
	print('There is error in importing some files')
from datetime import datetime
import operator
import random
import csv
import math

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
try:
	for i in range(22):
		b=Boy(boys[i],random.randint(10,100),random.randint(24,100),random.randint(50,5000),random.randint(6,50),random.choice(typ1))
		boyslist.append([b.name,b.attractiveness,b.intelligence,b.budget,b.minattreq,b.typ,b.status])
		B.append(b)
except IndexError:
	print('List out of bounds')

#writing csv file
with open("guys.csv","w") as h:
	writer=csv.writer(h,delimiter=',')
	writer.writerows(boyslist)

#generating a list named G of girl objects and girlslist with respective values of object for writing to csv
try:
	for i in range(13):
		g=Girl(girls[i],random.randint(10,100),random.randint(26,100),random.randint(12,5000),random.choice(crit),random.choice(typ2))
		girlslist.append([g.name,g.attractiveness,g.intelligence,g.maintbudget,g.criteria,g.typ,g.status])
		G.append(g)
except StopIteration:
	print('List out of bounds')

#writing csv file
with open("girls.csv","w") as f:
	writer=csv.writer(f,delimiter=',')
	writer.writerows(girlslist)

def findDates():
	try:
		for boy in B:
			for girl in G:
				#if boy and girls are both ready to pair with each other and are already not commited
				if boy.readytopair(girl) and girl.readytopair(boy) and boy.currStatus()=='S' and girl.currStatus()=='S':
					#change their status
					boy.changeStatus()
					girl.changeStatus()
						
					c=Couple(boy.name,boy.typ,girl.typ,girl.name,boy.budget,girl.maintbudget,boy.attractiveness,girl.attractiveness,boy.intelligence,girl.intelligence)
					couplesList.append(c)
					s1=boy.name+' is gonna date '+girl.name
					commit.append(s1)
					break
	except IndentationError:
		print('unexpected indentations')


findDates()


s1='Here starts the Valentine week of February:--------------------------------------------------------------'
commit.append(s1)


#making gift-basket

giftBasket=[]

gif=['Portable Charger','Sony Camera','earrings','Book','Chocolate','Teddy','Perfume','Cookies','Speakers','Purse','Bracelet','Novel','Game','earphones']
for item in gif:
	giftBasket.append(Gifts(item,random.randint(50,3500),random.randint(1,100),random.choice(gifts)))

giftBasket.sort(key=operator.attrgetter('price'))

fate=[]
happyCouples={}
compatibleCouples={}

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
		try:
			spent+=item.price/0
		except ArithmeticError:
			print('there is some error in arithmetics for this variable')
		s1=c.bf+' gifts '+item.name+' '+c.gf
		commit.append(s1)
	
	#calculate happiness
	c.Cal(c.budget,spent)
	h1=c.happiness
	c1=c.compatibility
	z=(h1,c1)
	fate.append(z) #fate of relationship depends upon this

	#dictionary of happiness with corresponding couples
	happyCouples.update({c.bf+' and '+c.gf:h1})

	#dictionary of compatibility with corresponding couples
	compatibleCouples.update({c.bf+' and '+c.gf:c1})


#taking note of all commitments and gift exchanges with time stamps
try:
	file=open("log.txt","r")
	for item in commit:
		file.write(str(datetime.now()))
		file.write(" %s\n"%item)
except IOError:
	print('Error can\'t write to file')
finally:
	file.close()

#print k most happiest couples
fate.sort(key=lambda x:x[0],reverse=True)
k=3
s1=str(k)+' most happiest couples are given below:--------------------------------------------------'
commit.append(s1)
print(s1)
hi=[x[0] for x in fate]
topk=hi[:k]
for item in topk:
	try:
		s1=list(happyCouples.keys())[list(happyCouples.values()).index(item)] + ' with happiness value: '+str(item)
	except TypeError:
		print('can\'t convert int object to string implicitly')
	
	commit.append(s1)
	print(s1)	
print('\n')

#print k most compatible couples
fate.sort(key=lambda x:x[1],reverse=True)
k=3
s1=str(k)+' most compatible couples are given below:'
commit.append(s1)
print(s1)
hi=[x[1] for x in fate]
topk=hi[:k]
for item in topk:
	try:
		s1=list(compatibleCouples.keys())[list(compatibleCouples.values()).index(item)]+ ' with compatibility value: '+str(item)
	except TypeError:
		print('can\'t convert int object to string implicitly')
	
	commit.append(s1)
	print(s1)


