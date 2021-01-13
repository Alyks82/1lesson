# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = 2
b = 3
day_count = 1

while a < b:
    day_count += 1
    a *= 1.1
    print('На {}-й день спортсмен пробежал {:01.1f} км'.format(day_count,a))

print(f'Таким образом номер дня {day_count}')


