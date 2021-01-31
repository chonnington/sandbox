text = 'Hello World'

print(text.ljust(20))  # 'Hello World '
print(text.rjust(20))  # ' Hello World'
print(text.center(20))  # ' Hello World '

print(text.rjust(20, '='))  # '=========Hello World'
print(text.center(20, '*'))  # '****Hello World*****'

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20s'))

print(format(text, '*^20s'))
print('{:>10s} {:>10s}'.format('Hello', 'World'))

x = 1.2345

print(format(x, '>10'))
print(format(x, '^10.2f'))
