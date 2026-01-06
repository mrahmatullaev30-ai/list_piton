list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

son = []  

for t in list1:
    temp = list(t)  
    temp[-1] = 100  
    son.append(tuple(temp))  
print(son)

