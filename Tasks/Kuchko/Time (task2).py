from datetime import datetime

current_time = datetime.now().time()
a = current_time.minute
b = current_time.hour

def time_as_it_is_current(a, b):
    if int(b) in h1.keys() and int(a) in m1.keys():          # если минуты от 1 до 30 и от 31 до 44
        print(current_time.strftime('%H:%M'))
        print(f"{m1.get(int(a))} {h1.get(int(b))}")

    elif int(b) in h1.keys() and int(a) in m2.keys():        # если минуты от 45 до 59
        print(current_time.strftime('%H:%M'))
        print(f"{m2.get(int(a))} {h2.get(int(b))}")

    elif int(b) == 00 and int(a) == 00:                      # если 00:00
        print(current_time.strftime('%H:%M'))
        print("полночь")

    elif int(a) == 30:                                       # если минуты равны 30
        print(current_time.strftime('%H:%M'))
        print(f"Половина {h1.get(int(b))}")

    elif int(b) in h3.keys() and int(a) == 00:               # если 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 и т д
        print(current_time.strftime('%H:%M'))
        print(f"Ровно {h3.get((int(b)))}")


h1 = {00: 'первого', 1: 'второго', 2: 'третьего', 3: 'четвертого', 4: 'пятого', 5: 'шестого',
      6: 'седьмого', 7: 'восьмого', 8: 'девятого', 9: 'десятого', 10: 'одинадцатого',
      11: 'двенадцатого', 12: 'первого', 13: 'второго', 14: 'третьего', 15: 'четвертого', 16: 'пятого',
      17: 'шестого', 18: 'седьмого', 19: 'восьмого', 20: 'девятого', 21: 'десятого', 22: 'одинадцатого',
      23: 'двенадцатого'}
h2 = {23: 'полночь', 0: 'час', 1: 'два', 2: 'три', 3: 'четыре', 4: 'пять', 5: 'шесть', 6: 'семь',
      7: 'восемь', 8: 'девять', 9: 'десять', 10: 'одинадцать', 11: 'двенадцать', 12: 'час', 13: 'два', 14: 'три', 15: 'четыре', 16: 'пять', 17: 'шесть', 18: 'семь', 19: 'восемь', 20: 'девять', 21: 'десять', 22: 'одинадцать', 23: 'двенадцать'}
h3 = {00: 'полночь', 1: 'час', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
      8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 13: 'час', 14: 'два',
      15: 'три', 16: 'четыре', 17: 'пять', 18: 'шесть', 19: 'семь', 20: 'восемь', 21: 'девять',
      22: 'десять', 23: 'одинадцать'}
m1 = {1: 'одна минута', 2: 'две минуты', 3: 'три минуты', 4: 'четыре минуты', 5: 'пять минут',
      6: 'шесть минут', 7: 'семь минут',
      8: 'восемь минут', 9: 'девять минут', 10: 'десять минут', 11: 'одинадцать минут',
      12: 'двенадцать минут', 13: 'тринадцать минут',
      14: 'четырнадцать минут', 15: 'пятнадцать минут', 16: 'шестнадцать минут', 17: 'семнадцать минут',
      18: 'восемьнадцать минут',
      19: 'девятнадцать минут', 20: 'двадцать минут', 21: 'двадцать одна минута', 22: 'двадцать две минуты',
      23: 'двадцать три минуты',
      24: 'двадцать четыре минуты', 25: 'двадцать пять минут', 26: 'двадцать шесть минут',
      27: 'двадцать семь минут', 28: 'двадцать восемь минут',
      29: 'двдцать девять минут', 30: 'половина', 31: 'тридцать одна минута', 32: 'тридцать две минуты',
      33: 'тридцать три минуты',
      34: 'тридцать четыре минуты', 35: 'тридцать пять минут', 36: 'тридцать шесть минут',
      37: 'тридцать семь минут', 38: 'тридцать восемь минут',
      39: 'тридцать девять минут', 40: 'сорок минут', 41: 'сорок одна минута', 42: 'сорок две минуты',
      43: 'сорок три минуты',
      44: 'сорок четыре минуты'}
m2 = {45: 'без пятнадцати минут', 46: 'без четырнадцати минут', 47: 'без тринадцати минут',
      48: 'без двенадцати минут', 49: 'без одинадцати минут',
      50: 'без десяти минут', 51: 'без девяти минут', 52: 'без восьми минут', 53: 'без семи минут',
      54: 'без шести минут', 55: 'без пяти минут',
      56: 'без четырех минут', 57: 'без трех минут', 58: 'без двух минут', 59: 'без одной минуты'}

time_as_it_is_current(a, b)

time = input("Введите время в формате h:m: ")
hours = time[0:2]
minutes = time[3:5]

def time_as_it_is(minutes, hours):
    if int(hours) in h1.keys() and int(minutes) in m1.keys():          # если минуты от 1 до 30 и от 31 до 44
        print(f"{m1.get(int(minutes))} {h1.get(int(hours))}")

    elif int(hours) in h2.keys() and int(minutes) in m2.keys():        # если минуты от 45 до 59
        print(f"{m2.get(int(minutes))} {h2.get(int(hours))}")

    elif int(hours) == 00 and int(minutes) == 00:                      # если 00:00
        print("полночь")

    elif int(minutes) == 30:                                           # если минуты равны 30
        print(f"Половина {h1.get(int(hours))}")

    elif int(hours) in h3.keys() and int(minutes) == 00:               # если 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 и т д
        print(f"Ровно {h3.get((int(hours)))}")


h1 = {00: 'первого', 1: 'второго', 2: 'третьего', 3: 'четвертого', 4: 'пятого', 5: 'шестого',
      6: 'седьмого', 7: 'восьмого', 8: 'девятого', 9: 'десятого', 10: 'одинадцатого',
      11: 'двенадцатого', 12: 'первого', 13: 'второго', 14: 'третьего', 15: 'четвертого', 16: 'пятого',
      17: 'шестого', 18: 'седьмого', 19: 'восьмого', 20: 'девятого', 21: 'десятого', 22: 'одинадцатого',
      23: 'двенадцатого'}
h2 = {23: 'полночь', 0: 'час', 1: 'два', 2: 'три', 3: 'четыре', 4: 'пять', 5: 'шесть', 6: 'семь',
      7: 'восемь', 8: 'девять', 9: 'десять', 10: 'одинадцать', 11: 'двенадцать', 12: 'час', 13: 'два', 14: 'три', 15: 'четыре', 16: 'пять', 17: 'шесть', 18: 'семь', 19: 'восемь', 20: 'девять', 21: 'десять', 22: 'одинадцать', 23: 'двенадцать'}
h3 = {00: 'полночь', 1: 'час', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
      8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 13: 'час', 14: 'два',
      15: 'три', 16: 'четыре', 17: 'пять', 18: 'шесть', 19: 'семь', 20: 'восемь', 21: 'девять',
      22: 'десять', 23: 'одинадцать'}
m1 = {1: 'одна минута', 2: 'две минуты', 3: 'три минуты', 4: 'четыре минуты', 5: 'пять минут',
      6: 'шесть минут', 7: 'семь минут',
      8: 'восемь минут', 9: 'девять минут', 10: 'десять минут', 11: 'одинадцать минут',
      12: 'двенадцать минут', 13: 'тринадцать минут',
      14: 'четырнадцать минут', 15: 'пятнадцать минут', 16: 'шестнадцать минут', 17: 'семнадцать минут',
      18: 'восемьнадцать минут',
      19: 'девятнадцать минут', 20: 'двадцать минут', 21: 'двадцать одна минута', 22: 'двадцать две минуты',
      23: 'двадцать три минуты',
      24: 'двадцать четыре минуты', 25: 'двадцать пять минут', 26: 'двадцать шесть минут',
      27: 'двадцать семь минут', 28: 'двадцать восемь минут',
      29: 'двдцать девять минут', 30: 'половина', 31: 'тридцать одна минута', 32: 'тридцать две минуты',
      33: 'тридцать три минуты',
      34: 'тридцать четыре минуты', 35: 'тридцать пять минут', 36: 'тридцать шесть минут',
      37: 'тридцать семь минут', 38: 'тридцать восемь минут',
      39: 'тридцать девять минут', 40: 'сорок минут', 41: 'сорок одна минута', 42: 'сорок две минуты',
      43: 'сорок три минуты',
      44: 'сорок четыре минуты'}
m2 = {45: 'без пятнадцати минут', 46: 'без четырнадцати минут', 47: 'без тринадцати минут',
      48: 'без двенадцати минут', 49: 'без одинадцати минут',
      50: 'без десяти минут', 51: 'без девяти минут', 52: 'без восьми минут', 53: 'без семи минут',
      54: 'без шести минут', 55: 'без пяти минут',
      56: 'без четырех минут', 57: 'без трех минут', 58: 'без двух минут', 59: 'без одной минуты'}

time_as_it_is(minutes, hours)