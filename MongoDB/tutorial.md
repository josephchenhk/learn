# MongoDB

参考：

1. https://www.runoob.com/mongodb/mongodb-tutorial.html
2. https://www.runoob.com/docker/docker-install-mongodb.html
3. https://blog.csdn.net/u010649766/article/details/78497928

## Docker 安装 MongoDB


```angularjs
# 拉取官方的最新版本的镜像
$ docker pull mongo:latest

# 安装完成后，我们可以使用以下命令来运行mongo容器
$ docker run -itd --name mongo -p 27017:27017 mongo --auth

# 运行mongo容器
$ docker exec -it mongo mongo admin

# 创建一个名为 admin，密码为 123456 的用户
>  db.createUser({ user:'admin',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'}]});

# 尝试使用上面创建的用户信息进行连接。
> db.auth('admin', '123456')
```

## MongoDB 概念解释
	
|   SQL术语/概念 |   MongoDB术语/概念   |  解释/说明                        |
|:------------:|:-------------------:|:-------------------------------:|
| database     |  database           | 数据库                           |
| table        |  collection         | 数据库表/集合                     |
| row	       |  document           | 数据记录行/文档                    |
| column	   |  field              | 数据字段/域                       |
| index	       |  index              | 索引                             |
| table joins  |      /              | 表连接,MongoDB不支持               |
| primary key  |  primary key        | 主键,MongoDB自动将_id字段设置为主键  |

## MongoDB 连接数据库

```angularjs
# 查看数据库
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> 

# 查看所有用户（及其权限）
> use admin
switched to db admin
> show users
```

数据库不需要特别创建，直接写入就可以（如没有该数据库，便会自动创建）


```angularjs
# 赋予用户admin对runoob数据库的读写权限
> db.grantRolesToUser("admin",[{role:"readWrite",db:"runoob"}])

# 查看全局所有账户的权限
> use admin
> db.auth('admin','123456')
> db.system.users.find().pretty()

# 切换到runoob数据库
> use runoob

# 写入数据
> db.runoob.insert({"name":"菜鸟教程"})
WriteResult({ "nInserted" : 1 })
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
runoob  0.000GB
```

## MongoDB 创建/删除数据库、集合、文档

### 删除数据库
```
> use admin
switched to db admin
> 
> db.grantRolesToUser("admin",[{role:"dbAdmin",db:"runoob"}])
> use runoob
switched to db runoob
> db.dropDatabase()
{ "dropped" : "runoob", "ok" : 1 }
```

### 创建数据库和集合
```
> use runoob
switched to db runoob
> db.createCollection("runoob_table") 
{ "ok" : 1 }
> show tables
runoob_table
```

### 创建文档
```
> db.runoob_table.insert({title: 'MongoDB 教程', 
     description: 'MongoDB 是一个 Nosql 数据库',
     by: '菜鸟教程',
     url: 'http://www.runoob.com',
     tags: ['mongodb', 'database', 'NoSQL'],
     likes: 100
})

# db.collection.insertOne():向指定集合中插入一条文档数据
# db.collection.insertMany():向指定集合中插入多条文档数据
```

### 查看文档
```
> db.runoob_table.find()
```

### 更新文档方法1：update


update() 方法用于更新已存在的文档。语法格式如下：
```
db.collection.update(
   &lt;query>,
   &lt;update>,
   {
     upsert: &lt;boolean>,
     multi: &lt;boolean>,
     writeConcern: &lt;document>
   }
)
```
参数说明：

**query** : update的查询条件，类似sql update查询内where后面的。

**update** : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的。

*upsert* : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。

*multi* : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。

*writeConcern* :可选，抛出异常的级别。

```
> db.runoob_table.update(
   {title: 'MongoDB 教程'},
   {$set:{title: 'MongoDB 教程标题修改一次了'}}
)
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> 
> db.runoob_table.find()
{ "_id" : ObjectId("5e829a6adeaa3694d37f9e2e"), "title" : "MongoDB 教程标题修改一次了", "description" : "MongoDB 是一个 Nosql 数据库", "by" : "菜鸟教程", "url" : "http://www.runoob.com", "tags" : [ "mongodb", "database", "NoSQL" ], "likes" : 100 }
> 
```

### 更新文档方法2：save
save() 方法通过传入的文档来替换已有文档。语法格式如下：
```
> db.collection.save(
     &lt;document>,
     {
       writeConcern: &lt;document>
     }
  )
```
参数说明：

**document** : 文档数据。

*writeConcern* :可选，抛出异常的级别。
```
> db.runoob_table.save({
      "_id" : ObjectId("5e829a6adeaa3694d37f9e2e"),
      "title" : "MongoDB 教程标题修改第二次了"
      }
  )
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
> 
> db.runoob_table.find()
{ "_id" : ObjectId("5e829a6adeaa3694d37f9e2e"), "title" : "MongoDB 教程标题修改第二次了" }

```

### 删除文档

如果你的 MongoDB 是 2.6 版本以后的，语法格式如下：

```
db.collection.remove(
   &lt;query>,
   {
     justOne: &lt;boolean>,
     writeConcern: &lt;document>
   }
)
```

参数说明：

*query* :（可选）删除的文档的条件。

*justOne* : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。

*writeConcern* :（可选）抛出异常的级别。

```
> db.runoob_table.find()
{ "_id" : ObjectId("5e829a6adeaa3694d37f9e2e"), "title" : "MongoDB 教程标题修改第二次了" }
> db.runoob_table.remove({"title" : "MongoDB 教程标题修改第二次了"})
WriteResult({ "nRemoved" : 1 })
> db.runoob_table.find()
> 
```







