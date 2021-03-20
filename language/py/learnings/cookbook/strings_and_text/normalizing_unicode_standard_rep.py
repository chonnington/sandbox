

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)  # 'Spicy Jalapeño'
print(s2)  # 'Spicy Jalapeño'
print(s1 == s2)  # False

print(len(s1), len(s2))


import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)

print(t1 == t2)  # True

print(ascii(t1))  # 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)

print(t3 == t4)  # True

print(ascii(t3))  # 'Spicy Jalapen\u0303o'

s = '\ufb01'

print(s)  # ﬁ
print(unicodedata.normalize('NFD', s))  # ﬁ
print(unicodedata.normalize('NFKD', s))  # fi
print(unicodedata.normalize('NFKC', s))  # fi


t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))  # 'Spicy Jalapeno'

