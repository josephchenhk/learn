# Q Language

在docker下启动Q console：

```shell
> docker pull aakashsinghishere/kdb_docker_centos:latest

# 在5001端口启动一个q process（名字起作qserver）
> docker run -it -v /Users/joseph/Dropbox/code/learn/Q:/tmp --name qserver aakashsinghishere/kdb_docker_centos:latest q -p 5001

# 在5002端口启动一个q process（名字起作qclient）
> docker run -it -v /Users/joseph/Dropbox/code/learn/Q:/tmp --name qclient --link qserver aakashsinghishere/kdb_docker_centos:latest q -p 5002
```

## 1 Introduction

與傳統編程語言不同，Q programming：

* 沒有work flow的概念，不存在if-else這樣的語句結構
* 沒有object的概念，不存在繼承的關係
* 沒有thread的概念
* 沒有shared mutable globals

## 2 Q Console, Types and Lists

Q是動態類型語言，無需顯式指定類型。

|描述       | Q      | Python |        解釋     |
|:--------:|:------:|:------:|:--------------:|
|加        | +      |   +     |                |
|減        | -      |   -     |                |
|乘        | *      |   *     |                |
|除        | %      |   /     | Python %表示取餘數|
|布爾值     | 1b, 0b |True,False|                |
|64位整數   | 42     |   42    |                |
|32位整數   | 42i    |   42    |                |
|浮點數     | 42f    |   42    |Q只要寫小數點就會當成浮點數，例如42.0|
|數值列表   | 1 2 3  |[1,2,3]  | Q numeric List只用空格分開|
|布爾值列表  | 101b  |[True,False,True]  | Q boolean List不用任何分隔符，只需在最後加上b|

列表相加（element-wise）：

```shell
q)） 1 2 3+4 6 7
5 8 10
```

## 3 Q Operators & Operator Precedence

### count

計算一個列表有多少個元素用count

```shell
q))count 1 2 3
3
```

### scalar and vector

將一個標量（scalar）與矢量（vector）相作用，相當於對每一個元素操作：

```shell
q))5+1 2 3
6 7 8
q))1 2 3+5
6 7 8
q))2%1 2 3
2 1 0.6666667
q))1 2 3%2
0.5 1 1.5
```

### precedence

Q 沒有precedence（符合運算優先次序），所有的運算遵循**從右至左**的次序。當然，可以加上括號令其優先級更高。

```shell
q))2*3+4
14
q))2*(3+4)
14
q))(2*3)+4
10
```

### til

`til N`表示返回一個從0開始，步長為1，總長度為N的列表

```shell
q))til 4
0 1 2 3
q))count til 10000
10000
q))1+til 10000
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29..
```

## 4 Booleans and Temporal Data Types

### Boolean

Q直接用等號（=），而不是雙等號（==）作比較運算符

```shell
q))1011b
1011b
q))42=6*7
1b
q))1 2 3=10 2 30
010b
```

### Date

Date在Q語言裡，代表了自千禧年（2000）以來的天數，即2000.01.01那一天是0，往後每一天加上1，往前每一天減去1

```shell
q))2020.12.28
2020.12.28
q))2000.01.01=0
1b
q))2000.01.03-3
1999.12.31
```

如果只想精確到月份，只需要在月份後面加上m

```shell
q))2000.01m
2000.01m
q))2000.01m=0
1b
q))1999.12m=-1
1b
q))2000.01.01=2000.01m
1b
```

## 5 Casting and Date Operators

Casting表示強制類型轉換。語法格式很簡單，就是``` `(type)$(value)```

```shell
q))`long$1.0
1
q))`float$1
1f
q))`float$1b
1f
q))`date$3
2000.02.01
```

## 6 Operations on Lists

Generally speaking, ``/``符號表示iterate across整個List

### Cumulative

```(op/) (List)```表示對List的每一個元素進行op操作，並將結果累積起來

```shell
q))0 +/ 10 20 30 40 50
150
q))(+/) 10 20 30 40 50
150
q))(*/) 1 2 3 4 5
120
q))(*/) 1+til 5
120
```

### Max & Min

``|``表示返回兩者中較大值，`&`表示返回兩者中較小值

```shell
q))4|5
5
q))4&5
4
q))(|/) 10 30 20 50 40
50
q))(&/) 10 30 20 50 40
10
```

### Alias: sum, max, min

```shell
q))sum 10 30 20 50 40
150
q))max 10 30 20 50 40
50
q))min 10 30 20 50 40
10
```

### forward slash (/) and backward slash (\\)

與正斜槓（/）的區別是，反斜槓 （\\）保留了所有的中間結果：

```shell
q))(+/) 10 20 30 40 50
150
q))(+\) 10 20 30 40 50
10 30 60 100 150
```

### Alias: sums, maxs, mins

```shell
q))sums 10 30 20 50 40
10 40 60 110 150
q))maxs 10 30 20 50 40
10 30 30 50 50
q))mins 10 30 20 50 40
10 10 10 10 10
```

### Retrieving from a list

用符號`n#`去獲取一個列表的前n個元素（n大於0），或後n個元素（n小於0）

```shell
q)2#10 20 30 40 50
10 20
q)-3#10 20 30 40 50
30 40 50
```

### Concatenate two lists

用符號`,`將兩個list連接起來

```shell
q)1 2, 6 5 4 3
1 2 6 5 4 3
```

### First and Last

取出列表的第一個元素和最後一個元素

```shell
q)first 10 20 30 40 50
10
q)last 10 20 30 40 50
50
```

## 7 Defining Functions

用花括號定義一個函數，當輸入變量是x時，可以省略

```shell
q)){[x] x*x}
{[x] x*x}
q)){[x] x*x}4
16
q)){[x] x*x}[4]
16
q)){x*x}4
16
```

多個變量，用分號（ ;）隔開。

```shell
q)){[x;y] x:x+1; x*y}[2;4]
12
```

## 8 Functional Examples: Newton Raphson and Fibonacci Sequence

### Newton Raphson

假設我們有一個函數`f(x)=x^2-1`，我們想找出`f(x)=0`的解。根據牛頓算法，如果`x_n`是方程`f(x)=0`的一個近似解，則`x_n+1=x_n - f(x_n)/f'(x_n)`
是一個更好的解。

```shell
q)))){[xn] xn - (-2+xn*xn)%(2*xn)}\[1.0]
1 1.5 1.416667 1.414216 1.414214 1.414214
q)))){[xn] xn + (2-xn*xn)%2*xn}\[1.0]
1 1.5 1.416667 1.414216 1.414214 1.414214

# 注意q的運算規則是由右至左，下面這樣寫，(xn*xn-2)這項其實等價於 xn*(xn-2)

q)))){[xn] xn - (xn*xn-2)%(2*xn)}\[1.0]
1 1.5 1.75 1.875 1.9375 1.96875 1.984375 1.992188 1.996094 1.998047 1.999023 ..
q)))){[xn] xn - (xn*(xn-2))%(2*xn)}\[1.0]
1 1.5 1.75 1.875 1.9375 1.96875 1.984375 1.992188 1.996094 1.998047 1.999023 ..
```

### Fibonacci Sequence

在q裡定義一個Fibonacci序列很簡單：

```shell
q){x,sum -2#x} 1 1
1 1 2

# 由(1 1)開始，iterate 10次
q){x,sum -2#x}/[10;1 1]
1 1 2 3 5 8 13 21 34 55 89 144
```

## 9 Functions Examples: Variables

### deltas

deltas作用於一個列表上，將返回該列表元素的diff。注意第一個元素返回的是其本身：

```shell
q)deltas 10 20 30 40 50
10 10 10 10 10

# 注意返回的第一個元素是本身
q)deltas 110 120 130 140 150
110 10 10 10 10

# 先返回一個累加的列表，再計算diff
q)deltas sums 110 120 130 140 150
110 120 130 140 150

# 先計算diff，再返回累加的列表
q)sums deltas 110 120 130 140 150
110 120 130 140 150
```

留意上述操作，deltas實際上unwind了sums的操作。

### variables

用`:`來給variables賦值（assign values）：

```shell
q)a:42
```

在q語言裡，`:`用來賦值；`=`用來比較。與之對應，在傳統編程語言裡，通常`=`用來賦值；而`==`用來比較。

### A sample: allocate buys

以下例子展示如何根據給定的sell數量，分配buys：

```shell
q)buys: 2 1 4 3 5 4
q)sell:12

# sums對buys進行累加，然後用sell去取cap
q)sell&sums buys
2 3 7 10 12 12

# 如果想獲得每筆交易的buy數目
q)deltas sell&sums buys
2 1 4 3 2 0
```

## 10 Tables

傳統編程語言（例如MySQL）裡，table是collection of rows；但在Q語言裡，table是collection of columns。columns即是Q裡面的list，所以對於table的
操作，實際上是對table裡的list（即columns）進行操作，是一種vector operations，所以非常快。

```shell
# 創建table，由創建column開始。我們先創建一個10000000個屬於2018年1月份的random日期
q)dates:2018.01.01+10000000?31
q)count dates
10000000

# 同樣地，我們創建10000000個隨機的時間戳
q)times:10000000?24:00:00.0000

# 接著，我們創建10000000個在範圍100到10000以內的隨機數字，作為qty
q)qtys:100*1+10000000?100
q)qtys
4300 4000 5700 9100 8000 2400 500 1900 2500 7300 2500 7200 1200 3700 5800 310..

# 假設我們考慮3隻股票，我們先創建index
q)ixs:10000000?3
q)ixs
2 0 1 2 2 1 0 2 0 1 1 0 0 2 1 2 0 2 1 0 2 2 1 2 0 1 0 2 1 1 1 2 0 2 2 1 2 2 1..

# 然後將三隻股票名字影射到index裡
q)syms:`appl`amzn`googl` ixs
q)syms
`googl`appl`amzn`googl`googl`amzn`appl`googl`appl`amzn`amzn`appl`appl`googl`a..

# 給價格一個隨機浮動3%的幅度
q)pxs:(1+10000000?.03)*172.0 1189.0 1073.0 ixs
q)pxs
1080.679 172.5521 1211.08 1104.971 1097.452 1193.656 175.9138 1087.95 172.029..

# 現在我們可以創建我們的table了
q)t:([] date:dates;time:times;sym:syms;qty:qtys;px:pxs)

# 對table按日期和時間進行升序排序
q)t:`date`time xasc t

# 取出前5個row看一下
q)5#t
date       time         sym  qty  px
------------------------------------------
2018.01.01 00:00:01.129 appl 8800 174.7627
2018.01.01 00:00:02.099 amzn 8000 1198.197
2018.01.01 00:00:02.670 appl 1400 175.7161
2018.01.01 00:00:02.885 amzn 9300 1223.15
2018.01.01 00:00:03.396 appl 7600 175.518
```

## 11 qSQL

SQL-like syntax對q-table進行查詢

```shell
q)select date,time,sym,qty,px from 5#t where sym=`appl
date       time         sym  qty  px
------------------------------------------
2018.01.01 00:00:01.129 appl 8800 174.7627
2018.01.01 00:00:02.670 appl 1400 175.7161
2018.01.01 00:00:03.396 appl 7600 175.518

# 在前面加上\t表示計算運算時間
q)\t select date,time,sym,qty,px from t where sym=`appl
81

# 選出appl公司每天的開盤價和收盤價
q)5#select open:first px, close:last px by date from t where sym=`appl
date      | open     close
----------| -----------------
2018.01.01| 174.7627 174.5251
2018.01.02| 172.6117 175.7077
2018.01.03| 176.2038 177.1559
2018.01.04| 175.5028 176.1028
2018.01.05| 173.9064 176.6098

# 選出appl公司每天的開盤價和收盤價，最高價和最低價（OCHL）
q)5#select open:first px, close:last px, high:max px, low:min px by date from t where sym=`appl
date      | open     close    high     low
----------| -----------------------------------
2018.01.01| 174.7627 174.5251 177.1599 172.0001
2018.01.02| 172.6117 175.7077 177.16   172
2018.01.03| 176.2038 177.1559 177.16   172
2018.01.04| 175.5028 176.1028 177.16   172
2018.01.05| 173.9064 176.6098 177.16   172
```

## 12 Complex Queries

### wavg

weight-average命令，前面代表權重（weights），後面代表要加權的數值（values）

```shell
# 以下表示(4*10 + 3*20 + 2*30 + 1*40) / (4+3+2+1)
q)4 3 2 1 wavg 10 20 30 40
20f
```

### xbar

`N xbar (list)`表示以N作為interval，對右邊的list每一個元素取bar（即看它落在哪一個interval區間）

```shell
# 劃分區間為[0,5), [5,10), [10,15), [15,20), [20,25), ...
q)5 xbar 0 1 2 3 4 5 10 11 21
0 0 0 0 0 5 10 10 20
```

### complex queries

如果以每天對低價買入，然後計算每天的最高profit，可以如下計算：

```shell
q)select max px - mins px by date from t where sym=`appl
date      | px
----------| --------
2018.01.01| 5.159831
2018.01.02| 5.159934
2018.01.03| 5.159926
2018.01.04| 5.159944
2018.01.05| 5.159916
2018.01.06| 5.159867
2018.01.07| 5.159898
2018.01.08| 5.159942
2018.01.09| 5.159739
2018.01.10| 5.159922
2018.01.11| 5.159891
2018.01.12| 5.159866
2018.01.13| 5.159896
2018.01.14| 5.159875
2018.01.15| 5.159907
2018.01.16| 5.159866
2018.01.17| 5.159862
2018.01.18| 5.159782
2018.01.19| 5.159972
2018.01.20| 5.159882
..
```

## 13 Interprocess Communication

`\p (port)`表示打開某個port

在server端： 

```shell
# 打开一个端口4242
q)\p 4242

# 在server端，定义一个函数cub3
q)cub3:{x*x*x}

# 在前面加上0N!代表将后面的结果即时输出至当前console
q)cub3:{0N!x*x*x}
q)125
```

在client端：

```shell
# 通过hopen `:[server name]:[port]连接至进程4242
q)h:hopen `:qserver:4242

# 将运算6*8发送至server去进行计算，并收到运算结果
q)h "6*8"
48

# 在client端，定义一个函数sq
q)sq:{x*x}

# 将client端定义的函数sq，带上参数4，传到server端进行运算，并收到运算结果
# 注意：这样并不安全！
q)h (sq;4)
16

# 调用server端定义的函数cub3，并传入参数5，传到server端进行运算，并收到运算结果
# 注意：这是更推荐的一种做法（更安全）
q)h (`cub3; 5)
125
q)h (`cub3; 5)
125
```

## 14 Callbacks


## 15 I/O

### List of characters

雙引號`""`表示a list of characters。而``` ` ```表示string

```shell
q) count "jab"
3
q) count `jab
1
```

我們可以用括號`(string1, string2, ...)`來表示list of strings (而string本身又是list of characters，所以是一個nested list)

```shell
q)count ("So long"; "and thanks"; "for all the fish")
3
```

### File Handles

File Handler代表了一個路徑，我們用backtick+colon（``` `:[path]filename ```）去代表一個handler

#### hsym

`hsym`是一種創建file handler的方法。其語法結構是``hsym `$[path]filename``，先將一個代表路徑的string強制轉換成symbol，然後通過hsym命令將symbol轉換成合法的file symbol

```shell
q)hsym `$"/Users/joseph/Dropbox/code/learn/Q/table.csv"
`:/Users/joseph/Dropbox/code/learn/Q/table.csv
```

### save

保存一个名字叫table的表：

```shell
q)save `:/tmp/table.csv
`:/tmp/table.csv
```

### hcount

获得文件大小(in bytes):

```shell
q)hcount `:/tmp/table.csv
85995
```

### hdel

删除文件

```shell
# 删除一个存在的文件
q)hdel `:/tmp/table.csv
`:/tmp/table.csv

删除一个不存在的文件
q)hdel `:/tmp/table2.csv
'/tmp/table2.csv. OS reports: No such file or directory
  [0]  hdel `:/tmp/table2.csv
```

### serializing and deserializing q entities

任何q entity都可以被序列化持久保存。用`set`命令进行持久化，用`get`命令进行读取：

```shell
q)l: 1 2 3 4 5
q)l
1 2 3 4 5

# 保存
q)`:/tmp/lData set l
`:/tmp/lData

# 读取
q)l2:get `:/tmp/lData
q)l2
1 2 3 4 5
```

### hopen and hclose

``hopen``可以用于修改已经持久化的q entities。Syntax `hopen fh`其中`fh`是一个有效的file handler（可以是hsym或形如`` `: ``的路径），命令将会返回一个整型（int）file handler

```shell
# 打开已存在的持久化q entity
q)h:hopen `:/tmp/lData

# 返回额一个整型的file handler
q)h
1025i

# 在lData后面加上一个数字999
q)h[999]
1025i

# 在lData后面再加上两个数字 12 44
q)h 12 44
1025i

# 关闭（并自动保存修改）
q)hclose h

# 重新打开lData，看到新添加的数据已经在了
q)get `:/tmp/lData
1 2 3 4 5 999 12 44
```

### Writing and reading binary

任何数据，都可以以list of bytes的形式被q读取

在q里，`read0` 表示读取文本， `read1`则会读取一个文件as a list of bytes。用`fh 0: [list of strings]`去将数据写成binary保存下来；用`fh 1: [some bytes]`去将数据写成binary保存下来

```shell
# 读取文本
q)read0 `:/tmp/lData
"\376 \007\000\000\000\000\000\005\000\000\000\000\000\000\000\001\000\000\00..

# 写入文本（写入需要是list of strings，中间以分号隔开）
q)`:/tmp/txtData 0: ("hello\n"; "KDB")
`:/tmp/txtData

# 读取刚刚写入的文本text
q)read0 `:/tmp/txtData
"hello"
""
"KDB"

# 读取binary
q)read1 `:/tmp/lData
0xfe2007000000000005000000000000000100000000000000020000000000000003000000000..

# 写入binary
q)`:/tmp/binData 1: 0x06072a
`:/tmp/binData

# 读取刚刚写入的binary
q)read1 `:/tmp/binData
0x06072a
```

# --------------------

创建示例数据

```shell
q)N:3600
q)times:09:30:00.0000+1000*til N
q)idx:N?4
q)syms:`A`B`C`D idx
q)pxs:(1+N?0.1)*200 100 150 300 idx
q)table:([] time:times;sym:syms;price:pxs)
```

也可以将上述语句写进一个脚本 createdata.q:

```javascript
N:3600;
times:09:30:00.0000+1000*til N;
idx:N?4;
syms:`A`B`C`D idx;
pxs:(1+N?0.1)*200 100 150 300 idx;
table:([] time:times;sym:syms;price:pxs);
```

然后在q console里面执行该脚本：

```javascript
q)\l /tmp/createdata.q
```

1. 计算company A的30s移动窗口的平均价，每次遇到company A的Event都会触发Listener

```shell
lookback:1000*29;
ctable:a#table;
ctime:last ctable[`time];
window:select avg price,sym from ctable where (sym=`A) & (time within (ctime-lookback;ctime));
```