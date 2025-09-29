import math 
from datetime import date

#HI, I had add a opcion to know with its on time to replace the tire

current_date_time = date.today()

width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diamenter of the wheel in inches (ex 15): "))

volume = (math.pi * (width **2) * ratio* (width * ratio + (2540*diameter)))/10000000000
print(f"The aproximate volume is {volume:.2f} liters \n")

replace = input("Do you want to know if your tire need to be replaced?(Y/n) ")

if replace.upper() in ("Y","YES"):
    tire_age = input("Have you had this tire for over 5 years now?(Y/n) ")
    if tire_age.upper() in ("Y","YES"):
        print(" NOW its a exccelent to REPLACE your TIRE")
    elif tire_age.upper() in ("N","NO"):
        print(" Your tire its on day! \n If its close to 5 years of use its recommended to replace it\n")
    else:
        print("Ops! Try again")
else:
    print("Get out before you need a new TIRE!")
    print("Byeee")


with open("volumes.txt","a") as file:
    file.write(f"{current_date_time},{width}, {ratio}, {diameter}, {volume:.2f}\n")