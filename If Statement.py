is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

elif is_cold:
    print("it's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy Your day")

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1* price
else:
    down_payment = 0.2*price

print(f"Down payment: ${down_payment}")