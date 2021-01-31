
text = 'yeah, but no, but yeah, but no, but yeah'

print(text == 'yeah')  # False

print(text.startswith('yeah'))  # True
print(text.endswith('no'))  # False
print(text.find('no'))  # 10

import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

datepat = re.compile(r'\d+/\d+/\d+')
n = datepat.match('11/27/2012')
print(n.group())

print('block #1')
if datepat.match(text1):
    print('yes')
else:
    print('no')

print('block #2')
if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')

print(m.groups())


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

print(datepat.findall(text))

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

for m in datepat.finditer(text):
    print(m.groups())