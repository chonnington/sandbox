from tombola import Tombola
from random import randrange


@Tombola.register
class TomboList(list):  # Tombolist extends list.

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend  # Tombolist.load is the same as list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))