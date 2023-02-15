## 入门案例：单个源文件(Demo1)

创建CmakeLists.txt
```
[CmakeLists.txt]

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

## 多个源文件
### (1) 同一目录，多个源文件 (Demo2)
修改CMakeLists.txt，加上 aux_source_directory方法
```
[CmakeLists.txt]

# CMake 最低版本号要求
cmake_minimum_required (VERSION 3.13)

# 项目信息
project (Demo2)

# 查找当前目录下的所有源文件, 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 指定生成目标
add_executable(Demo ${DIR_SRCS})
```
