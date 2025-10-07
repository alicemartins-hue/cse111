import random

words = ['big','red', 'funny','baby','yellow','wait','python', 'japan', 'jabuticaba','tiramisu','jequitinhonha']

def main():
    numbers = [16.2, 75.1, 52.3]
    word_list = []
    print("")
    print(f" numbers list = {numbers}")
    append_random_numbers(numbers)
    print(f" number list = {numbers}")
    print("")
    append_random_numbers(numbers, 3)
    print(f" number list = {numbers}")

    print("")
    print("Random Words List:")
    append_random_words(word_list)
    print(word_list)
    append_random_words(word_list, 4)
    print(word_list)
    print("")

def append_random_words(words_list, quantity=1):
    for _ in range(quantity):
        words_list.append(random.choice(words))

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        num = random.uniform(0,100)
        num = round(num,1)
        print(f" + {num}")
        numbers_list.append(num)




if __name__ == "__main__":
    main()