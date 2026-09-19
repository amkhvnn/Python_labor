length = 5         # длина помещения, м
width = 3          # ширина помещения, м
height = 3          # высота помещения, м
paint_price = 100     # стоимость покраски, руб/м²

S_пола = length * width

P = 2 * (length + width)
S_стен = P * height

V = length * width * height

paint_cost = S_стен * paint_price

S_пола = round(S_пола, 2)
S_стен = round(S_стен, 2)
V = round(V, 2)
paint_cost = round(paint_cost, 2)

print("=" * 45)
print("ПАРАМЕТРЫ ПОМЕЩЕНИЯ")
print("=" * 45)
print(f"Длина:            {length} м")
print(f"Ширина:           {width} м")
print(f"Высота:           {height} м")
print("-" * 45)
print(f"Площадь пола:     {S_пола} м²")
print(f"Площадь стен:     {S_стен} м²")
print(f"Объём помещения:  {V} м³")
print("-" * 45)
print(f"Цена покраски:    {paint_price} руб/м²")
print(f"Стоимость покраски стен: {paint_cost} руб.")
print("=" * 45)