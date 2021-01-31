from frozenjson import FrozenJSON as FrozenJSON
from frozenjson1 import FrozenJSON as FrozenJSON1

if __name__ == "__main__":

    example_dict = {'name': 'Jim Bo', 'class': 1982}

    grad = FrozenJSON(example_dict)
    print(grad.name)

    # grad.class  -- errors out
    print(getattr(grad, 'class'))

    grad1 = FrozenJSON1(example_dict)
    print(grad1.class_)