def xor(a, n):
    return {True: 1, False: 0}[a!=n]

a, n = input().split()

print(xor(a, n))