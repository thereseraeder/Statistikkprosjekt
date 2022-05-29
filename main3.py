import numpy as np

x = []
y = []

with open('co2.txt', 'r') as file1:
    content = file1.read()
    lines = content.split('\n')
    for x, i in enumerate(lines):
        i = i.split(",")
        i.pop(-1)
        i[0] = i[0].strip()
        x.append(i[0])
        y.append(i[1])

print(x, y)