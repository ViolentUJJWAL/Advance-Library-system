import random,datetime,time,student_library_system
def today():
	e=datetime.datetime.now()
	time="%s:%s:%s" % (e.hour, e.minute, e.second)
	date="%s/%s/%s" % (e.day, e.month, e.year)
	return f"{date} | {time}"

# def date(a=0):
# 	e=datetime.datetime.now()
# 	date="%s/%s/%s" % (e.day, e.month + a, e.year)
# 	return date

def readFile(fileName):
	with open(fileName) as re:
		return re.read()

def writeFile(fileName, content, a="a"):
	with open(fileName, a) as wr:
		wr.write(content)

def listFinder(item,find):
	a=None
	for i in item:
		if find.lower() in i.lower():
			a=i
	return a

def showList(lst):
	for a in lst:
		print(a)
		time.sleep(0.1)

def showListFilter(lst,content):
	lstFil=[]
	for a in lst:
		if content.lower() in a.lower():
			lstFil.append(a)
	return lstFil


def nameFilter(i):
	if len(i)>3 :
		return i
	else:
		return None

def idInfo(idnum):
	lst=showListFilter(readFile("library_store.txt").split('\n'),idnum)
	if len(lst)==1:
		lst1=lst[0].split(',')
		return [lst1[0],lst1[1]]
	else:
		return None
def show(lst):
	for a in lst:
		showList(a.split(','))
		time.sleep(0.3)
		print('')

class library:
	libraryName="library_store [Books Hub]"
	def __str__(self):
		greet=f'\n{"*"*10} WELCOME To {self.libraryName} {"*"*10}'
		return f"{greet}\n{student_library_system.date()}"

	def addBook(self,book):
		while True:
			bookName=book
			if bookName=="Q" or bookName=='q':
				pro='Q'
				break;
			bookName=nameFilter(book)
			if bookName==None:
				print('Enter currect book name')
				break
			else :
				writeFile('books_store.txt', f'\n{bookName}')
				print(f"{bookName} is successfully add in Library")
				return 'yes'

	def showIssue(self):
		lst=readFile('history.txt').split('\n')
		idnum=input('Enter Id no.: ')
		if idnum.lower()=="all":
			showlst=showListFilter(lst,'[issue]')
			show(showlst)
		else:
			l=listFinder(readFile("library_store.txt").split('\n'),idnum)
			if l==None:
				print('Enter valid ID number')
			else:
				showlst=showListFilter(lst,'[issue]')
				lst1=showListFilter(showlst,idnum)
				show(lst1)

	def showHistory(self):
		lst=readFile('history.txt').split('\n')
		idnum=input('Enter Id no.: ')
		if idnum.lower()=='all':
			show(lst)
		else:
			l=listFinder(readFile("library_store.txt").split('\n'),idnum)
			if l==None:
				print('Enter valid ID number')
			else:
				showlst=showListFilter(lst,idnum)
				show(showlst)

	def donateBook(self,book,idnum,name):
		donate=self.addBook(book)
		if donate=='yes':
			writeFile('history.txt',f'[donate],Donate Book,{idnum} ({name}),Book - {book},Thanks for Donate Book\n')

	def searchBook(self,book):
		if book.lower()=='all':
			lst=showListFilter(readFile('books_store.txt').split('\n'),'')
			return lst
		else:
			lst=showListFilter(readFile('books_store.txt').split('\n'),book)
			return lst

	def showRequest(self):
		while True:
			i=0
			lstFil=readFile("request.txt").split('\n')
			lstFil.remove('')
			for a,item in enumerate(lstFil):
				if a==0:
					pass;
				else:
					print(f'{a} for')
					showList(item.split(','))
					print('')
					i=1
					time.sleep(0.3)
			if i==0:
				print('No Request')
				break;
			else:
				w=input("\nEnter no.- ")
				if w.lower()=='q':
					break;
				else:
					w=int(w)
					strlst=lstFil[w]
					lst=strlst.split(',')
					if lst[0]=='[feedback]':
						print(f'This is Feedback\nRead Feedback ->\n')
						showList(lst)
						lstFil.pop(w)
						writeFile('request.txt',"\n".join(lstFil),'w')
						writeFile('request.txt','\n')
					elif lst[0]=='[donate]':
						lstbook=lst[2].split(' ')
						lstbook.pop(0)
						lstbook.remove('-')
						book=' '.join(lstbook)
						idnum=lst[3].split(' ')[0]
						name=idInfo(idnum)[1]
						self.donateBook(book,idnum,name)
						lstFil.pop(w)
						writeFile('request.txt',"\n".join(lstFil),'w')
						writeFile('request.txt','\n')
					elif lst[0]=='[request]':
						lstbook=lst[3].split(' ')
						lstbook.pop(0)
						book=" ".join(lstbook)
						fibook=self.searchBook(book)
						if len(fibook)>0:
							print(f'{book[0]} is available in Library')
							con=input(f"send message - ")
							if con.lower()=="yes" or con.lower()=='y':
								lst[0]="[available]"
								lst[1]='Your requested book is Available'
								lststr=",".join(lst)
								writeFile('history.txt',f'{lststr}\n')
								lstFil.remove(strlst)
								writeFile('request.txt',"\n".join(lstFil),'w')
								writeFile('request.txt','\n')
								print("Message Send")
							else:
								print('Message not send')
						else:
							com=input(f'Add {book} in Library - ')
							if com.lower()=="yes" or com.lower()=='y':
								print(book)
								self.addBook(book)
								lst[0]="[available]"
								lst[1]='Your requested book is Available'
								lststr=",".join(lst)
								writeFile('history.txt',f'{lststr}\n')
								lstFil.remove(strlst)
								writeFile('request.txt',"\n".join(lstFil),'w')
								writeFile('request.txt','\n')
								print("Message Send")
							else:
								print('Book not add in Library')
					elif lst[0]=='[return request]':
						his=readFile('history.txt').split('\n')
						req=readFile('request.txt').split('\n')
						num=''
						for a in lst:
							if 'Request no.' in a:
								for i in (a.split(' ')):
									if 'BHLRR' in i:
										num=i
						retstr=showListFilter(his,num)
						show(retstr)
						con=input('\nReturn book -')
						print('')
						if con.lower()=='yes':
							his.remove(retstr[0])
							retlst=retstr[0].split(',')
							book=''
							for i,a in enumerate(retlst):
								print(a)
								if '[issue]' in a:
									retlst[i]='[return]'
								elif 'Issued Book' in a:
									rewBook=retlst[i].split(' ')
									rewBook.remove('Issued')
									rewBook.remove('Book')
									book=' '.join(rewBook)
								elif 'Return date' in a:
									retlst[i]=f'Return date {today()}'
								elif 'return (request' in a:
									retlst[i]="_______________________________Return"
							for h in his:
								if h=="":
									his.remove(h)
							addlst=",".join(retlst)
							print('')
							showList(addlst.split(','))
							his.append(addlst)
							writeFile('history.txt',"\n".join(his),'w')
							writeFile('history.txt','\n')
							self.addBook(book)
							lstFil.remove(strlst)
							writeFile('request.txt',"\n".join(lstFil),'w')
							writeFile('request.txt','\n')					
						else:
							print('Book no return ')	
					break;

	def showReturnRequest(self):
		con=input('Enter no. - ')
		for index,item in enumerate(readFile('request.txt').split('\n')):
			if con.lower()=='all':
				if "[return request]" in item:
					print(f"\nNo. {index}")
					showList(item.split(','))
			else:
				if "[return request]" in item:
					if con in item:
						print(f"\nNo. {index}")
						showList(item.split(','))

while True:
	try:
		lb=library()
		print(lb)
		work=input('''	  1 for Add book
	  2 for Search Book 
	  3 for Show Issue books
	  4 for Show & Solve Request 
	  5 for Show Return Request
	  6 for Show History
	  7 for Show User informetion
	  8 for Donate book
	  9 for Show Feedback
	  Q for EXIT & Off Library
		  -''')
		if work=='1':
			book=input('Enter Book Name: ')
			lb.addBook(book)

		elif work=='2':
			book=input('Search...: ')
			lst=lb.searchBook(book)
			if len(lst)==0:
				print("This book not available in Library")
			else:
				showList(lst)
				print(f"\n{' '*10}{len(lst)} Books")

		elif work=='3':
			lb.showIssue()

		elif work=='4':
			lb.showRequest()

		elif work=='5':
			lb.showReturnRequest()

		elif work=='6':
			lb.showHistory()

		elif work=="7":
			num=input("Enter ID no. or name: ")
			if num.lower()=='all':
				num=''
			lst=showListFilter(readFile("library_store.txt").split('\n'),num)
			for a in lst:
				sh=a.split(',')
				showList(sh)
				print('')

		elif work=='8':
			while True:
				name=''
				book=input('Enter Book Name: ')
				idnum=input('Enter ID no.:')
				if idnum.lower()=="no":
					name=input('Enter name: ')
				else:
					lst=idInfo(idnum)
					if lst==None:
						print('Enter valid ID number')
						break;
					else:
						idnum=lst[0]
						name=lst[1]
				lb.donateBook(book,idnum,name)
				break;

		elif work=="9":
			lst=showListFilter(readFile('request.txt').split('\n'),'[feedback]')
			if len(lst)==0:
				print('No Feedback')
			else:
				show(lst)

		elif work.lower()=="q":
			con=input('EXIT Y/N-')
			if con=='y' or con=="Y":
				c=['E','X','I','T']
				showList(c)
				break;
			else:
				pass;
		else:
			print("Enter currect key")
	except Exception as e:
		print(f'Something is wrong \nError: {e}')