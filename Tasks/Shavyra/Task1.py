import math
# P - начальный депозит
# N - годовая ставка, разделенная на 100
# T - срок договора
P = float(input('Введите сумму начального депозита: '))
N = int(input('Введите желаемую годовую ставку (пример: 20): '))
t = int(input('Введите срок договора в годах (пример: 4): '))
# T = int(input('Введите срок договора в месяцах (пример: 48): '))
# D - Итоговый доход, итоговый доход, то есть размер вклада на конец срока включая сумму открытия и начисленный процент
# Форумула для T в месяцах:
# D = P*math.pow((1+(N/100)/12), T)
# Формула для t в годах
D1 = P*math.pow((1+(N/100)/12), (t*12))
# print('Сумма в конце указанного срока: ', "%.2f" % D)
print('Сумма на счету в конце указанного срока: ', "%.2f" % D1)