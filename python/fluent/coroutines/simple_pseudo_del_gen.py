
'''

========================================
RESULT = yield from EXPR
========================================

_i (iterator)
    The subgenerator.

_y (yielded)
    A value yielded from the subgnerator.

_r (result)
    The eventual result, i.e. the value of the yield from expression when the subgen‐ erator ends.

_s (sent)
    A value sent by the caller to the delegating generator, which is forwarded to the subgenerator.

_e (exception)
    An exception (always an instance of StopIteration in this simplified pseudocode).

'''

_i = iter(EXPR)

try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break

RESULT = _r


'''


'''

_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e

        '''
        this deals with exceptions thrown in by the caller using .throw(...). 
        Again, the subgenerator may be an iterator with no throw method to be called — 
        in which case the exception is raised in the delegating generator.
        
        '''
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break

RESULT = _r