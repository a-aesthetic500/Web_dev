x = int(input())
c = 0
for i in range(len(str(x))):
    c+=x%10
    x=x//10
print(c)