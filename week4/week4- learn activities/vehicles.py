def main():
    vehicles_dict = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5] 
        }

    MANUFACTURER_INDEX = 1
    MODEL_INDEX = 2
    COLOR_INDEX = 3

    # Ask the user for a vehicle identification number (VIN).
    vin = input("Please enter a VIN: ")

    if vin in vehicles_dict:
        answer = vehicles_dict[vin]
        manufacturer = answer[1]
        model = answer[2]
        color = answer[3]


        print("")
        print(f"Your vin is vinculated")
        print(f"Manufacturer: {manufacturer}")
        print(f"Model: {model}")
        print(f"Color: {color}")
        print("")
        print(f"Your car is an {color} {manufacturer} {model}")
        print("")
    else:
        print(f"{vin} is not in the dictionary.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
