product=float(input("Price for product: "))
discount=int(input("Discount is: "))

DiscConv= discount/100

Disc=product*DiscConv

AfDisc=product-Disc

print(f"Product price: {product}")
print(f"Discount: {discount}")
print(f"Price with discount: {AfDisc:.2f}")
print(f"Reduction: {Disc:.2f}")