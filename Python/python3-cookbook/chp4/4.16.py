
class CallableObj:
    test_str = "hahaha"

    def __call__(self, *args, **kwargs):
        return self.test_str

print("CallableObj is callable: ", callable(CallableObj))
callable_obj = CallableObj()
print("CallableObj instance is callable(because it realized __call__): ", callable(callable_obj))
print("call result: ", callable_obj())
# 不停call callable_obj，直到遇到"hahaha"为止
for chunk in iter(callable_obj,"hahaha"):
    print(chunk)