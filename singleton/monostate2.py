class CA:
    cls_pre = 'aaaa'
    __shared_state = {"1":"2"}
    def __init__(self):
        self.obj_pre = 'bbbb'
        self.__dict__ = self.__shared_state

a = CA()
b = CA()
a.obj_pre = 'xxxx'
print(a.cls_pre)
print(b.cls_pre)

CA.cls_pre = 'cccc'
CA.obj_pre = 'eeee'

c = CA()
d = CA()

d.cls_pre = 'dddd'
a.obj_pre = 'ffff'

print(a.cls_pre)
print(b.cls_pre)
print(c.cls_pre)
print(d.cls_pre)