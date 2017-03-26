from boy import Boy
from girl import Girl
import random
import csv

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

#generating a list named B of boy objects and boyslist with respective values of object for writing to csv
for i in range(19):
	b=Boy(boys[i],random.randint(0,100),random.randint(0,100),random.randint(0,5000),random.randint(0,50),random.choice(typ1))
	boyslist.append([b.name,b.attractiveness,b.intelligence,b.budget,b.minattreq,b.typ,b.status])
	B.append(b)

#writing csv file
with open("guys.csv","w") as h:
	writer=csv.writer(h,delimiter=',')
	writer.writerows(boyslist)

#generating a list named G of girl objects and girlslist with respective values of object for writing to csv
for i in range(13):
	g=Girl(girls[i],random.randint(0,100),random.randint(0,100),random.randint(0,5000),random.choice(crit),random.choice(typ2))
	girlslist.append([g.name,g.attractiveness,g.intelligence,g.maintbudget,g.criteria,g.typ,g.status])
	G.append(g)

#writing csv file
with open("girls.csv","w") as f:
	writer=csv.writer(f,delimiter=',')
	writer.writerows(girlslist)

for boy in B:
	for girl in G:
		#if boy and girls are both ready to pair with each other and are already not commited
		if boy.readytopair(girl) and girl.readytopair(boy) and boy.currStatus()=='S' and girl.currStatus()=='S':
			#change their status
			boy.changeStatus()
			girl.changeStatus()
			s1=boy.name+' is gonna date '+girl.name
			commit.append(s1)
			break

#taking note of all commitments
file=open("log.txt","w")
for item in commit:
	file.write("%s\n"%item)


