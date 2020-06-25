python的源代码可以在python的官网www.python.org中下载

重新编译

```
tar Jxvf  Python-3.8.3.tar.xz
cd Python-3.8.3
./configure --prefix=/usr/local/python3 # /usr/local/python3为你期望python安装到的路径: /Users/joseph/miniconda3/envs/python383
make
make install
```

使用新编译的python编译器

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