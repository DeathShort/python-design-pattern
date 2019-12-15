# 单一实例模式
# 运行期间只有一个实例，避免与其他实例发生相互冲突的请求
class Singleton:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

a = Singleton()
b = Singleton()
print(a)
print(b)