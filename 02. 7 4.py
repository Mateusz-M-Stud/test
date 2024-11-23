import math  # module to use pi

circumference = float(input(f'Enter tree circumference in cm: '))

# diameter of the tree
diameter = circumference / math.pi
if diameter>=50:
    x=True
elif diameter<=50:
    x=False

if diameter>=50:
    print(f'Tree can be cut down: {diameter:.2f}')
    print(f'Tree can be cut down: {x}')
elif diameter<=50:
    print(f'Tree can be cut down: {diameter:.2f}')
    print(f'Tree can not be cut down: {x}')