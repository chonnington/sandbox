
import re

text2 = 'Computer says "no." Phone says "yes." "WTF.YO?"'

str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))