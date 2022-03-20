## 如何使用 ryu.app.rest_router

### 启动

```shell
ryu-manager ryu.app.rest_router
```

```shell
sudo mn --custom create_topo.py --topo mytopo --switch ovs --controller remote,ip=192.168.233.130 --link tc
```

### API 接口

`GET http://localhost:8080/router/0000000000000001 ` 是得到`01`号router的信息

```
POST http://localhost:8080/router/0000000000000001
{
} //JSON对象
```

是修改`01`号router的信息，由json对象指定修改内容。

+ `"address" : ""`指定`ip`
+ `"gateway":""`指定路由路径，**后面的参数填的是要送到的下一跳地址**
+ `"destination"`指定目的地址

## 如何运行

首先开启RYU和mininet，然后：

```shell
python make_route.py
```

之后在mininet中用

```shell
ip route add default via 
```

给各个终端添加默认路由

```shell
u1 ip route add default via 172.18.0.2
u2 ip route add default via 172.18.1.2
u3 ip route add default via 172.18.2.2
u4 ip route add default via 172.18.3.2
u5 ip route add default via 172.18.4.2

pingall
```

## test

tcp :
```shell
u1 iperf3 -c u3 -t 20 > u1-3.tcp &
```

udp :
```shell
u1 iperf3 -c u6 -u -b 40M > u1-e.udp &
```