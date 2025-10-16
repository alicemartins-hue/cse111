import csv


def read_dictionary(filename,key_column_index):
    """return dictionary"""
    s_dictionary = {}
    with open(filename,'rt') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        next(csvreader)
        for row in csvreader:
            key_value = row[key_column_index]
            s_dictionary[key_value] = row
    return s_dictionary

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    request_dict = {}
    product = read_dictionary("products.csv",KEY_INDEX)
    
    with open("request.csv",'rt') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        next(csvreader)
        for row in csvreader:
            key_value = row[KEY_INDEX]
            request_dict[key_value] = row

    for request in request_dict:
        x = request_dict

if __name__ == "__main__":
    main()
