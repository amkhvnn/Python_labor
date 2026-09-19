prices = {
    "Цемент": 450,
    "Песок": 300,
    "Кирпич": 25,
    "Бетон": 3800,
    "Дерево": 65
}

print("ПРАЙС-ЛИСТ МАТЕРИАЛОВ")
print(f"Исходный прайс-лист: {prices}")

prices["Гипсокартон"] = 320
prices["Газобетон"] = 780
print(f"После добавления 2 материалов: {prices}")

old_price = prices["Цемент"]
prices["Цемент"] = round(old_price * 1.10, 2)
print(f"Цена 'Цемент' изменена: {old_price} => {prices['Цемент']} руб. (+10%)")

removed = prices.pop("Песок")
print(f"Удалён материал: 'Песок' (цена была {removed} руб.)")

average_price = sum(prices.values()) / len(prices)
average_price = round(average_price, 2)

print(f"Итоговый прайс-лист: {prices}")
print(f"Количество материалов: {len(prices)}")
print(f"Средняя цена: {average_price} руб.")