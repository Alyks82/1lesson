# 1.Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
name = 'Aleksandr'
surname = 'Lykov'
age = 38

print(name, surname, age, sep='*')

print(type(name))
print(type(surname))
print(type(age))

pet_name = input('Сообщите имя своего питомца ')
maiden_name = input('Введите девичью фамилию Вашей мамы ')

print(f'Никогда не используй в паролях {pet_name},{maiden_name} и 123456789')
