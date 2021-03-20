######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'

cost1 = int(record[20:32]) * float(record[40:48])
print(record[20:32])
print(record[40:48])
print(cost1)

SHARES = slice(20, 32)
PRICE = slice(40, 48)
cost2 = int(record[SHARES]) * float(record[PRICE])

assert cost1 == cost2
print('noice')