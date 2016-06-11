# Generated by Haxe 3.3.0

import numpy as NumPy


class KwCall:
    __slots__ = ()


class IterableAdaptor:
    __slots__ = ()

    @staticmethod
    def iterator(it):
        _this_x = it
        return python_HaxeIterator(_this_x.__iter__())


class IteratorAdaptor:
    __slots__ = ()

    @staticmethod
    def iterator(it):
        return python_HaxeIterator(it)


class DynamicIterationAdaptor:
    __slots__ = ()

    @staticmethod
    def iterator(it):
        _this_x = it
        return python_HaxeIterator(_this_x.__iter__())


class Script:
    __slots__ = ()

    @staticmethod
    def main():
        kwArgs = dict()
        kwArgs["delimiter"] = ","
        world_alcohol = NumPy.genfromtxt("world_alcohol.csv",**kwArgs)
        print(str(world_alcohol.dtype))


class python_HaxeIterator:
    __slots__ = ("it", "x", "has", "checked")

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except Exception as _hx_e:
                _hx_e1 = _hx_e
                if isinstance(_hx_e1, StopIteration):
                    s = _hx_e1
                    self.has = False
                    self.x = None
                else:
                    raise _hx_e
            self.checked = True
        return self.has




Script.main()