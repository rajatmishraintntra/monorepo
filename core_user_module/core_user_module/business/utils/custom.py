class Sict(object):
    def __init__(self, dicth) -> None:
        for key, value in dicth.items():
            setattr(self, key, value)


class CustomDict(object):
    def set_attr(self, my_dict):
        return Sict(my_dict)
