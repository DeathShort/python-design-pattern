class LazySingleton:
    __instance = None
    def __init__(self):
        if not self.__instance:
            print('__init__ mothed not called')
        else:
            print('instance already created,',self.get_instance())
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

a = LazySingleton()
print(a.__dict__)


print(LazySingleton.get_instance())
b = LazySingleton()