addresses = [
    " г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]

print("ОЧИСТКА АДРЕСОВ")

print("Исходные адреса:")
for a in addresses:
    print(f"  «{a}»")           



def clean_address(address):
    address = address.strip()                    
    address = address.replace(" ,", ",")
    address = address.replace(",", ", ")
    address = address.replace(",  ", ", ")

    for abbr in ["г.", "ул.", "д."]:             
        address = address.replace(abbr, abbr + " ")    
        address = address.replace(abbr + "  ", abbr + " ")

    address = " ".join(address.split())
    return address


cleaned = [clean_address(a) for a in addresses]

print("Очищенные адреса:")
for a in cleaned:
    print(f"  «{a}»")           

