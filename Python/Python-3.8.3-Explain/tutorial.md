python的源代码可以在python的官网www.python.org中下载

#重新编译

```
tar Jxvf  Python-3.8.3.tar.xz
cd Python-3.8.3
./configure --prefix=/usr/local/python3 # /usr/local/python3为你期望python安装到的路径: /Users/joseph/miniconda3/envs/python383
make
make install
```

#### 使用新编译的python编译器

```
cd /Users/joseph/miniconda3/envs/python383/bin
./python3  # 注意一定要加上./表示使用当前目录的python3，否则还是会调用系统默认的python3
```

例子：

```
joseph@Josephs-MacBook-Pro bin % ./python3
Python 3.8.3 (default, Jun 25 2020, 13:45:23)
[Clang 11.0.0 (clang-1100.0.33.12)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> l = [1,2,3]
>>> l[2]
3
>>> l[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: 哈哈哈，我被修改了！list index out of range
```

# Cython internals
Cython internals: interpreter and source code overview: Philip Guo
```
c = compile(open('test.py').read(), 'test.py', 'exec')
dir(c)
print(c.co_code)
print([byte for byte in c.co_code]) # in Py2, [ord(byte) for byte in c.co_code]

python -m dis test.py
```

用dis模块去disemble python byte code

```
joseph@Josephs-MBP Python-3.8.3-Explain % python
Python 3.7.1 (default, Dec 14 2018, 13:28:58)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import dis
>>> import test1
>>> test1.foo
<function foo at 0x104598c80>
>>> test1.bar
<function bar at 0x104598d08>
>>> dis.dis(test1.foo)
  4           0 LOAD_FAST                0 (x)
              2 LOAD_CONST               1 (2)
              4 BINARY_MULTIPLY
              6 STORE_FAST               1 (y)

  5           8 LOAD_GLOBAL              0 (bar)
             10 LOAD_FAST                1 (y)
             12 CALL_FUNCTION            1
             14 RETURN_VALUE
>>>
```

# Visualize Python Execution

http://pythontutor.com/visualize.html
