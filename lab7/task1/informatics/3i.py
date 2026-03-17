x = int(input())
c = 0
for d in range(1, x + 1):  
    if x % d == 0:      
        c += 1 

print(c)