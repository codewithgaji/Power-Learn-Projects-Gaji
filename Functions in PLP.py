from ctypes import HRESULT


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        total = price - discount
        print(f"This is the amount you are to pay: {total}")
    else:
        result = price
        print("You don't have enough discount.\n")
        print(f"This is the amount you have to pay: {result}")

calculate_discount(350, 26)