price = float (input ("Введите цену товара: "))
count = int (input ("Введите кол-во товара: "))

base_cost = price * count

if base_cost < 1000:
    discount_percent = 0
elif base_cost <= 5000:
    discount_percent = 5
else:
    discount_percent = 10

discount_amount = base_cost * discount_percent / 100
final_cost = base_cost - discount_amount

base_cost = round(base_cost, 2)
discount_amount = round(discount_amount, 2)
final_cost = round(final_cost, 2)

print("КАЛЬКУЛЯТОР СКИДКИ")
print(f"Цена за единицу товара:  {price} руб.")
print(f"Количество товара:       {count} шт.")
print(f"1. Базовая стоимость:    {base_cost} руб.")
print(f"2. Процент скидки:       {discount_percent} %")
print(f"3. Сумма скидки:         {discount_amount} руб.")
print(f"4. Итоговая стоимость:   {final_cost} руб.")