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

## 父子进程

```shell
$ ps -f # 通过PPID显示父进程
UID PID PPID
...

$ ps --forest # 展示树状关系（父子进程关系）
...
```


在Mac系统，需要安装`brew install pstree`，然后通过`pstree`命令去展示树状关系。

## 进程列表

依次运行一系列命令：

```shell
$ pwd; ls; cd /etc; pwd; ls
```

进程列表需要在上面的命令加上一对括号：

```shell
$ (pwd; ls; cd /etc; pwd; ls)
```

进程列表是一种命令分组（command grouping），会创建一个子shell来执行命令。另外一种命令分组方式为花括号`{ command;}`（命令结尾处要加上分号`;`）
使用花括号进行命令分组则不会创建子shell。

## 后台模式

在命令后面加上符号`&`:

```shell
$ sleep 10 &
[1] 2396

$ ps -f
UID      PID  PPID  C STIME TTY TIME CMD
Jospeh  2396  ...
```

## 协程

用`coproc`启动协程（创建一个子shell，并且将命令置入后台模式）

```shell
$ coproc sleep 10                           ✔  5.33G RAM  2.93 L
[1] 17522

$ jobs -l                               ✔  5.32G RAM  2.92 L  ⚙
[1]  + 17522 running    sleep 10

$ coproc My_Job { sleep 10; }  # 给协程一个名字（注意花括号前后要空格）
[1] 17534
```


## 内建命令

首先，外部命令是存在于bash shell之外的程序，并不是shell的一部分。例如，ps就是一个外部命令，你可以通过which和type命令找到它：

```shell
$ which ps
/bin/ps

$ type -a ps
ps is /bin/ps
```

当外部命令执行时，会创建一个子进程，这种操作被称为**衍生**（forking）.

相对地，内建命令不需要使用子进程来执行，内建命令与shell编译成了一体，作为shell工具的组成部分存在，不需要借助外部程序文件来运行。`cd`和`exit`都是内建
于shell的命令：

```shell
$ type cd
cd is a shell builtin

$ type -a echo   # echo既有内建命令，也有外部命令                            ✔  5.44G RAM  2.73 L
echo is a shell builtin
echo is /bin/echo
```

## history

history命令的默认记录数，可以通过 $HISTSIZE 查看：

```shell
$ echo $HISTSIZE
50000

# 输入`!!`可以唤回上一条执行的命令
$ !!
$ echo $HISTSIZE

# 通过`history -a`命令，强制将命令历史记录写入 .bash_history文件（而不是等待退出shell之后再写入)
$ history -a
$ history

# 通过`!`后面跟历史序号，可以唤起历史列表上任意一条命令：
history | grep "HISTSIZE"
 1168  echo $HISTSIZE
$ !1168
$ echo $HISTSIZE
```

## alias

```shell
# 显示已有的别名命令
$ alias -p # 在mac上不需要加 -p                                  
-='cd -'
...=../..
....=../../..
...

# 设置别名 (仅在本shell进程生效)
$ alias li='ls -li'
```

# Linux环境变量

## 全局环境变量

```shell
$ env # 通过env或者printenv查看全局环境变量
ZSH=/Users/joseph/.oh-my-zsh
...

$ printenv HOME # 显示个别环境变量，用printenv，不要用env
/Users/joseph
$ echo $HOME # 等价于print HOME
/Users/joseph
```

## 局部环境变量

Linux系统并没有一个只显示局部环境变量的命令。`set`命令会显示为某个特定进程设置的所有环境变量，包括局部变量、全局变量以及用户定义变量

```shell
$ set
[...] # 既包括env命令所显示的全局变量，也包括用户自定义的局部变量

# 可以创建一个局部用户定义变量（注意=前后没有空格）
$ my_variable=Hello
$ echo $my_variable
Hello

# 创建全局环境变量的方法，是先创建一个局部环境变量，然后再把它导出（export）到全局环境中
$ my_variable="I am Global now"
$ export my_variable
$ exit
$ echo $my_variable
I am Global now
```

特别需要注意，子shell里面修改的全局变量，并不能影响父shell：

```shell
$ my_variable=Hello      # 父shell里面定义变量
$ export my_variable     # 使之变成全局变量
$ zsh                    # 进入子shell
$ echo $my_variable      # 显示全局变量（这时子shell和父shell的全局变量是一致的）
Hello
$ exit                   # 退出档期啊子shell
$ echo $my_variable      # 在父shell里全局变量依然是Hello
Hello
$ zsh                    # 进入另一个子shell
$ my_variable="No Hello" # 将my_variable的值修改为"No Hello"
$ echo $my_variable      # 查看一下my_variable的值，确实已经被修改为"No Hello"
No Hello
$ export my_variable     # 使这个修改变成全局变量（注意：仅在子shell有效）
$ exit                   # 退出子shell
$ echo $my_variable      # 在父shell里面全局变量依然是Hello
Hello
```

删除环境变量用`unset`:

```shell
$ echo $my_variable
Hello
$ unset my_variable
$ echo $my_variable

$
```

一条简单规则：如果用到变量，使用$；如果操作变量，不使用$。

## PATH环境变量

PATH中的目录使用冒号分隔

```shell
$ echo  $PATH
/Users/joseph/miniconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/VMware Fusion.app/Contents/Public

# 如果希望临时添加新目录，以便在bash里直接唤起程序，可以如下修改PATH
$ PATH=$PATH:/Users/joseph/my_program

# 这样便可以直接唤起在`Users/joseph/my_program`目录里的程序myprog
$ myprog

# 如果想对子shell也生效，记得导出PATH环境变量
$ export PATH
```


注意：以上对PATH的修改只能持续到退出或重启系统，在下一节会学到如何永久保持环境变量的修改效果

## 定位系统环境变量

启动bash shell有3种方式：

* 登录时作为默认登录shell
* 作为非登录shell的交互式shell
* 作为脚本运行的非交互式shell

### 登录shell

登录shell会从5个不同的启动文件里读取命令：

- /etc/profile
- $HOME/.bash_profile
- $HOME/.bash_login
- $HOME/.profile
- $HOME/.bashrc

### 交互式shell

交互式shell不会访问/etc/profile文件。交互式shell读取$HOME/.bashrc文件去获得环境变量。

### 非交互式shell

非交互式shell通常情况下是读取BASH_ENV去获得环境变量。

### 环境变量持久化

在大多数发行版中，存储个人用户永久性bash shell变量的地方是$HOME/.bashrc文件，这一点适用于所有类型的shell进程。
但如果设置了BASH_ENV变量，除非它指向的是$HOME/.bashrc，否则你应该将非交互式shell的用户变量放在别的地方。


## 数组变量

要给某个环境变量设置多个值，可以把值放在括号里，值与值之间用空格分隔

```shell
$ mytest=(one two three four five)
$ echo ${mytest[*]}
one two three four five
$ echo ${mytest[2]}  # In Mac, count from 1; in Linux, count from 0
two
$ unset mytest
```

# Linux文件权限

## /etc/passwd文件

/etc/passwd文件 的字段包含了如下信息:
*  登录用户名
*  用户密码
*  用户账户的UID(数字形式)
*  用户账户的组ID(GID)(数字形式)
*  用户账户的文本描述(称为备注字段)
*  用户HOME目录的位置
*  用户的默认shell

```shell
$ cat /etc/passwd
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
[...]
```
## /etc/shadow文件

只有root用户才能访问/etc/shadow文件，它保存了每个用户关于密码的详细记录，包括加密后的密码、多少天后需要修改密码等等。

## 管理Linux用户

(1) 创建用户命令两条：

```shell
$ adduser # 会主动调用/etc/adduser.conf，默认创建/home/用户名
$ useradd # 需要自己配置参数
```

为用户指定参数的useradd命令：

常用命令行选项：

* -d：指定用户的主目录
* -m：如果存在不再创建，但是此目录并不属于新创建用户；如果主目录不存在，则强制创建； -m和-d一块使用。
* -s：指定用户登录时的shell版本
* -M：不创建主目录

例子：

```shell
$ sudo  useradd  -d  "/home/tt"   -m   -s "/bin/bash"   tt
```

(2) 修改用户密码

修改用户tt的密码：

```shell
$ sudo passwd tt
$ sudo passwd -e tt # 强制下次登入时修改密码
```

(3) 用户删除命令：

```shell
$ sudo userdel 用户名
$ sudo userdel -r 用户名 # 连同用户主目录一块删除
```

## 管理Linux群组

在 /etc/group 文件里存储了用户组的信息

```shell
$ cat /etc/group
root:x:0:root
...

$ groupadd shared # 添加一个新的组shared
$ usermod -G shared testuser # 添加一个用户testuser进shared用户组
$ groupmod -n sharing shared # 把组名shared改为sharing
$
```

## 理解文件权限

```shell
$ ls -l
-rw-rw-r-- 1 rich rich ...
drw-rw-r-x 2 rich rich ...
```

输出结果第一个字段代表对象的类型：

- -代表文件
- d代表目录
- l代表链接
- c代表字符型设备
- b代表块设备
- n代表网络设备

后面3组三字符的编码，分别代表读（r），写（w）和执行（x）。每3个字符段分别对应：

- 文件属主（u，user）
- 文件属组（g，group）
- 其他（o，others）

所有人（a，all）代表以上全部三类

## 默认文件权限

Linux的文件权限码如下：

|权限   | 二进制值| 八进制值 |        描述     |
|:----:|:------:|:------:|:--------------:|
|---   | 000    |   0    | 没有任何权限     |
|--x   | 001    |   1    | 只有执行权限     |
|-w-   | 010    |   2    | 只有写权限       |
|-wx   | 011    |   3    | 只有写和执行权限  |
|r--   | 100    |   4    | 只有读权限       |
|r-x   | 101    |   5    | 只有读和执行权限  |
|rw-   | 110    |   6    | 只有读和写权限    |
|rwx   | 111    |   7    | 有所有权限       |

`umask`是个掩码，屏蔽掉不想授权安全级别的权限：

```shell
$ umask
022            # 默认的掩码

$ umask 026    # 修改默认的掩码至026

$ touch newfile & ls -l newfile
-rw-r----- ... # 文件默认权限666，减掉026等于640

$ mkdir newdir & ls -l
drwxr-x--x     # 目录默认权限777，减掉026等于751
```

## 改变安全性设置

`chmod`命令用来改变文件和目录的安全性设置

```shell
$ chmod o+r newfile
$ chmod 641 newfile
```

## 改变所属关系

chown命令用来改变文件的属主， chgrp命令用来改变文件的默认属组。

```shell
$ chown dan newfile        # 指定文件新属主
$ chown dan.shared newfile # 指定属主和属组
$ chown .shared newfile    # 只指定属组

$ chgrp shared newfile     # 改变文件或目录的属组
```

# 管理文件系统

找出物理分区。旧式IDE驱动器，Linux使用的是/dev/hdx，其中x表示一个字母，具体
是什么要根据驱动器的检测顺序（第一个驱动器是a，第二个驱动器是b，依次类推）。对于
新式的SATA驱动器和SCSI驱动器，Linux使用的是/dev/sdx。

## 操作文件系统

进入fdisk工具操作界面

```shell
$ sudo fdisk /dev/sda
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p # 将存储设备的详细信息显示出来
Disk /dev/sda: 42.9 GB, 42949672960 bytes, 83886080 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000bcbfe

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    83886079    40893440   8e  Linux LVM

Command (m for help): n # 创建新的分区
Command action
e extended
p primary partition (1-4)
p # 创建一个主分区
Partition number (1-4): 1 # 给这个主分区的编号为1
First cylinder (1-652, default 1): 1
Last cylinder, +cylinders or +size{K,M,G} (1-652, default 652): +2G

Command (m for help): w # 保存新的分区
```

# 安装软件程序

## 包管理基础

Linux中广泛使用的两种主要的基础工具是dpkg和rpm，分别是Debian发行版（如Ubuntu和Mint）和Red Hat发行版（Fedora，openSUSE和CentOS）的包管理工具。

```shell
$ yum list installed                    # 列出所有安装的包
$ yum list xterm                        # 查看xterm是否已经安装
$ yum provides file_name                # 查看系统上某个文件属于哪个包
$ yum install package_name              # 安装包package_name
$ yum localinstall package_name.rpm     # 本地通过rpm安装包package_name
$ yum list updates                      # 显示所有有更新的包
$ yum update package_name               # 更新包package_name
$ yum update                            # 一次过更新所有的包
$ yum remove package_name               # 删除包
$ yum erase package_name                # 删除包及清除关联文件
$ yum clean all                         # 清除broken dependency
$ yum deplist package_name              # 列出包package_name的所有依赖关系
$ yum update --skip-broken              # 忽略掉broken的包，继续更新其他所有包
$ yum repolist                          # 查看正从哪些仓库获取软件。yum的仓库定义文件位于 /etc/yum.repos.d
```

## 从源码安装

以安装sysstat为例：

```shell
$ tar -zxvf sysstat-11.1.1.tar.gz  # tar解压文件至同名文件夹
$ cd sysstat-11.1.1                # 进入sysstat-11.1.1文件夹
$ ls                               # 显示当前文件夹的所有文件和文件夹
README
configure
INSTALL
...
$ ./configure                      # 检查依赖
$ make                             # 编译成可执行文件
$ make install                     # 将运行文件安装到系统的常用位置上
```

# Shell脚本编程基础

## 构建基础脚本

### 使用多个命令

用分号隔开：

```shell
$ date;who
Mon Oct 19 19:03:56 HKT 2020
joseph   console  Oct 19 09:17
joseph   ttys004  Oct 19 09:17
joseph   ttys005  Oct 19 09:17
```

### 创建shell脚本文件

创建一个如下文件 test

```markdown
#!/bin/bash
# This script displays the date and who's logged on
date
who
```

第一行`#!/bin/bash`是必须的，指定要使用的shell. shell通过寻找$PATH里的路径去寻找可执行脚本，

```shell
echo $PATH
/Users/joseph/miniconda3/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

要让shell找到test脚本，只需要采取以下两种方法之一：

* 将shell脚本文件test所在的目录添加到
PATH环境变量中

* 在提示符中用绝对或者相对文件路径来引用shell脚本文件

```shell
$ chmod u+x test  # 添加执行权限
$ ./test          # 告诉shell将当前目录作为引用路径
```

### shell脚本

以下是一些常用的shell用法：


#!/bin/bash
echo start a script
var1=10
var2=testing
echo "var1=$var1, var2=$var2, var3=\$var2"
date > test.txt
who >> test.txt

# 调整swap
1. check available swap
   ```
   free -h
   ```
2. create a swap file
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   ```
3. enable the swap file
   ```
   sudo swapon /swapfile
   ```
4. make the swap file permanent
   to make the swap file persistent across reboots, add an entry for it in the `/etc/fstab` file. Open the file using a text editor:
   ```
   sudo vi /etc/fstab
   ```
   Add the following line at the end of the file:
   ```
   /swapfile none swap sw 0 0
   ```
5. adjust swap settings (optional)
    By default, Linux swaps data to and from the swap space frequently. However, you can adjust the swappiness value to control the frequency of swapping. The swappiness value ranges from 0 to 100. A lower value reduces swapping, while a higher value increases it. To check the current swappiness value:
   ```
   cat /proc/sys/vm/swappiness
   ```
   To temporarily change the swappiness value:
   ```shell
   sudo sysctl vm.swappiness=10
   ```
   To make the change permanent, edit the `/etc/sysctl.conf` file and add or modify the following line:
   ```
   vm.swappiness=10
   ```
6. verify the changes:
   ```
   free -h
   ```
7. **change the size of an existing swap**
   
   * 1. disable the swap
   ```
   sudo swapoff /swapfile
   ```
   * 2. resize the swap file
   ```
   sudo fallocate -l 4G /swapfile
   ```

   If the above doesn't work, alternatively, you can **use the `dd` command** to resize the swap file:
   ```shell
   sudo dd if=/dev/zero of=/swapfile bs=1G count=4
   ```

   * 3. update the swap file
   ```
   sudo mkswap /swapfile
   ```

   * 4. enable the swap
   ```
   sudo swapon /swapfile
   ```

   * 5. verify the changes
   ```
   free -h
   ```
