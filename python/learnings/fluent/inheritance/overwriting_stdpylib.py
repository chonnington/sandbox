import collections

# ====================================================


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
dd['two'] = 2
dd.update(three=3)

print(dd)

# ====================================================


class AnswerDict(dict):
    def __getitem__(self, key):
        return 42


ad = AnswerDict(a='foo')
print(ad['a'])

d = {}
d.update(ad)
d['a']

print(d)

# ====================================================


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict2(one=1)
dd['two'] = 2
dd.update(three=3)

print(dd)


class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42


ad = AnswerDict2(a='foo')
ad['a']

d = {}
d.update(ad)
d['a']

print(d)