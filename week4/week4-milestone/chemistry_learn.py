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
    print("And so you should.")

    list_atomic_mass = []
    def find_mass(symbol):
         """Function to find the atomic mass
           of a symbol in the periodic dict
           parameter: symbol = string
           return float"""
         
         atomic_mass = make_periodic_table()[symbol][1]
         return atomic_mass
    
    for symbol in y:
         #here we find the atomic value referent to the symbols that we got in formula
         #pass that to the find mass function and add the value to the list_atomic_mass
         atomic_mass = find_mass(symbol)
         list_atomic_mass.append(atomic_mass)

    mult_list = []
    for atom_num, atom_mass in zip(x,list_atomic_mass):
         #here we gonna multiply the number of atoms by it self reference atomic mass
         multiply = atom_num * atom_mass
         mult_list.append(multiply)

    molar_mass = sum(mult_list)
    moles = amount / molar_mass

    print("")
    print(f"{molar_mass} grams/mole")
    print(f"{moles:.5f} moles")
    print("")