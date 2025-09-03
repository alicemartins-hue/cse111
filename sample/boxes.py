import math

items = int(input("Enter the number of manufactured items: "))
pack = int(input("How much items you gonna pack per box? "))
2
box = math.ceil(items/pack)

print(f"For {items} items, packing {pack} in each box, you will need {box} boxes")

