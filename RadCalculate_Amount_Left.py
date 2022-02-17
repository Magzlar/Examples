import math

e = 0.5
nt = float(input("Enter current amount of radioactivity (CPM): "))
t = float(input("Enter amount of time passed (Days): "))

choice1 = input("Are you using 1) tritium or 2) Iodine 125 :")
choice1 = float(choice1)
    
if choice1 == 1 or "one" or "1":
        T = 365*12.5

elif choice1 == 2:
        T = 59.86
        
elif choice1 != 1 or 2:
        print("Thats not an option")

def func(nt,e,t, T):
    
    return nt*e**(t/T)

result = func(nt,e,t,T)

result1 = int(result)

print(result1, "CPM remain")

  
