import json
import os
import time

data = []
userData = []


with open('data/books.json') as file:
  data = json.load(file)
  
with open('data/users.json') as file:
  userData = json.load(file)


class Book:
    def __init__(self, title, author, isbn, id):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
    status = "ready"
    location = "z1"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkOut(data, userData):
    clear()
    print("Enter UserID..")
    userIdInput = input()
    for user in userData:
        if userIdInput == user["ID"]:
            userName = user["fullName"]
    
    while True:
        clear()
        print("Username:", userName)
        print("......................")
        print("Enter BookID...")
        bookIdInput = input()
        if bookIdInput == "n":
            break
        for book in data:
            if bookIdInput == book["ID"]:
                book["status"] = "1"
                book["location"] = userIdInput
                with open('data/books.json','w') as file:
                    json.dump(data, file, indent=2)

def checkIn(data):
    while True:
        clear()
        print("Please enter book ID number")
        bookIdInput = input()
        if bookIdInput == "n":
            break
        for book in data:
            if book['ID'] == bookIdInput:
                print('Turning in "'+book['title']+'"!')
                book['status'] = "0"
                print('Putting on the shelf...')
                book['location'] = "z1"
                with open('data/books.json','w') as file:
                  json.dump(data, file, indent=2)

    
def chooseAction():
    clear()
    print("Choose a task...")
    print("[1.] Check Out Books")
    print("[2.] Check In Books")
    userInput = input()
    if userInput == "1":
        checkOut(data, userData)
    if userInput == "2":
        checkIn(data)

while True:
    chooseAction()
