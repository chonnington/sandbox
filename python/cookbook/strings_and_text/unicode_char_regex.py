
import re

pat = re.compile('stra\u00dfe', re.IGNORECASE)

s = 'straße'
print(pat.match(s))  # Matches <_sre.SRE_Match object at 0x10069d370>
print(pat.match(s.upper()))  # Doesn't match >>>
print(s.upper())  # STRASSE


'''
Mixing Unicode and regular expressions is often a good way 
to make your head explode. If you’re going to do it seriously, 
you should consider installing the third-party regex library, 
which provides full support for Unicode case folding, as well 
as a variety of other interesting features, 
including approximate matching.
'''