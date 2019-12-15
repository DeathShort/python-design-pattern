#单一状态
class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object b:",b)
print("Borg Object b1:",b1)
print("Object state b:",b.__dict__)
print("Object state b1:",b1.__dict__)
