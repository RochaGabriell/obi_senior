n = int(input())
s = list(map(str, input()))
ss = ''.join(s[::-1])
maior = ""

for i in range(len(s)):
    aux = []
    for j in range(len(s)):
        aux = ''.join(s[i:j+1])
        if aux in ss:
            if len(aux) > len(maior):
                maior = aux

print(len(maior))
