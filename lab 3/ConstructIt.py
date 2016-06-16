from functools import reduce

plant = []

while True:
    d = input()
    if not d:
        break
    plant.append(d)

plant = [a.split(' ') for a in plant]
parts = {part.pop(0): part[1:] for part in plant[1:] if len(part[1:]) > 0}
atoms = [a for a in plant if len(a) == 1]
atoms = reduce(lambda x, y: x + y, atoms) if atoms else []

is_constructable = 1

def make_plant(details):
    global is_constructable
    if isinstance(details, list):
        for detail in details:
            make_plant(detail)
    elif isinstance(details, str) and (details in atoms):
        is_constructable &= 1
    elif isinstance(details, str) and (details in parts):
        make_plant(parts[details])
    else:
        is_constructable &= 0

make_plant(plant[0][1:])
print('YES' if is_constructable else 'NO')