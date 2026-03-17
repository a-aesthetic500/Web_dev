n = int(input())  
arr = list(map(int, input().split()))  
c= 0
for num in arr: 
    if num > 0:  
        c += 1
print(c)