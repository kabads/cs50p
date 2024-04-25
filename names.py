names = []


for _ in range(3):
    name = names.append(input("What's your name?"))

for name in sorted(names):
    print(f"Hello, {name}")

with open('names.txt', 'a') as f:
    for name in names:
        f.write(str(name) + "\n")


with open('names.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    print(line, end='')
