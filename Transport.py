a = int(input('Enter distance in km: '))
b = float(input('Enter fuel price per liter: '))
c = float(input('Enter fuel consumption per 100 km (liters): '))

cost = (a / 100) * c
totalcost = cost*b

print(f'Total fuel consumption for {a} km: {cost:.2f} liters')
print(f'Total cost of transporting goods: {totalcost:.2f} currency units')