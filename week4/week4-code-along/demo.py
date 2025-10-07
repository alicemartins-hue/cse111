
#a code to show that a integer value passing to a function 
# dont change the original value on the original variable

def add_one(num):
    print(f"num inside function num = {num}")
    num+=1
    print(f"num inside function after adding 1, num = {num}")
    

var = 1
print(f"var before calling function var = {var}")
add_one(var)
print(f"var after calling function var = {var}")
