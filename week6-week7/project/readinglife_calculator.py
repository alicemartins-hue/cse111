#Discover how much time of your life you had used reading
import random

BOOKS = {}
x = [
    "lightning","storm","wildfire","machine","tornado","hurricane","dragon","shadow",
    "phoenix","beast","flame","stormcloud","thunderbolt","comet","spark","rocket",
    "ghost","demon","angel","titan","scholar","wizard","knight","warrior","bard",
    "alchemist","monk","pirate","hunter","assassin","strategist","oracle","scribe",
    "poet","wanderer","sage","rebel","dreamer","champion","guardian","volcano",
    "thunderstorm","battlefield","library","forest","temple","galaxy","inferno",
    "desert","labyrinth","mountain","ocean","mirror","abyss","kingdom","realm",
    "dungeon","castle","arena","cathedral","griffin","unicorn","serpent","wolf",
    "raven","lion","leviathan","chimera","sphinx","banshee","golem","valkyrie",
    "giant","elf","vampire","fae","siren","reaper","centaur","hydra","firestorm",
    "melody","heartbeat","eclipse","chaos","destiny","prophecy","echo","silence",
    "twilight","dawn","dusk","fate","illusion","memory","paradox","myth","legend",
    "eternity","dream"
]


def add_books(name,pag):
    """Add keys and values to the dictionary
    Parameters
    name = string
    pag = int
    Return None
    """

    title = name.capitalize()
    BOOKS[title] = pag

def sum_page(dict_name=BOOKS):
    """Compute all the pages values
    Parameters
    dict_name= dict
    Return int 
    """
    pages = sum(BOOKS.values())
    return pages

def read_time(time):
    """Compute total reading time
      based on pages and reading speed.
    Parameters
    time = int
    Returns float
    """
    time_reading = sum_page() * time
    hours_reading = round(time_reading/60,2)
    return hours_reading

def character_life(pages, c_l=30):
    """Compute the amount of characters life you had read
    Parameters
    pages = int
    c_l = int
    Return int
    """
    quantity = pages/c_l 
    return round(quantity)

def life(age,reading):
    """Compute the percent of your life you had passed reading
    Parameters
    age = int
    reading = float
    Return float
    """
    days_lived = age * 365
    hours_lived = days_lived * 24
    time_read = reading * 100 / hours_lived
    return round(time_read,4)

def days_reading(reading):
    """Compute the total of hours you passed reading to days
    Parameters
    reading = float
    Return int
    """
    x = reading / 24
    return round(x)

def ranking(list):
    """Taking a word from a dict using module random
    Parameters
    list = dict
    Return string
    """
    word = random.choice(list)
    return word

def main():
    print("")
    print("HI, WELCOME TO READING LIFE CALCULATOR")
    print("")

    age = int(input("Enter your age: "))
    print("Do you know How much min you spend to read an page? ")
    reading_time  = input("--- ")
    if reading_time.upper() in ('Y', 'YES'):
        reading_time = float(input("Enter the time in minutes: "))
        print(f"You read {reading_time} per page")
    else:
        print("Dont worry, we gonna use a general time instead.")
        reading_time = 2

    print("")
    print("ADD THE BOOKS YOU HAD READ")
    title = input("Enter the title: ")
    pag = int(input("Enter the amount of pages: "))
    add_books(title,pag)
    print("")
    print(f"Stored book '{title.capitalize()}': {pag} pages")
    add_more_books = input("ADD MORE?(Y/n) ")
    while add_more_books.upper().startswith("Y"):
        title = input("Enter the title: ")
        pag = int(input("Enter the amount of pages: "))
        add_books(title,pag)
        print("")
        print(f"Stored book '{title.capitalize()}': {pag} pages.")
        add_more_books = input("ADD MORE?(Y/n) ")
        print("")

    pages = sum_page()
    reading_hours = read_time(reading_time)
    reading_in_days = days_reading(reading_hours)
    months_reading = reading_in_days/ 30
    percent_life = life(age, reading_hours)

    print("")
    print(f"You had lived {character_life(pages)} character lifes")
    print(f"You had read {reading_hours} hours, {reading_in_days} days and {months_reading:.0f} months")
    print(f"This is equivalent to {percent_life}% of your life")
    print(f"")
    print(f"Wow! You read like a {ranking(x)}!")

if __name__ == "__main__":
    main()