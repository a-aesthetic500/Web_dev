a = int(input())
b = int(input())
print( {True: 0, False: ({True: 1, False: 2}[a > b])}[a==b])