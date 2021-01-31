print()

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


res1 = [x*3 for x in gen_AB()]
print(type(res1))

for r in res1:
    print(r)

print()

res2 = (x*3 for x in gen_AB())
print(type(res2))

for r in res2:
    print(r)

