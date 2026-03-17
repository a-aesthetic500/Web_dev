x = int(input())
d = int(input())
c = 0
for i in range(len(str(x))):
    if(x%10==d):
        c+=1
    x=x//10

print(c)