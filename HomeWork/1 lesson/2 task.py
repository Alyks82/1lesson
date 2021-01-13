# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

raw_time = int(input('Введите время в секундах '))

time_hours = raw_time // 3600
time_minutes = (raw_time - time_hours * 3600) // 60
time_seconds = raw_time % 60

print('Время {}:{:02d}:{:02d}'.format(time_hours,time_minutes,time_seconds)) # метод format, в других 0 не знаю как
