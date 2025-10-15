def changing_places(list_name):
    for i in range(len(list_name)):
        if list_name[i] == "AB":
            list_name[i] = "Alberta"
    return list_name


def read_list(filename):
    text_list=[]

    with open(filename,'rt') as text_file:
        for line in text_file:
            clean_line  = line.strip()
            text_list.append(clean_line)
    
    return text_list
 
def main():
    text_list = read_list('provinces.txt')
    text_list.pop(0)
    text_list.pop()
    changing_places(text_list)
    
    x = 0
    for i in range(len(text_list)):
        if text_list[i] == "Alberta":
            x+=1

    print(text_list)
    print(f"Alberta appears {x} times in the list.")

if __name__ == "__main__":
    main()

