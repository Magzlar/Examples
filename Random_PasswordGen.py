import random 

ter = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_+=[}{"

password = ""
for t in range(15): 
    password += random.choice(ter)

print(password)