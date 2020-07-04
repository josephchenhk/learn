## 入门案例：单个源文件(Demo1)

创建CmakeLists.txt
```
# CMake 最低版本号要求
cmake_minimum_required (VERSION 3.13)

# 项目信息
project (Combination)

# 指定生成目标
add_executable(comb combination.c)
```


构建程序
用cmake来编译这段代码，进入命令行执行内部构建命令（后边会讲外部构建）：

```
cmake .
```

同时生成了三个文件CMakeCache.txt、Makefile、cmake_install.cmake和一个文件夹CmakeFiles,然后执行

```
make 
```

复制代码
即可生成可执行程序comb

