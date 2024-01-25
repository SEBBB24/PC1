hora = input('Ingresa una hora del día: ')
n = hora.index(':')
hora_num1 = int(hora[:n])
hora_num2 = int(hora[n+1:])

if (7 <= hora_num1 < 8) or (hora_num1 == 8 and hora_num2 == 00):
    print("Es hora de desayunar.")
elif (12 <= hora_num1 < 13) or (hora_num1 == 13 and hora_num2 == 00):
    print("Es hora de almorzar.")
elif (18 <= hora_num1 < 19) or (hora_num1 == 19 and hora_num2 == 00):
    print("Es hora de cenar.")