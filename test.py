class Cls_01:
    _x : str | int = "0"

    @property
    def x(self) -> int:
        return int(self._x)
    @x.setter
    def x(self, value: int):
        self._x = value
    @x.setter
    def x(self, text: str):
        self._x = text


obj = Cls_01()
print(obj.x)

obj.x = 2
print(obj.x)

obj.x = "20"
print(obj.x)
