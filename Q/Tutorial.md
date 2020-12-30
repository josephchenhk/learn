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