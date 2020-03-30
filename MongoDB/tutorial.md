# MongoDB

参考：

1. https://www.runoob.com/mongodb/mongodb-tutorial.html
2. https://www.runoob.com/docker/docker-install-mongodb.html

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
```

数据库不要特别创建，直接写入就可以（如没有该数据库，便会自动创建）





