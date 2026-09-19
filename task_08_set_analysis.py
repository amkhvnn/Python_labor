contractor1 = ["Цемент", "Песок", "Кирпич", "Бетон", "Дерево"]
contractor2 = ["Кирпич", "Бетон", "Гипсокартон", "Газобетон", "Дерево"]
contractor3 = ["Бетон", "Дерево", "Цемент", "Газобетон", "Стекло"]

print("АНАЛИЗ ЗАКАЗОВ ТРЁХ ПОДРЯДЧИКОВ")
print(f"Подрядчик 1: {contractor1}")
print(f"Подрядчик 2: {contractor2}")
print(f"Подрядчик 3: {contractor3}")

set1 = set(contractor1)
set2 = set(contractor2)
set3 = set(contractor3)

# 1. Все уникальные материалы 
all_unique = set1 | set2 | set3

# 2. Общие для всех (пересечение)
common_all = set1 & set2 & set3

# 3. Только у первого подрядчика
only_first = set1 - set2 - set3

# 4. У двух подрядчиков
only_two = (set1 & set2) | (set1 & set3) | (set2 & set3)
only_two = only_two - common_all

print(f"1. Все уникальные материалы ({len(all_unique)} шт.):")
print(f"   {sorted(all_unique)}")
print()

print(f"2. Общие для всех трёх подрядчиков ({len(common_all)} шт.):")
print(f"   {sorted(common_all)}")
print()

print(f"3. Только у первого подрядчика ({len(only_first)} шт.):")
print(f"   {sorted(only_first)}")
print()

print(f"4. Ровно у двух подрядчиков ({len(only_two)} шт.):")
print(f"   {sorted(only_two)}")
