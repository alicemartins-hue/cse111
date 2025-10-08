from chemistry import make_periodic_table

def learn_molar_mass(formula, amount):
    """
    Calculates the molar mass and number of moles of a compound.
    Takes a formula (list of element–quantity pairs) and the sample mass.
    Uses the periodic table to find atomic masses and perform the calculations.
    Parameters:
    formula = string
    amount = float
    Return: float
    """

    x = []
    y = []
    for element in formula:
            for value in element:
                if isinstance(value, int):
                    i = value
                    x.append(i)
                else:
                     symbol = value
                     y.append(symbol)

    print("Do you want to know the diference ")
    question1 = input("between the letter and the numbers? (Y/n) ")
    if question1.upper() in ("Y","YES"):
         print("The capitals in the list are references to symbols")
         print("on periodic table. The numbers are the quantity")
         print("of the element present in that molecule.")
        
         confirmation = input("Did you understand? (Y/n) ")
         while confirmation.upper() != ("Y","YES"):
            print("The capitals in the list are references to symbols")
            print("on periodic table. The numbers are the quantity")
            print("of the element present in that molecule.")
            confirmation = input("Did you had understood? (Y/n)  ")
    
    print("")
    print("On the sequence, Separe the symbols of the number of atoms")
    print("")
    print("Write - symbol - to list the symbols")
    question2 = input("--- ")
    if question2.upper().startswith("S"):
         print(y)
    else:
         print("Now will not see the list")
         print(" and your powers of summoning an chemical symbols list is gone")
    
    print("")
    print("Write - number - to list the number of atoms")
    question3 = input("--- ")
    if question3.upper().startswith("N"):
         print(x)
    else:
         print("Now will not see the list")
         print(" and your powers of summoning, an number of atoms list, is gone")
    print("")

    list_atomic_mass = []
    def find_mass(symbol):
         """Function to find the atomic mass
           of a symbol in the periodic dict
           parameter: symbol = string
           return float"""
         
         atomic_mass = make_periodic_table()[symbol][1]
         return atomic_mass
    
    print("It is important to have 2 lists to be capable of use the values on differents ways")
    print("")
    print("We gonna use the list of symbols like a key to find they atomic mass on the dictionary.")
    print("I had create a function to do that so now,")
    
    for symbol in y:
         #here we find the atomic value referent to the symbols that we got in formula
         #pass that to the find mass function and add the value to the list_atomic_mass
         atomic_mass = find_mass(symbol)
         list_atomic_mass.append(atomic_mass)
    
    print("you just have to enter 'you are incrible' for your powers summon the list")
    question4 = input("--- ")
    print(list_atomic_mass)
    print("WOW, you ARE incrible!!!")
    print("")
    question5 = input("Did you really write that I am incrible?")
    if question5.upper().startswith("Y"):
         print("Awnn, thank you!")
    else:
         print("I know...")
         print("this is not a game, I know")
         print("but I like to talk")
    print("well, keep going")
    print("")

    print("Find the atomic mass is important because we need that to discover the molar mass")
    print("The atomic mass need to be in the same index that they reference symbol")
    print("That index is gonna be the same as the number, in the number of atoms list")
    print("")
    question6 = input("ok? ")
    print("They had to be in the same index")
    print("to the number of atoms multiply the right atomic mass")
    print("")
     
    mult_list = []
    for atom_num, atom_mass in zip(x,list_atomic_mass):
         #here we gonna multiply the number of atoms by it self reference atomic mass
         multiply = atom_num * atom_mass
         mult_list.append(multiply)
    print("Now use your powers one last time, write - atomic mass -")
    question7 = input("--- ")
    print(mult_list)

    if question7.upper() == "ATOMIC MASS":
         print("I really dont believe that you are using your powers")
         print("That is REALLY awesome")
         print("in someway I think that... I love you")
         print("Did you think that we have chemistry?")
         print("HAHAHHAAHA")
    else:
         print("")
         print("you lost a good joke")
         print("")
    
    molar_mass = sum(mult_list)
    moles = amount / molar_mass

    question8 = input("Are you ready to the conclusion? ")
    print("")
    print("CONCLUSION")
    print("To conclude we need to sum all the atomic mass values")
    print("And... tcharan!")
    print(molar_mass)
    print("This is our molar mass")
    print("")
    question9 = input("use your power to discover the moles  ")
    print("")
    print("**discovering the moles**")
    print("To find the mole just divide the amount by the molar mass")
    print(f"amount {amount} / {molar_mass} molar mass")
    question10= input("Did you know the answer? ")
    print("I dont know (either), but the machine knows")
    print("Ask the machine the answer")
    print("The biggest power we have, is the power to be gentle")
    question11= input("say something gentle... ")
    print("")
    print(moles)
    print("")
    print("byee")
