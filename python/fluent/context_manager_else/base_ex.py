# -*- coding: utf-8 -*-

'''

for item in my_list:
    if item.flavor == 'banana':
        break
else:
    raise ValueError('No banana flavor found!')
    
'''

'''

with open('base_ex.py') as fp: 
    src = fp.read(60) 

print(len(src))
print(fp)
print(fp.closed, fp.encoding)

try:
    fp.read(60)
except ValueError:
    print('que')
    
'''
    
'''

But you can’t perform I/O with fp because at the end of 
the with block, the TextIOWrapper.__exit__ method is called 
and closes the file.

'''


class LookingGlass:
    
    def __enter__(self):
        
        import sys
        
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
        
    def __exit__(self, exc_type, exc_value, traceback):
        
        import sys
        
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

'''

with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)
print('Back to normal')

'''

manager = LookingGlass()

print(manager)

monster = manager.__enter__()

print(monster == 'JABBERWOCKY')
print(monster)
print(manager)

manager.__exit__(None, None, None)

print(monster)





