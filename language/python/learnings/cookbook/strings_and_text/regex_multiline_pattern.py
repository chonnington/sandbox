import re


text1 = '/* this is a comment */'
text2 = '''/* this is a
                multiline comment */ ... '''


comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

'''
In this pattern, (?:.|\n) specifies a noncapture group 
(i.e., it defines a group for the purposes of matching, 
but that group is not captured separately or numbered).
'''

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))