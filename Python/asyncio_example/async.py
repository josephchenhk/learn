import types
import time
import asyncio

# 普通函数
def function():
    return 1

# 生成器很函数
def generator():
    yield 1

# 异步函数（协程）
async def async_function():
    return 1

# 异步生成器
async def async_generator():
    yield 1

# 直接调用异步函数不会返回结果，而是返回一个coroutine对象
print(type(function), type(function) is types.FunctionType)
print(type(generator()), type(generator()) is types.GeneratorType)
print(type(async_function()), type(async_function()) is types.CoroutineType)
print(type(async_generator()), type(async_generator()) is types.AsyncGeneratorType)