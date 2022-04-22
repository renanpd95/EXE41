import os,math

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
os.system('clear')

n1 = math.pow(n1,2)
n2 = math.pow(n2,2)
n3 = math.pow(n3,2)
n4 = math.pow(n4,2)

soma = n1+n2+n3+n4

print("O resultado da soma dos quadrados é: ",soma)
