consumo = float(input("¿Cuánto consumió en el restaurante?"))
propinamin = 0.15*float(consumo)
porcdepropinaelegida = input("La propina mínima es " + str(propinamin) + ", si no está de acuerdo, indique por favor el porcentaje que desea dejar: ")
montopropinaelegida = float(porcdepropinaelegida)*float(consumo)/100
print ("La propina a dejar será: " + str(montopropinaelegida))