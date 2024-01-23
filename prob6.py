edad = int(input("¿Cuál es su edad?: "))
if edad < 4:
    print("Puede entrar gratis")
if 4 <= edad <= 18:
    print("El costo de la entrada es $5")
if edad > 18:
    print("El costo de la entrada es $10")