d = int(input())
a = int(input())
n = int(input())
chegada = n
diaria = 0

if chegada > 15:
    chegada = 15
    
diaria = d + (chegada-1) * a
print((31 - n + 1)*diaria)