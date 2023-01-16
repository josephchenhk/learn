# quantkits

## 简单的Git Tutorial

配置用户名和邮箱

* config
```shell
git config --global user.name "joseph"
git config --global user.email "josephchenhk@gmail.com"
```
如果没有--global参数，则表示local设置；如果没有后面的"XXX"，则查看config。

* branch

查看远程分支

```shell
git branch -a
```

在本地更新远程分支的信息（To update the local list of remote branches）：

```shell
git remote update origin --prune
```

查看本地分支

```shell
git branch
```

删除本地分支

```shell
git branch -d <branchname>
git branch -D <branchname>
```
Note: 

1. The -d option is an alias for --delete, which only deletes the branch if it has already been fully merged in its upstream branch.

2. The -D option is an alias for --delete --force, which deletes the branch "irrespective of its merged status." [Source: man git-branch]

删除远程分支

```shell
$ git push -d <remote_name> <branchname>
```

Note: In most cases, <remote_name> will be origin.

* merge

假如你在dev分支开发，与此同时master分支也有了更新：

![alt text](../Contents/Git/git_diverge.png "Git diverge")

你可以选择将master分支合并到dev：
```shell
git checkout dev
git merge master
```

![alt text](../Contents/Git/git_merge.png "Git merge")

* log

你可以通过 `git log -n` 查找最近n条commit记录. 更简洁的命令是 `git log --oneline -n` ，n是最近几多次提交的记录。

回撤至旧记录，有两种方法：1. revert（会创建一个和旧commit一模一样的commit，从而达到后退的目的）；2. reset（会彻底消灭旧的commit，如果带--hard参数，就不单只缓存区，连工作区也会回退。这个操作不可撤销，要慎重！）

* revert
```shell
git revert HEAD -m 1
```
对于merge的revert，需要提供-m参数，1/2分别对应dev和master分支. revert后如下：
![alt text](../Contents/Git/git_revert.png "Git revert")

* reset

主要用于撤销git add（撤销提交至缓存区的提交）
```shell
git reset <commit-id>
```
![alt text](../Contents/Git/git_reset.png "Git reset")

假如提交记录如下：
```
$ git log --oneline -5 // 最近5次提交记录
ba2f0a4 (HEAD -> master, origin/master) test4 //最新提交的记录
f3a6683 test3 // 上一个提交的记录
4f0f054 test2
6fefa2d test1
77f9ec8 reset
```

则通过`git reset --hard HEAD`(或者`git reset --hard ba2f0a4`)回到最新的提交test4；通过`git reset --hard HEAD~`(或者`git reset --hard f3a6683`)回到上一个提交test3；通过`git reset --hard HEAD~2`(或者`git reset --hard 4f0f054`)回到最新的提交test2.

最后大杀招，通过interactive rebase的方式将当前dev分支rebase到master分支：

* rebase
```shell
git rebase -i master
```
![alt text](../Contents/Git/git_rebase.png "Git rebase")

* stash

查看现有的储藏，
```shell
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

应用储藏，

```shell
$ git stash apply              # 等价于 git stash apply stash@{0}
$ git stash apply stash@{2}    # 应用stash@{2}
```

以上命令只恢复工作区，如果想连暂存区也恢复，需要加上--index参数

```shell
$ git stash apply --index
```

移除stash，用drop：

```shell
$ git stash drop stash@{0}
```

* push

推到远程同名分支（如果远程不存在该分支则创建一个）：

```shell
$ git push origin HEAD
```

* submodule

添加submodule，如果不指定名称，就会默认同名

```shell
$ git submodule add https://github.com/josephchenhk/quantkits.git
```

用`git submodule init`去初始化本地配置，用`git submodule update`去fetch远端的数据并且checkout到相应的commit

```shell
$ git submodule init
$ git submodule update
```

如果有nested submodules，可以用recursive参数：

```shell
$ git submodule update --init --recursive
```

当远端有更新，则需要用remote参数去更新git submodule，

```shell
$ git submodule update --remote
```

默认是追踪master分支，如果需要追踪其他分支，则需要在.gitmodules里面指定

```shell
$ git config -f .gitmodules submodule.quantkits.branch dev
```

如果没有`-f .gitmodules`的话，则只会改变你本地的track branch；如果希望其他人也能更新track branch的话，则需要加上这个参数


* How to init git and push to remote ([Ref](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line))

如果已经有一个项目，则只需要在github上面新建一个空目录（注意不要初始化，不要添加README, gitignore等任何文件，就一个空目录）

然后运行

```shell
$ git init
```

初始化项目，然后执行

```shell
$ git add .
$ git commit -m "first commit"
```

之后设定刚才在github上面创建的目录为远程目录，并指定名字为origin

```shell
$ git remote add origin https://github.com/josephchenhk/trading.git
$ git remote -v # 确认目录是否设置正确
```

将项目推上github：

```shell
$ git push origin master
```

便可以在github上面看到整个项目。如果想要pull，则需要设置upstream

```shell
$ git branch --set-upstream-to=origin/master
```

之后便可以正常pull和push至master了。

### 取消已经push至Github的commit

Ref：https://stackoverflow.com/questions/448919/how-can-i-remove-a-commit-on-github

```
>> git status
>> git stash
>> git reset --soft HEAD^
>> git stash list
>> git stash apply
>> git add Python/smtp_example/auto_send_email.py
>> git add .gitignore
>> git commit -m "update cred"
>> git status
>> git push origin +master --force
```

### 用一个branch覆盖另外一个branch

这里用staging branch去覆盖master branch（顺便将原来master branch打一个标签）

```shell
$ git checkout email
$ git tag old-email-branch
$ git reset --hard staging
```

### 将在远程删除的分支在本地仓库也删除

用命令 `git remote show origin` 查看分支的情况，可以看到 `origin/dev` 分支已经呈 `stale`
状态，即已经在远程服务器被删除，但我们在本地仍然可以通过 `git branch -a`看到。
```shell
> git remote show origin                                                                           ✔  5.83G RAM  2.87 L
* remote origin
  Fetch URL: https://github.com/josephchenhk/xxx.git
  Push  URL: https://github.com/josephchenhk/xxx.git
  HEAD branch: main
  Remote branches:
    main                    tracked
    refs/remotes/origin/dev stale (use 'git remote prune' to remove)
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (up to date)
```

在这种情况下，根据提示，可以通过 `git remote prune [origin]` 进行清理，将远程和本地的分支情况进行同步，
这样再通过 `git branch -a` 来查看就会发现 `origin/dev` 分支已经不存在了。

```shell
> git remote prune origin
```


