print("-------------------------------------------------------")
print("Trabajo 12")
print("-------------------------------------------------------")

print("Ingrese la fecha: ")
a = int( input("Año: "))
m = int( input("Mes: "))
d = int( input("Dia: "))

print("\nSALIDA: ")
print("-------------------------------------------------------")

if d > 0 and d < 30 :
print("Mañana es:", d+1, m, a)

else:
if m > 0 and m < 12 :
print("Mañana es:", 1, m+1, a)

else:
print("Mañana es:", 1, 1, a+1)