print("-------------------------------------------------------")
print("Complemento8")
print("-------------------------------------------------------")

PI = 3.1416

print("Ingrese valores del menu:")
print("1: area del triangulo:")
print("2: area del circulo:")

Opc = int( input("Opc: "))

if Opc == 1 :
print("area del triangulo")
print("Ingrese el lado d0el triangulo")

L = float( input("L: "))
A = ( (3 ** 0.5)/ 4) * L**2

print("\nEl area del triangulo es:", A)
elif Opc == 2:

print("area del Circulo")
print("Ingrese el radio del circulo")

R = float( input("R: "))
C = PI * R**2

print("\nEl area del circulo es:", C)

else:
print("\nerror")