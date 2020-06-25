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