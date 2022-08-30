import random,datetime,time

def today():
	e=datetime.datetime.now()
	time="%s:%s:%s" % (e.hour, e.minute, e.second)
	date="%s/%s/%s" % (e.day, e.month, e.year)
	return f"{date} | {time}"

def date(a=0):
	e=datetime.datetime.now()
	date="%s/%s/%s" % (e.day, e.month + a, e.year)
	return date

def idload():
	Ids=''
	with open("library_store.txt") as re:
		Ids=re.read()
		Ids=Ids.split('\n')
	idNum=f'BHL{random.randint(100,999)}{len(Ids)+2}'
	return idNum

def nameFilter(i):
	if len(i)>3 :
		return i
	else:
		return None

def phoneFilter(phone):
	try:
		if 10<=len(phone)<=13:
			f=int(phone)
			return phone
		else:
			return None
	except Exception as e:
		return None

def signInSystem():
	while True:
		pr=''
		print('Note: Enter Q/q for Back')
		username=None
		phone=None
		address=None
		while username==None :
			i=input('Emter your Usename: ')
			if i=="Q" or i=="q":
				pr="Q"
				break;
			username=nameFilter(i)
			if username==None or username=='Student' :
				print('Enter valid urename')

		if pr=='':
			while phone==None :
				phoneNum=input('Enter Phone no.: ')
				phone=phoneFilter(phoneNum)
				if phoneNum=='Q' or phoneNum=="q":
					pr="Q"
					break; 
				if phone==None or phone=='':
					print('Enter valid phone Number')
		if pr=='':
			while address==None:
				a=input('Enter Address: ')
				if a=="Q" or a=='q':
					pr="Q"
					break;
				address=nameFilter(a)
				if address==None :
					print('Enter valid Location')
		if pr=='':
			idNum=idload()
			print(f'\nYour Information\n(Note: Save your Id no. for login )\nId no. is {idNum}\nUserName is {username}\nPhone no. {phone}\nAddress: {address}')
			con=input('''Confirm your informetion
	1 for Yes save
	2 for Edit
	3 for not save & Back
						--> ''')
			if con=='1':
				signIn(idNum,username,phone,address)
				break;
			elif con=='2':
				pass;
			else:
				break;
		if pr =="Q":
			break;

def signIn(idNum, username, phone, address):
	writeFile("library_store.txt",f'{idNum},{username.capitalize()},{phone},{address}\n')

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

def greeting(libraryName,name):
	greet=f'\n{"*"*10} WELCOME To {libraryName} {"*"*10}'
	nameGreet=f"{' '*5}Hello Dear, {name}"
	print(f'{greet}\n{nameGreet}')

def issueBook(book,idNum,username):
	pr=''
	while pr=="":
		issueBook=None
		while issueBook==None:
			issueBook=input("Enter Book Name: ")
			if issueBook=="Q" or issueBook=='q':
				pr='Q'
				break;
			issueBook=nameFilter(issueBook)
		if pr=='':
			findBook=listFinder(book,issueBook)
			if findBook==None:
				print(f'''Sorry {issueBook} book is not available and request send for {issueBook} book available soon as posible''')
				requestbook(issueBook,idNum,username)
				break;
			else:
				con=input('Confirm for Issue Y/N -')
				if con=='Y' or con=='y':
					book.remove(findBook)
					storeBook="\n".join(book)
					writeFile("books_store.txt", storeBook, "w")
					writeFile("history.txt", f'[issue],Book issue,{idNum} ({username}),Issued Book {findBook},Issued date {today()},Return date {date(1)},return (pending)\n')
					print(f'Thankyou have a enjoy {findBook} book and return book with in 30 Days')
					break;
				else:
					print('Book not Issued')
					break;

def showList(lst):
	for i,a in enumerate(lst):
		if a=="":
			pass
		else:
			print(a)

def showListFilter(lst,content):
	lstFil=[]
	for a in lst:
		if content.lower() in a.lower():
			lstFil.append(a)
	return lstFil

def requestbook(bookName,idNum,username):
	writeFile('request.txt', f'[request],Request,{idNum} ({username}),Request {bookName}\n')

def historyShow(idNum):
	lst=readFile('history.txt').split('\n')
	idnum=idNum
	if idnum.lower()=='all':
		show(lst)
	else:
		l=listFinder(readFile("library_store.txt").split('\n'),idnum)
		if l==None:
			print('Enter valid ID number')
		else:
			showlst=showListFilter(lst,idnum)
			show(showlst)

def returnRequest(bookName,idNum,username):
	c=0
	lst=readFile("history.txt").split('\n')
	lst1=''
	for i in range(len(lst)):
		if idNum in lst[i] and "[issue]" in lst[i] and bookName in lst[i]:
			lst1=lst[i].split(',')
			for e in range(len(lst1)):
				if "return (pending)" in lst1[e]:
					lst1[e]=''
					lst[i]=''
					c=e
					
			if c>0:
				requestNum=f'BHLRR{random.randint(100,999)}{len(lst)+2}'
				lst1[c]=f'return (request - {requestNum})'
				stl=','.join(lst1)
				showList(stl.split(','))
				lst[i]=stl
				strlist="\n".join(lst)
				writeFile("history.txt", f'{strlist}\n', "w" )
				print('\nRequest send')
				writeFile('request.txt', f'[return request],{idNum} ({username}),Book - {bookName},Request no. {requestNum}\n')
				break;
		if c>0:
			break;
		else:
			pass;

def donateBook(bookName, idNum, name):
	writeFile('request.txt', f'[donate],Donate Book,Book - {bookName},{idNum} ({name})\n')
	print('Thankyou for Donate book and Have a wonderful day')

def show(lst):
	for a in lst:
		showList(a.split(','))
		time.sleep(0.3)
		print('')

class student:
	libraryName="Books Hub Library"
	name='Student'
	storeId=''

	def logIn(self, idNum):
		name=''
		while True:
			Ids=readFile("library_store.txt")
			Ids=Ids.split('\n')
			store=listFinder(Ids,idNum)
			if store==None:
				print("enter valid id")
				break;
			self.storeId=store.split(',')
			name=self.storeId[1]
			greeting(self.libraryName,name)
			mainMenu=input('''     (Note: Enter only)
	1 for Search book
	2 for Issue book
	3 for Request book
	4 for My History
	5 for Request for Return Book
	6 for Donate Book
	7 for Feedback
	Q for EXIT & Log out
	   - ''')
			if mainMenu=='1':
				book=readFile("books_store.txt").split('\n')
				search=input('Search book: ').split(' ')
				searchList=[]
				for se in search:
					for bookShow in book:
						if se.lower() in bookShow.lower():
							if bookShow not in searchList:
								searchList.append(bookShow)
								print(f"* {bookShow}")
				if len(searchList)==0:
					print('No Search Result')
				else:
					issueBook(book,idNum,name)
	
			elif mainMenu=='2':
				book=readFile("books_store.txt").split('\n')			
				issueBook(book,idNum,name)

			elif mainMenu=='3':
				while True:
					bookName=input('Enter Request book name: ')
					if bookName.lower()=='q':
						break;
					else:
						requestbook(bookName,idNum,name)
						print(f'Request send for {bookName} book available soon as posible')
						break

			elif mainMenu=='4':
				historyShow(idNum)

			elif mainMenu=='5':
				r=0
				lst=readFile('history.txt').split('\n')
				for e in lst:
					if idNum in e and 'return (pending)' in e:
						print('')
						showList(e.split(','))

						r+=1

				while r>0:
					print('')
					print(f'{r} books pending to return')
					bookName=input('''(Note: please enter currect book name)
Enter Return Book Name: ''')
					if bookName=='q' or bookName=="Q":
						break;
					returnRequest(bookName,idNum,name)
					break;
				else:
					print("Not Pending Book for Return")

			elif mainMenu=="6":
				while True:
					bookName=input('Enter Book Name: ')
					if bookName=='Q' or bookName=='q':
						print("Please Donate book for ")
						break;
					else:
						bookName=nameFilter(bookName)
						if bookName==None:
							print('Please enter valid book name')
						else:
							donateBook(bookName,idNum,name)
						break;

			elif mainMenu=="7":
				while True:
					srt=input('''(Note: Enter only Q for back)
Write-
 ''')
					if srt.lower()=='q':
						break
					else:
						writeFile('request.txt', f'[feedback],Feedback,{idNum} ({name}),{srt}\n')
						print('Thankyou for Your Feedback and Your valuable time')
						break;

			elif mainMenu.lower()=='q' :
				con=input('Log Out Y/N -')
				if con=="Y" or con=="y":
					print(f'Thankyou {name}, have a Great day.')
					break;
				else:
					print('Use The Library Then have a Great day.')
					pass;

			else:
				print('Enter valid key')

		
	def __str__(self):
		if __name__=='__main__':
			FrontMenu=['1 for Log in', '2 for Sign in', '3 for Feedback', "Q for EXIT"]
			FMstr='\n     '.join(FrontMenu)
			greeting(self.libraryName,self.name)
			return f'     {FMstr}'
			
if __name__=='__main__':
	while True:
		sl=student()
		print(sl)
		work=input('         -')
		if work=="1":
			try:
				idNum=input('Enter ')
				if 'bhl' in idNum.lower() and len(idNum)>=7:
					sl.logIn(idNum)
				else:
					print('Enter full ID no.')
			except Exception as e:
				print(F'Error: {e}\nSorry for error please try again\n')
		elif work=="2":
			try:
				signInSystem()
			except Exception as e:
				print(F'Error: {e}\nSorry for error please try again\n')
		elif work=="3":
			while True:
				name=input('Enter Name: ')
				srt=input('''(Note: Enter only Q for back)
	Write-
	 ''')
				if srt.lower()=='q':
					break
				else:
					writeFile('request.txt', f'[feedback],Feedback,Name - {name},{srt}\n')
					print('Thankyou for Your Feedback and Your valuable time')
					break;
		elif work.lower()=="q":
			conf=input('EXIT\ny/n Y/N -')
			if conf=='y' or conf=='Y':
				print(f'thankyou for visiting\n{" "*20}EXIT')
				exit()
			else:
				pass;
		else:
			print('Please Enter valid key')