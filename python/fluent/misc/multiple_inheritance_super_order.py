class a:
    def __init__(self):
        print(1)
        super().__init__()
    def display(self):
        print('a')
    
    
class b:
    def __init__(self):
        print(2)
        super().__init__()
    def display(self):
        print('b')
        
        
class c:
    def __init__(self):
        print(3)
        
        
class c(b, a, c):
    pass


C = c()


class First(object):
  def __init__(self):
    super(First, self).__init__()
    print("first")

    
class Second(object):
  def __init__(self):
    print("second")

    
class Third(First, Second):
  def __init__(self):
    super(Third, self).__init__()
    print("that's it")
    
    
x = Third()

    
