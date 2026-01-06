a = int(input("a = "))
b = int(input("b = "))

sonlar = [] 

for x in range(a, b): 
    if x % 2 == 0:     
        sonlar.append(x) 

print("=" , sonlar)