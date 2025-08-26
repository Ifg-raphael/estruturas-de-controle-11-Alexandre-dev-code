# Sua solução aqui
a = int(input())
b = int(input())
c = int(input())

if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print("Não forma triângulo")

elif (a == b) and (a == c):
    print("equilátero")

elif (a == b) and (b != c):
    print("isósceles")

elif (a == c) and (c != b):
    print("isósceles")

elif (b == c) and (c != a):
    print("isósceles")

else:
    print("escaleno")