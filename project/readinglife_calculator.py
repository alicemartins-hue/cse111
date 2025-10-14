#Discover how much time of your life you had used reading
"""
"Reading Life Calculator, is project made to show how much you 
had been reading, the time of your life you had using to read.
You will have a opportunity to add all the books you want, its gonna make
a list with all them, the program will calculate the time reading life time basead on how much time
you depend to read 1 page. Using some collect informations, not scientifically accurate, 
it will compare the time you had read with the time how much a character usually lives in a 
YA fantasy book for you know what amount of characters lifes you had.
Also, make a funny ranking comparing you with something random just to appear:
    'Wow! You read like a (random)!'
"

2. What real-world problem will your program address or help to solve?
Discover how much time of your life you had used reading

3. What will you learn from developing this program?
How to  apply researchs in programs, how to use a google api
develop my habilility of working with lists and objects, maybe dict too.
patience.

4. What Python modules will your program use?
pytest, math, and maybe some more.

5. List the names of functions you will need?
readtime, lifetime, comparison, add_books, list_books, ranking

6. List the names of the test functions you will write.
test_readtime, test_lifetime, test_comparison, test_add_books, test_list_books
test_ranking
"""

from random_words import x
import random

BOOKS = {}

def readtime():
    pass

def lifetime():
    pass

def comparison():
    pass


def add_books(name,pag):
    BOOKS[name] = pag
    

def ranking():
    pass

def main():
    print("")
    print("HI, WELCOME TO READING LIFE CALCULATOR")
    print("")

    age = int(input("Enter your age: "))
    reading_time  = input("Do you know how much time you spend to read a page?")
    print("")
    #print("Enter *list* to add more than one book")
    #book_or_list = input("--- ")
    print("ADD THE BOOKS YOU HAD READ")
    tittle = input("Enter the title: ")
    pag = int(input("Enter the amount of pages: "))
    add_books(tittle,pag)
    add_more_books = input("ADD MORE?(Y/n) ")
    while add_more_books.upper.startswith("Y"):
        tittle = input("Enter the title: ")
        pag = int(input("Enter the amount of pages: "))
        add_books(tittle,pag)
        add_more_books = input("ADD MORE?(Y/n) ")

    if reading_time.upper in ('Y', 'YES'):
        reading_time = float(input("Enter the time in minutes: "))
    else:
        reading_time = 2
