# -*- coding: utf-8 -*-

################################################################
'''
tt = (1, 2, (30, 40))
tl = (1, 2, [30, 40]) 
tf = (1, 2, frozenset([30, 40]))

cont = (tt, tl, tf)
for i in cont:
    try: print(i, hash(i))
    except Exception as e: print(i, e)
'''
################################################################
'''
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

cont = (a, b, c, d, e)
print(a==b==c==d==e)
for i in cont: print(i)
'''
################################################################
'''
DIAL_CODES = [(86, 'China'),
              (91, 'India'),
              (1, 'United States'),
              (62, 'Indonesia'),
              (55, 'Brazil'),
              (92, 'Pakistan'),
              (880, 'Bangladesh'),
              (234, 'Nigeria'),
              (7, 'Russia'),
              (81, 'Japan'),]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

country_code_m = {code: country.upper() for country, code in country_code.items() if 
                  code < 100 and code > 75}
print(country_code_m)
'''
################################################################



