#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

par = 0
impar= 0
numero= 0
for i in range(10):
   numero= int(input('Informe o valor: '))
   if numero % 2 == 0:
    par= par + 1
   else:
    impar= impar + 1
    
print("Pares:", par)
print("Impares:", impar)

