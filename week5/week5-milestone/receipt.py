import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary."""
    s_dictionary = {}
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            key = row[key_column_index]
            s_dictionary[key] = row
    return s_dictionary


def main():
    try:
        KEY_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2

        products_dict = read_dictionary("products.csv", KEY_INDEX)
        print("All Products")
        print(products_dict)
        print("Requested Items")

        subtotal = 0
        total_items = 0

        with open("request.csv", 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader) 

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                product_info = products_dict[product_number]
                name = product_info[NAME_INDEX]
                price = float(product_info[PRICE_INDEX])

                print(f"{name}: {quantity} @ {price:.2f}")

                subtotal += quantity * price
                total_items += quantity



    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


if __name__ == "__main__":
    main()
