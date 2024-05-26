import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
print("welcome to pypassword generator!")
nr_letters = int(input("how many letters you want in your password?\n"))
nr_digits = int(input("how many digits you want in your password?\n"))
nr_symbols = int(input("how many symbols you want in your password?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
    
for char in range(1, nr_digits + 1):
    password_list += random.choice(digits)
    
for char in range(1, nr_symbols + 1):
    password_list +=  random.choice(symbols)

random.shuffle(password_list)
print(password_list)

password= ""
for char in password_list:
    password += char

print("your password is:",password)    

