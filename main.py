from enum import Enum

import os

class Genres(Enum):
    Philosophical = "philosophy"
    Classic = "classic"
    Encyclopedic = "encyclopedic"
    Historical = "historical"
    Folklore = "folklore"
    Epic = "epic"
    Religious = "religious"



FILE_NAME = "list_of_books.txt"
PROPERTIES_SPLITTER = "|p/"
NEWLINE_REPLACMENT = "|n/"
class Book:
    def __init__(self, title: str, author: str, genre: str, rate: float, review: str):
        self.title =  title
        self.author = author
        self.genre = genre
        self.rate = rate
        self.review = review

    def __str__(self):
        return f"{self.title} by {self.author}\nGenre: {self.genre}"

    def ShowUserOpinion(self):
        print(f"{"-"*30}\n{self.title} by {self.author}\nGenre: {self.genre}\nRate: {self.rate}\n{self.review}\n{"-"*30}")

    def AppropriateFormatForWriting(self):
        return f"{self.title}{PROPERTIES_SPLITTER}{self.author}{PROPERTIES_SPLITTER}{self.genre}\
{PROPERTIES_SPLITTER}{self.rate}{PROPERTIES_SPLITTER}{self.review.replace("\n", NEWLINE_REPLACMENT)}\n"

    def __lt__(self, other):
        return self.title < other.title

'''
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self.__title = new_title
        else:
            print("Enter correct title")

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author_name):
        if len(author_name) > 0:
            self.__author = author_name
        else:
            print("Enter correct author's name")

    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, new_genre):
        if len(new_genre) > 1:
            self.__genre = new_genre
        else:
            print("Enter correct genre")
'''

def TryParse(userValue: str, minValue: int, maxValue: int):
    result = 0
    while True:
        try:
            result = int(userValue)
            if minValue > result or maxValue < result:
                raise ValueError
            else:
                return result
        except ValueError:
            userValue = input("Enter correct value: ")

def GeneralStringCheck(text: str):
    while True:
        if len(text) < 0:
            input("Enter correct vlaue: ")
        else:
            return text

def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")

def PrintBooks(listOfBooks: list[Book]):
    clearConsole()
    PrintAppName("Local Library")
    for book in listOfBooks:
        print(book.ShowUserOpinion(), end="\n\n")

def PrintAppName(text: str):
    print(text)

def readFromFile() -> list[Book]:
    try:
        file = open(FILE_NAME, "r")
        listOfBooks = appendingBooks(file)
        return listOfBooks
    except FileNotFoundError:
        print("You do not have existing library. Creating new.")
        file = open("list_of_books.txt", "w")
        return []

def writeInFile(newBook: Book, books):
    with open(FILE_NAME, "a+") as file:
        file.write(newBook.AppropriateFormatForWriting())
        books.append(newBook)


def appendingBooks(file) -> list[Book]:
        list = []
        string = " "
        while len(string) != 0:
            string = file.readline()
            properties = string.split(PROPERTIES_SPLITTER)
            book = Book(properties[0], properties[1], properties[2], float(properties[3]), properties[4].replace(NEWLINE_REPLACMENT, "\n"))
            list.append(book)
        return list

def sortByTitle(books: list[Book]):
    return sorted(books, key=lambda s: s.title)


def sortByRate(books: list[Book]):
    return sorted(books, key=lambda s: s.rate)

def getExistingGenres(books: list[Book]):
    return set([i for i in books])

def filterByGenre(books: list[Book]):
    clearConsole()
    genres = sorted(getExistingGenres(books))
    amountOfGenres = len(genres)
    for i in range(amountOfGenres):
        print(f"{i + 1} - {genres[i].genre}")
    choice = TryParse(input("Choose genre: "), 1, amountOfGenres) - 1
    basicGenre = genres[choice].genre
    neededBooks = [book for book in books if book.genre == basicGenre]
    PrintBooks(neededBooks)



def __main__():

    crimeAndPunishment = Book("Crime and Punishment", "F.M.Dostoevsky", "Russian Classics", 10, "I love this book")
    crimeAndPunishment2 = Book("A Crime and Punishment2", "A.N.Dostoevsky", "American Classics", 10, "I love this book\nAnd I love my dear Lise")
    crimeAndPunishment3 = Book("Bad book", "f. nigger", "Jap", 10, "I love this book\nAnd I love my dear Lise")

    listOfBooks: list[Book] = [crimeAndPunishment, crimeAndPunishment3]# get from file
    writeInFile(crimeAndPunishment2, listOfBooks)
    listOfBooks = sortByTitle(listOfBooks)

    print("Local Library")
    choice = TryParse(input("1 - books by the Name, 2 - filter by genre, 3 - search for author, 4 - add new book, 5 - edit existing book, 0 - exit\n"), 0, 4)
    match(choice):
        case 1:
            PrintBooks(listOfBooks)
        case 2:
           filterByGenre(listOfBooks)
        case 3:
            print("jotaro")
        case 4:
            print("josuke")
        case 5:
            print("Lise")
        case 0:
            print("joseph")
    print("end")

__main__()
