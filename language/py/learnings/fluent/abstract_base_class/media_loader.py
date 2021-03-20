import abc


class MediaLoader(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractclassmethod
    def stop(selfs):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

    
class Wav(MediaLoader):
    pass


# x = Wav()


class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        pass
    def stop(self):
        pass

    
o = Ogg()


class Ogg1():
    ext = '.ogg'
    def play(self):
        print("this will play an ogg file")
    def stop(self):
        pass

print(issubclass(Ogg1, MediaLoader))
print(isinstance(Ogg1(), MediaLoader))
