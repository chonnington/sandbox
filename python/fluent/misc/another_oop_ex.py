# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/3394835/args-and-kwargs

#------------------------------------------------------------------------------

def foo(a, b, c, **args):
    print("a = %s" % (a,))
    print("b = %s" % (b,))
    print("c = %s" % (c,))
    print(args)

foo(a="testa", d="excess", c="testc", b="testb", k="another_excess")

#------------------------------------------------------------------------------

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    print("second normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')

#------------------------------------------------------------------------------

def print_everything(*args):
    for count, thing in enumerate(args):
        print( '{0}. {1}'.format(count, thing))
        
        
print_everything('apple', 'banana', 'cabbage')

#------------------------------------------------------------------------------

def table_things(**kwargs):
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))

print('kwargs')

d_ = {'a':1,'b':2,'c':3}
print(d_)

table_things(**d_)

table_things(apple = 'fruit', cabbage = 'vegetable')

#------------------------------------------------------------------------------

class Foo(object):
    def __init__(self, value1, value2):
        # do something with the values
        print(value1, value2)

class MyFoo(Foo):
    def __init__(self, *args, **kwargs):
        # do something else, don't care about the args
        print('myfoo')
        super(MyFoo, self).__init__(*args, **kwargs)

a = Foo(1,2)
b = MyFoo

#------------------------------------------------------------------------------

def func(required_arg, *args, **kwargs):
    # required_arg is a positional-only parameter.
    print(required_arg)

    if args: print(args)
    if kwargs: print(kwargs)

func("required argument") 
func("required argument", 1, 2, '3') 
func("required argument", 1, 2, '3', keyword1=4, keyword2="foo")


