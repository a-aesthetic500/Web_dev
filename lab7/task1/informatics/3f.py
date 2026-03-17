x = input()
for i in range(len(x)):
    if x[len(x)-1]=="0":
        x = x[:len(x)-1]
    else:
        break
for i in range(len(x)):
    print(x[len(x)-i-1], end = "")