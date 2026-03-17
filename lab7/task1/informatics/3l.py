n = int(input())
c = 0
for i in range(len(str(n))):
    if n%10 == 1:
        c += 2**i
    n=n//10

print(c)