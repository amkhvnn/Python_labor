warehouse = {
    "Кирпич":    {"quantity": 5000, "price": 12.50,   "min_quantity": 1000},
    "Цемент":    {"quantity": 120,  "price": 450.00,  "min_quantity": 50},
    "Песок":     {"quantity": 8,    "price": 800.00,  "min_quantity": 10},
    "Дерево":  {"quantity": 30,   "price": 48000.00,"min_quantity": 20},
    "Бетон":     {"quantity": 45,   "price": 4200.00, "min_quantity": 15},
}

print("СИСТЕМА УЧЁТА СКЛАДА")

# --- 1. Таблица материалов ---
print("\n1. ТАБЛИЦА МАТЕРИАЛОВ")
print(f"{'Материал':<12} {'Кол-во':>10} {'Цена, руб':>12} {'Мин. остаток':>15}")
for name, data in warehouse.items():
    print(f"{name:<12} {data['quantity']:>10} {data['price']:>12.2f} {data['min_quantity']:>15}")

# --- 2. Самый дорогой материал ---
print("\n2. САМЫЙ ДОРОГОЙ МАТЕРИАЛ")
most_expensive = max(warehouse.items(), key=lambda item: item[1]["price"])
print(f"Материал: {most_expensive[0]}")
print(f"Цена:     {most_expensive[1]['price']:.2f} руб.")

# --- 3. Список критических остатков ---
print("\n3. КРИТИЧЕСКИЕ ОСТАТКИ")
critical = []
for name, data in warehouse.items():
    if data["quantity"] < data["min_quantity"]:
        critical.append(name)
        print(f" {name}: остаток {data['quantity']} < минимум {data['min_quantity']}")

if not critical:
    print("  Все остатки в норме.")
else:
    print(f"\nИтого критических позиций: {len(critical)}")

# --- 4. Моделирование выдачи со склада ---
print("\n4. ВЫДАЧА СО СКЛАДА")

def issue_material(name, amount):
    """Выдать amount единиц материала name со склада."""
    if name not in warehouse:
        return f"Ошибка: материала '{name}' нет на складе."
    if amount <= 0:
        return "Ошибка: количество должно быть положительным."
    if warehouse[name]["quantity"] < amount:
        return (f"Ошибка: недостаточно '{name}'. "
                f"Запрошено {amount}, доступно {warehouse[name]['quantity']}.")

    warehouse[name]["quantity"] -= amount
    remains = warehouse[name]["quantity"]
    result = f"Выдано {amount} ед. '{name}'. Остаток: {remains}."
    if remains < warehouse[name]["min_quantity"]:
        result += " Достигнут критический остаток!"
    return result

# Примеры выдачи
print(issue_material("Цемент", 30))
print(issue_material("Песок", 10))       # недостаточно
print(issue_material("Дерево", 15))    # станет критический остаток (30 - 15 = 15 < 20)
print(issue_material("Гипсокартон", 5))  # такого материала нет