# Basic bash shell commands

## ls

```shell
$ ls -F           # Show directory/ or file
$ ls -a           # Show all including hidden
$ ls -F -R        # Recursively, or ls -FR
$ ls -l           # Show more information
$ ls -d Scripts/  # Show only the information of the folder, but not its contents
$ ls -l my_script # match only the file my_script
$ ls -l my_scr?pt # match anything with pattern my_scr[1 char]pt
-rw-rw-r-- ... my_scrapt
-rw-rw-r-- ... my_script
$ ls -l my_scr*pt # match anything with pattern my_scr[0-many char]pt
-rw-rw-r-- ... my_scrapt
-rw-rw-r-- ... my_script
-rwxrwxrw- ... my_scroooopt
-rwxrwxr-- ... my_scrpt
$ ls my_scr[a-i]pt # any characters between a to i
my_scrapt  my_script 
$ ls my_scr[ai]pt # either a or i
my_scrapt  my_script 
$ ls my_scr[!a]pt # anything match pattern scr[1 char]pt but not a (Mac好像不支持？)
my_script
```

The first 'd' in 'drwxr-xr-x' means directory. If it is '-', it means an ordinary file.

## touch

Use touch command to create a file or change its modification time:

```shell
$ touch my_test  # create a file named my_test
$ ls -l my_test
-rw-r--r--  1 joseph  staff  0 Aug  7 14:32 my_test
$ touch my_test  # change modification time of my_test
$ ls -l my_test
-rw-r--r--  1 joseph  staff  0 Aug  7 14:36 my_test
```

## cp

Basic usage is "cp source destination". But there are some additional parameters that should be useful.

```shell
$ cp my_test my_test2    # will override my_test2 without asking
$ cp -i my_test my_test2 # will ask before overwriting
overwrite my_test2? (y/n [n])y
$ cp -i /aaa/bbb/ccccc/ddddd . # copy a deep file to current directory
$ cp -R Scripts/ new_scripts   # recursively copy whole directory and sub folders
```

## ln

Create a soft/hard link to a certain file.

### soft link

```shell
$ ln -s my_test sl_my_test  # soft link
$ ls -i *my_test            # verify they are two different files
8678429 my_test    8681318 sl_my_test
$ ls -l *my_test            # they are with different sizes
-rw-r--r--  1 joseph  staff  *0* Aug  7 14:36 my_test
rwxr-xr-x  1 joseph  staff  *7* Aug  7 15:10 sl_my_test -> my_test
```

### hard link

```shell
$ ln my_test hl_my_test     # without -s, means hard link
$ ls -i *my_test            # they refer to the same inode number
8678429 hl_my_test 8678429 my_test
$ ls -l *my_test            # they are of same size
-rw-r--r--  2 joseph  staff  0 Aug  *7* 14:36 hl_my_test
-rw-r--r--  2 joseph  staff  0 Aug  *7* 14:36 my_test
```

## mv

Same as command `cp`, but do not keep original copy anymore.

## rm

A good habbit is always using `-i` in rm, which will prevent you from mistakenly remove something.

```shell
$ rm -i my_test   # remove after confirmation
remove my_test?   
$ rm -f *test     # force to remove (careful!)
```

## mkdir

```shell
$ mkdir new_dir
$ mkdir -p new_dir/sub_dir/sub_sub_dir # create folder structure with `-p` param 
```

## `rmdir` & `rm -ri`

```shell
$ rmdir new_dir  # works only when new_dir is empty
$ rm -ir new_dir # can recursively remove directories, and need confirmation
$ rm -rf new_dir # [dangerous] force to remove the whole directory (and sub dirs)
```

## file

```shell
$ file my_test
my_test: empty
$ file New_Dir
New_Dir: directory
```

## cat

```shell
$ cat my_test
hello
world
$ cat -n my_test # line number for all lines
1 hello
2 world
$ cat -b my_test # line number for non-empty lines
```

## `more` and `less`
 
`cat` will show whole text immediately. `more` (and `less`) will show in pages. You can input `q` to exit.

```shell
$ more my_test
hello
world
my_test (END)
q # input q to exit

$ less my_test # more flexible than command `more`
hello
world
my_test (END)
q # input q to exit
```

## tail

```shell
$ tail log_file       # show last 10 (default) lines
$ tail -n 2 log_file  # show last 2 lines
$ tail -f log_file    # show in flush mode
```

## head

`head` is almost same as `tail` command, but there is no `-f` param for it, as we do not expect the headers of a file 
should change frequently.


# Advance bash shell commands

## ps

A snapshot of processes at the current moment.

```shell
$ ps -ef                     # `-e` show all processes; `-f` full output
$ ps -ef | egrep "disk|PID"  # show headers as well
```

## top

`ps` shows only static snapshot of processes; while `top` can dynamically show processes. After entering `top`, use the following command to sort:
1. Linux

* Sorted by CPU: P
* Sorted by Mem: M

2. Mac 

Input `o` first, then type the column names:

* Sorted by CPU: `o` + `CPU`
* Sorted by Mem: `o` + `MEM`

## kill

Process signals:

| Signals        | Name          | Description  |
| ------------- |:-------------:| -----:  |
|       1       |   HUP         | Hang up 挂起 |
|       2       |   INT         | Interupt 中断|
|       3       |   QUIT        | Quit 结束运行|
|       9       |   KILL        | Kill whatever 无条件终止|
|       11      |   SEGV        | Segment err 段错误|
|       15      |   TERM        | Kill if possible 尽可能终止|
|       17      |   STOP        | Stop but not kill 无条件停止运行，但不终止|
|       18      |   TSTP        | Stop but still in backoffice 停止或暂停，但继续在后台运行|
|       19      |   CONT        | Continue after STOP/TSTP 在STOP或TSTP之后恢复执行|

```shell
$ kill 3940 (PID)
$ kill -9 3940 # same as `kill -s KILL 3940`
```

## killall

This command is more powerful and more dangerous. It supports killing process by its name instead of its PID:

```commandline
$ killall http*
```

**Be careful** since this operation might accidentally kill system process and make your system crashed.

## mount

```shell
$ mount # show devices
/dev/disk1s1 on / (apfs, local, read-only, journaled)
devfs on /dev (devfs, local, nobrowse)
/dev/disk1s2 on /System/Volumes/Data (apfs, local, journaled, nobrowse)
/dev/disk1s5 on /private/var/vm (apfs, local, journaled, nobrowse) 

$ mount -t vfat /dev/sdb1 /media/disk # usage: `mount -t type device directory`
```

## umount

```shell
$ umount /home/rich/mnt # if any app is using the mounted directory, you can't un-mount
```

## df

show disk-free.

```shell
$ df
Filesystem    512-blocks      Used Available Capacity iused      ifree %iused  Mounted on
/dev/disk1s1   976490576  21706480 596657360     4%  487653 4881965227    0%   /
devfs                670       670         0   100%    1160          0  100%   /dev
/dev/disk1s2   976490576 350326928 596657360    37% 1655757 4880797123    0%   /System/Volumes/Data

$ df -h # human readable
Filesystem      Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk1s1   466Gi   10Gi  285Gi     4%  487653 4881965227    0%   /
devfs          335Ki  335Ki    0Bi   100%    1160          0  100%   /dev
/dev/disk1s2   466Gi  167Gi  285Gi    37% 1655827 4880797053    0%   /System/Volumes/Data
```

## du

We can find big directories/files using du and (e)grep:

```shell
$ du -h | grep "^ *[0-9][0-9.]*G" # locate big files larger than 1GB
$ du -ah | egrep "^ *([0-9][0-9][0-9][0-9.]*M)|([0-9][0-9.]*G)" # locate big directories/files larger than 100MB
```

## sort

```shell
$ cat my_test                             ✔  5.99G RAM  1.73 L
1
2
100
3
4

$ sort my_test # sort as characters
1
100
2
3
4

$ sort -n my_test # sort as numbers                       ✔  5.75G RAM  1.67 L
1
2
3
4
100
```

## `grep` & `egrep`

Please refer to [Linux grep基本用法与正则表达式](https://blog.csdn.net/xy010902100449/article/details/51426354).
### Usages

`grep [-acinv] [--color=auto] [-A n] [-B n] '搜寻字符串' 文件名`

参数说明：

- -a：将二进制文档以文本方式处理
- -c：显示匹配次数
- -i：忽略大小写差异
- -n：在行首显示行号
- -A：After的意思，显示匹配字符串后n行的数据
- -B：before的意思，显示匹配字符串前n行的数据
- -v：显示没有匹配行-A：After的意思，显示匹配部分之后n行-B：before的意思，显示匹配部分之前n行
- --color：以特定颜色高亮显示匹配关键字

### Regular expressions

|元数据	| 意义和范例 |
|:-----:|:--------:|
|^word	|搜寻以word开头的行。 例如：搜寻以#开头的脚本注释行 grep –n ‘^#’ regular.txt|
|word$	|搜寻以word结束的行 |
|.	    |匹配任意一个字符。 例如：grep –n ‘e.e’ regular.txt 匹配e和e之间有任意一个字符，可以匹配eee，eae，eve，但是不匹配ee。|
|\	    |转义字符。 例如：搜寻’，’是一个特殊字符，在正则表达式中有特殊含义。必须要先转义。grep –n ‘\,” regular.txt|
|*	    |前面的字符重复0到多次。 例如匹配gle，gogle，google，gooogle等等 grep –n ‘go*gle’ regular.txt|
|[list]	|匹配一系列字符中的一个。 例如：匹配gl，gf。grep –n ‘g[lf]’ regular.txt|
|[n1-n2]|匹配一个字符范围中的一个字符。 例如：匹配数字字符 grep –n ‘[0-9]’ regular.txt|
|[^list]|匹配字符集以外的字符 例如：grep –n ‘[^o]‘ regular.txt 匹配非o字符|
|\<word	|单词是的开头。 例如：匹配以g开头的单词 grep –n ‘\<g’ regular.txt|
|word\>	|前面的字符重复n1，n2次 例如：匹配google，gooogle。grep –n ‘go\{2,3\}gle’ regular.txt|
|\<word	|匹配单词结尾 例如：匹配以tion结尾的单词 grep –n ‘tion\>’ regular.txt|
|word\{n1\}	    |前面的字符重复n1 例如：匹配google。 grep –n ‘go\{2\}gle’ regular.txt|
|word\{n1,\}	|前面的字符至少重复n1 例如：匹配google，gooogle。 grep –n ‘go\{2\}gle’ regular.txt|
|word\{n1,n2\}	|前面的字符重复n1，n2次 例如：匹配google，gooogle。 grep –n ‘go\{2,3\}gle’ regular.txt|


## gzip

Compressor for `.gz` files.

```shell
$ gzip my_prog  # compress my_prog to my_prog.gz
$ gzip my*      # compress all files match pattern my*
```

## tar

Common parameters used in `tar`:

|Param | Name | Description|
|:----:|:----:|:----------:|
|-c    |--create| compress file|
|-x    |--extract| extract file|
|-v    |--verbose| verbose     |
|-z    | (zip)   | extract .tgz file|

Example:

```shell
$ tar -zxvf filename.tgz
```


# 认识Shell

## shell的版本

```shell
# 默认交互的shell是/bin/bash
$ cat /etc/passwd   
[...]
christine:x:1000:1000:Christine,,,:/home/christine:/bin/bash

# 默认系统shell是/bin/sh
$ ls -l /bin/sh 12 lrwxrwxrwx 1 root root 4 Apr 22 12:33 /bin/sh -> dash

# 启动非默认shell
$ /bin/dash
# 推出当前shell
$ exit
```
