print('Калькулятор вкладов')
a1 = int(input('введите сумму вклада: '))
a2 = int(input('введите процентную ставку в %: '))
a3 = int(input('введите срок вклада в годах: '))
x = a1*(1+((a2*30)/(100*365)))**(a3*12)
print('Cумма по истечении срока вклада составит: ', round(x, 2))
# альтернативный варинат вывода результата
print('-----Расчет дохода-----')
print(f'Вклад в размере {a1} по истечении {a3} лет принесет доход в размере {round(x-a1, 2)}')