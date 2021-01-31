
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {ord('\t') : ' ',
         ord('\f') : ' ',
         ord('\r') : None}

a = s.translate(remap)
print(a)

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)

print(b.translate(cmb_chrs))

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd' }

print(len(digitmap))
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

print(a)

b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
