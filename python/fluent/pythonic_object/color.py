
class Color0:

    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


# c = Color0("#ff0000", "bright red")
# print(c.get_name())
# c.set_name("red")
# print(c.get_name())


class Color1:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name


# c = Color1("#ff0000", "bright red")
# print(c.name)
# c.name = "red"


class Color2:

    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(fget=_get_name,
                    fset=_set_name,
                    fdel=None,
                    doc=None)

c = Color2("#0000ff", "bright red")
print(c.name)
c.name = "red"
print(c.name)