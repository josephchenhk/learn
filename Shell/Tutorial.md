# ls

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

# touch

Use touch command to create a file or change its modification time:

```shell
$ touch my_test  # create a file named my_test
$ ls -l my_test
-rw-r--r--  1 joseph  staff  0 Aug  7 14:32 my_test
$ touch my_test  # change modification time of my_test
$ ls -l my_test
-rw-r--r--  1 joseph  staff  0 Aug  7 14:36 my_test
```

# cp

Basic usage is "cp source destination". But there are some additional parameters that should be useful.

```shell
$ cp my_test my_test2    # will override my_test2 without asking
$ cp -i my_test my_test2 # will ask before overwriting
overwrite my_test2? (y/n [n])y
$ cp -i /aaa/bbb/ccccc/ddddd . # copy a deep file to current directory
$ cp -R Scripts/ new_scripts   # recursively copy whole directory and sub folders
```

# ln

Create a soft/hard link to a certain file.

## soft link

```shell
$ ln -s my_test sl_my_test  # soft link
$ ls -i *my_test            # verify they are two different files
8678429 my_test    8681318 sl_my_test
$ ls -l *my_test            # they are with different sizes
-rw-r--r--  1 joseph  staff  *0* Aug  7 14:36 my_test
rwxr-xr-x  1 joseph  staff  *7* Aug  7 15:10 sl_my_test -> my_test
```

## hard link

```shell
$ ln my_test hl_my_test     # without -s, means hard link
$ ls -i *my_test            # they refer to the same inode number
8678429 hl_my_test 8678429 my_test
$ ls -l *my_test            # they are of same size
-rw-r--r--  2 joseph  staff  0 Aug  *7* 14:36 hl_my_test
-rw-r--r--  2 joseph  staff  0 Aug  *7* 14:36 my_test
```

# mv

Same as command `cp`, but do not keep original copy anymore.

# rm

A good habbit is always using `-i` in rm, which will prevent you from mistakenly remove something.

```shell
$ rm -i my_test   # remove after confirmation
remove my_test?   
$ rm -f *test     # force to remove (careful!)
```

# mkdir

```shell
$ mkdir new_dir
$ mkdir -p new_dir/sub_dir/sub_sub_dir # create folder structure with `-p` param 
```

# `rmdir` & `rm -ri`

```shell
$ rmdir new_dir  # works only when new_dir is empty
$ rm -ir new_dir # can recursively remove directories, and need confirmation
$ rm -rf new_dir # [dangerous] force to remove the whole directory (and sub dirs)
```





