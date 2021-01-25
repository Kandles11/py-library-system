import json
import os
import time

data = []
selectedBooks = []
headers = []

with open('data/books.json') as file:
  data = json.load(file)

class Book:
    def __init__(self, title, author, isbn, id):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
    status = "ready"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def selectBook(data, selectedBooks):
    clear()
    counter = 0
    for book in data:
        if book["status"] == "0":
            stringToPrint = "[{}.] {}: {}".format(book["ID"], book["title"], book["author"])
            print(stringToPrint)
            counter += 1
    if counter > 0:
        print('Select a book! (enter the books id number)')
        selectedBookID = input()
        for book in selectedBooks:
            if book == selectedBookID:
                print('You already selected that book!')
                time.sleep(3)
            if book != selectedBookID:
                selectedBooks.append(selectedBookID)
        if len(selectedBooks) == 0:  
            selectedBooks.append(selectedBookID)

    else:
        print("Oh no! There aren't any books available. Come back later!")
        time.sleep(5)
    

def checkOut(data, selectedBooks):
    clear()
    for selectedBook in selectedBooks:
        for book in data:
            if book['ID'] == selectedBook:
                print('Found your book! (',book['title'],")")
                book['status'] = "1"
                print('Pulling from shelf...')
    with open('data/books.json','w') as file:
        json.dump(data, file, indent=2)
    print("Check out complete! Enjoy your books!")
    time.sleep(5)

def checkIn(data, selectedBooks):
    clear()
    print("Please enter book ID number")
    userInput = input()
    for book in data:
            if book['ID'] == userInput:
                print('Turning in "'+book['title']+'"!')
                book['status'] = "0"
                print('Putting on the shelf...')
    with open('data/books.json','w') as file:
        json.dump(data, file, indent=2)
    print("Check in complete! Thank you!")
    time.sleep(5)
        
def generateHeader():
    headerString1 = "Books selected: "+ str(len(selectedBooks))
    headerString2 = "--------------------------------"
    return [headerString1, headerString2]

    
def chooseAction():
    clear()
    print(headers[0])
    print(headers[1])
    print("Choose a task...")
    print("[1.] Select Books")
    print("[2.] Check Out Books")
    print("[3.] Check In Books")
    userInput = input()
    if userInput == "1":
        selectBook(data, selectedBooks)
    if userInput == "2":
        checkOut(data, selectedBooks)
    if userInput == "3":
        checkIn(data, selectedBooks)

while True:
    headers = generateHeader()
    chooseAction()
