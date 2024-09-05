import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbol = ["!","#","@","$","&","*","(",")"]

print("\t\t\t*************Password Generator*************\n\n\n")
lett = int(input("Number of Letters:\n"))
num = int(input("Number of numeric values:\n"))
sym = int(input("Number of Symbols:\n"))

password_list = []

for char in range(1,lett+1):
    random_let = random.choice(letters)
    password_list.append(random_let)
    
for char in range(1,num+1):
    random_let = random.choice(numbers)
    password_list.append(random_let)
    
for char in range(1,sym+1):
    random_let = random.choice(symbol)
    password_list.append(random_let)

random.shuffle(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")