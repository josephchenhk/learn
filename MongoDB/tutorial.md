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




