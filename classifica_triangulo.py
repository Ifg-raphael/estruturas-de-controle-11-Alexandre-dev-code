# Sua solução aqui

# Exercicio de classificacao de Triangulos

# Leitura dos tres valores para o triangulo
a = int(input())
b = int(input())
c = int(input())

# Validacao para ver se e possivel formar
# um triangulo com esses tres valores
if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print("Não forma triângulo")

# Validacao para Triangulo Equilatero:
# precisa ter os tres lados iguais
elif (a == b) and (a == c):
    print("equilátero")

# Validacao para Triangulo Isosceles:
# precisa ter dois lados iguais e um diferente
elif (a == b) and (b != c):
    print("isósceles")

# Segundo caso de Triangulo Isosceles 
elif (a == c) and (c != b):
    print("isósceles")

# Terceiro caso para Triangulo Isosceles
elif (b == c) and (c != a):
    print("isósceles")

# Caso nao atenda a nenhum dos requisitos anteriores,
# entao esse triangulo e escaleno, com os tres
# lados possuindo valores diferentes
else:
    print("escaleno")