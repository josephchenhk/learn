# Esper Tutorial

Esper is a language, a language compiler and a runtime environment (runs on JVM).

The esper language is the Event Processing Language (EPL)

## Esper支持的事件表现形式

Esper支持多种事件表现形势：包括遵循JavaBean方式的含有getter方法的Java POJO（普通Java对象），实现了Map接口的对象，对象数组，XML文档对象，以及Apache Avro（一个支持JSON和Schema的数据序列化系统，可以将数据结构或对象转化成便于存储和传输的格式）。这些事件表现形式的共同之处在于，它们都提供了事件类型的元数据，也就是说能够表示事件的一系列属性，例如，一个Java对象可以通过其成员变量来表示其事件属性，一个Map对象能够通过键值对来表示属性。由此可见，本质上事件是一系列属性值的集合，对事件的操作即对事件中的部分或全部属性的操作。

##vEsper事件处理模型
Esper事件处理模型主要包含两部分：

###（1）Statement 

利用Esper的事件处理语言EPL声明对事件进行的操作，Esper中提供了多种类型的事件操作，包括过滤、加窗、事件聚合等等。EPL是一种类似于SQL的语言，从这一点上来看，Esper恰好与数据库相反，数据库时保存数据，并在数据上运行查询语句，而Esper是保存查询语句，在这些查询上运行数据，只要事件与查询条件匹配，Esper就会实时进行处理，而不是只有在查询提交的时候才处理。

###（2）Listener

用于监听事件的处理情况，接收事件处理的结果，通过UpdateListener接口来实现，它相当于一个回调函数，当事件处理完成之后，可以通过该回调函数向结果发送到目的地。