# Q Language

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

Generally speaking, ``|``符號表示iterate across整個List

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