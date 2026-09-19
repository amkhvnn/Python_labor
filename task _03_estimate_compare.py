T = float(input("Введите температуру в °C: "))

F = T * 9/5 + 32

if F <= 0:
    state = "Лёд"
elif F >= 100:
    state = "Пар"
else:
    state = "Жидкость"

print(f"КОНВЕРТЕР ТЕМПЕРАТУР \n")
print(f"Температура в °C: {T}\n")
print(f"Температура в F: {F}\n")
print(f"Состояние воды: {state}")