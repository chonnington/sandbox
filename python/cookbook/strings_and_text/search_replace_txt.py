

import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
print(text)
text = text.replace('yeah', 'yep')
print(text)

text = 'Today is 01/31/2019. PyCon starts 03/13/2019.'
print(text)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    print(m.group(1), mon_name)
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))


print(datepat.sub(change_date, text))

newtext, n = datepat.subn(r'\3-\1-\2', text)

print(newtext, n)
