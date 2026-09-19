day_number = int(input("Введите номер дня недели (1-7): "))

if day_number == 1:
    day_name = "Понедельник"
    day_type = "Рабочий"
    schedule = "8:00 - начало смены"
elif day_number == 2:
    day_name = "Вторник"
    day_type = "Рабочий"
    schedule = "8:00 - начало смены"
elif day_number == 3:
    day_name = "Среда"
    day_type = "Рабочий"
    schedule = "8:00 - начало смены"
elif day_number == 4:
    day_name = "Четверг"
    day_type = "Рабочий"
    schedule = "8:00 - начало смены"
elif day_number == 5:
    day_name = "Пятница"
    day_type = "Рабочий"
    schedule = "8:00 - начало смены"
elif day_number == 6:
    day_name = "Суббота"
    day_type = "Выходной"
    schedule = "Отдых"
elif day_number == 7:
    day_name = "Воскресенье"
    day_type = "Выходной"
    schedule = "Отдых"
else:
    day_name = "—"
    day_type = "—"
    schedule = "Ошибка: введите число от 1 до 7"

print("РАБОЧИЙ ГРАФИК")
if 1 <= day_number <= 7:
    print(f"День недели:   {day_name}")
    print(f"Тип дня:       {day_type}")
    print(f"Режим:         {schedule}")
else:
    print(schedule)