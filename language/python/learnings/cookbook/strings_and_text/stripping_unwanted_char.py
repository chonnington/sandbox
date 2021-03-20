import re

s = ' hello world \n'

print(s.strip())  # 'hello world'
print(s.lstrip())  # 'hello world \n'
print(s.rstrip())  # ' hello world'

t = '-----hello====='

print(t.lstrip('-'))  # 'hello====='
print(t.strip('-='))  # 'hello'

s = ' hello world \n'
s = s.strip()
print(s)  # 'hello world'

s.replace(' ', '')  # 'helloworld'
print(re.sub('\s+', ' ', s)) # 'hello world'

'''
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        ...
...

It’s efficient because it doesn’t actually read the data 
into any kind of temporary list first. It just creates 
an iterator where all of the lines produced have the stripping 
operation applied to them.

'''