import inflect

p = inflect.engine()

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    pass

formatted_names = p.join(names)

print(f"\nAdieu, adieu, to {formatted_names}")
