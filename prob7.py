numeroa = float(input("Ingrese un primer número: "))
numerob = float(input("Ingrese un segundo número: "))
opcion = int(input("Introduzca la opción que desee mostrar, ya sea 1, 2 o 3: "))

primeraopc = float((numeroa)+(numerob))
segundaopc = float(numeroa) - float(numerob)
terceraopc = float(numeroa)*float(numerob)

if opcion == 1:
    print("La suma entre ambos números es " + str(primeraopc))

if opcion == 2:
    print("La resta entre ambos números es " + str(segundaopc))

if opcion == 3:
    print("La multiplicación entre ambos números es " + str(terceraopc))

if opcion != 1 and opcion != 2 and opcion != 3:
    print("La última opción ingresada no es correcta")