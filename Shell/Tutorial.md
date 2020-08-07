# ls

```shell
$ ls -F           # Show directory/ or file
$ ls -a           # Show all including hidden
$ ls -F -R        # Recursively, or ls -FR
$ ls -l           # Show more information
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

$ touch my_test  # create a file named my_test
$ ls -l my_test
-rw-r--r--  1 joseph  staff  0 Aug  7 14:32 my_test
$ touch my_test  # change modification time of my_test
$ ls -l my_test
-rw-r--r--  1 joseph  staff  0 Aug  7 14:36 my_test
