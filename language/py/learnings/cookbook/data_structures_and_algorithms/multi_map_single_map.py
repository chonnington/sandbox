
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)

print(c['x'])  # Outputs 1  (from a)
print(c['y'])  # Outputs 2  (from b)
print(c['z'])  # Outputs 3  (from a)

print(len(c))  # 3
print(list(c.keys()))  # ['y', 'z', 'x']
print(list(c.values()))  # [2, 3, 1]

values = ChainMap()
values['x'] = 1

values = values.new_child()
values['x'] = 2

values = values.new_child()
values['x'] = 3

print(values)  # ChainMap({'x': 3}, {'x': 2}, {'x': 1})

print(values['x'])  # 3

values = values.parents
print(values['x'])  # 2

values = values.parents
print(values['x'])  # 1

print(values)  # ChainMap({'x': 1})

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

merged = dict(b)
merged.update(a)

print(merged['x'])  # 1
print(merged['y'])  # 2
print(merged['z'])  # 3

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

merged = ChainMap(a, b)

print(merged['x'])  # 1

a['x'] = 42

print(merged['x'])  # 42
