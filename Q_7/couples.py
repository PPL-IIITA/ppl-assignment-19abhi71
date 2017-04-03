from datetime import datetime

class Couple:

	def __init__(self,bf,bfType,gfType,gf,budget,maintbudget,bfatt,gfatt,bfint,gfint,happiness):
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
		self.happiness=happiness

	
class findInList(Couple):
	
	def __init__(self,boys,coupleList):
		#super(findInList,self).__init__()
		print('In list: ')
		self.boys=boys
		self.coupleList=coupleList
		self.commit=[]

	def look(self):

		for b in self.boys:
			k=0
			for c in self.coupleList:
				if b==c.bf:
					self.s1=b + ' has gf named '+c.gf
					self.commit.append(self.s1)
					print(self.s1)
					k=1
					break
			if k!=1:
				self.s1=b + ' is single!'
				self.commit.append(self.s1)
				print(self.s1)

	def writ(self):

		file=open("log.txt","a+")
		for item in self.commit:
			file.write(str(datetime.now()))
			file.write(" %s\n"%item)
		file.close()


class  findInSortedList(Couple):
	
	def __init__(self,boys,coupleList):
		#super(findInSortedList, self).__init__()
		print('In sorted List :')
		self.boys=boys
		self.coupleList=coupleList
		self.commit=[]

	def binarySearch(self,alist, item):
	    self.first = 0
	    self.last = len(alist)-1
	    self.found = False

	    while self.first<=self.last and not self.found:
	        self.pos = 0
	        self.midpoint = (self.first + self.last)//2
	        if alist[self.midpoint].bf == item:
	            self.pos = self.midpoint
	            self.found = True
	        else:
	            if item < alist[self.midpoint].bf:
	                self.last = self.midpoint-1
	            else:
	                self.first = self.midpoint+1
	    return (self.pos, self.found)

	def look(self):
		self.coupleList.sort(key=lambda x:x.bf)
		self.t=()
		for b in self.boys:
			self.t=self.binarySearch(self.coupleList,b)
			if self.t[1]==True:
				self.s1=b + ' has gf named '+self.coupleList[self.t[0]].gf
				self.commit.append(self.s1)
				print(self.s1)
			else: 
				self.s1=b + ' is single!'
				self.commit.append(self.s1)
				print(self.s1)

	def writ(self):

		file=open("log.txt","a+")
		for item in self.commit:
			file.write(str(datetime.now()))
			file.write(" %s\n"%item)
		file.close()
				

class findInHashtable(Couple):

	def __init__(self,boys,coupleList):
		#super(findInHashtable, self).__init__()
		print('In Hashtable:')
		self.boys =boys
		self.coupleList=coupleList
		self.commit=[]

	def look(self):

		for b in self.boys:
			if b in self.coupleList:
				self.s1=b + ' has gf named '+self.coupleList[b]
				self.commit.append(self.s1)
				print(self.s1)
				
			else:
				self.s1=b + ' is single!'
				self.commit.append(self.s1)
				print(self.s1)

	def writ(self):

		file=open("log.txt","a+")
		for item in self.commit:
			file.write(str(datetime.now()))
			file.write(" %s\n"%item)
		file.close()