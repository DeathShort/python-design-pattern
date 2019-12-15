class Borg:
    __shared_state = None
    def __init__(self):
        if not self.__shared_state:
            Borg.__shared_state = self.__dict__
            self.x = 1
        else:
            self.__dict__ = Borg.__shared_state

a = Borg()
b = Borg()
print(a.__dict__)
print(b.__dict__)
a.x = 4

print(a.x)
print(b.x)