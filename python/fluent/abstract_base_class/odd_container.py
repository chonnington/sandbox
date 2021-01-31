from collections import Container

print(Container.__abstractmethods__)
print(help(Container.__contains__))


class OddContainer:

    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True


odd_container = OddContainer()

print(isinstance(odd_container, Container))
print(issubclass(OddContainer, Container))
