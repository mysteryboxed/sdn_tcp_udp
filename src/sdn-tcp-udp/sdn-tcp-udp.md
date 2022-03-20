首先打开RYU控制器：

```shell
ryu run --observe-links ryu.app.rest_router ryu.app.gui_topology.gui_topology ryu.app.ofctl_rest
```

按照与经典路由相同的方式配置好拓扑与经典路由。

然后运行

```shell
python make_sdn_route.py
```

这会创建将TCP和UDP分流的路由