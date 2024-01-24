hora = input('¿Qué hora es? ')
n = hora.index(':')
hora_numerica = int(hora[:n])

if 7 <= hora_numerica <= 8:
    print("Es hora de desayunar.")

if 8 < hora_numerica < 12:
    print("No es hora de comer.")

if 12 <= hora_numerica <= 13:
    print("Es hora de almorzar.")

if 13 < hora_numerica < 18:
    print("No es hora de comer.")

if 18 <= hora_numerica <= 19:
    print("Es hora de cenar.")

if 19 < hora_numerica:
    print("No es hora de comer")