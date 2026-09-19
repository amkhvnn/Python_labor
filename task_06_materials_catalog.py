materials = ["Цемент", "Песок", "Кирпич", "Бетон", "Дерево"]

print("КАТАЛОГ МАТЕРИАЛОВ")
print(f"Исходный список: {materials}")

print(f"Первый элемент:      {materials[0]}")
print(f"Последний элемент:   {materials[-1]}")
print(f"Средние элементы:    {materials[1:4]}")   
materials.append("Гипсокартон")     
materials.append("Газобетон")
print(f"После добавления 2 материалов: {materials}")

removed = materials.pop(1)          
print(f"Удалён элемент: {removed}")

print(f"Итоговый список: {materials}")
print(f"Длина списка:    {len(materials)}")