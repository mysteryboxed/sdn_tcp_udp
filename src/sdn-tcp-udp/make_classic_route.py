import requests
import dijkstra

node_list = [ 0, 1, 2, 3, 4, 5 ]
network_list = [ 0, 1, 2, 3, 4 ]
distance_list =\
  [ 
    [ 0, 1, 3 ],
    [ 0, 5, 2 ],
    [ 0, 4, 3 ],
    [ 1, 2, 2 ],
    [ 1, 3, 3 ],
    [ 1, 5, 2 ],
    [ 2, 3, 2 ],
    [ 3, 4, 3 ],
    [ 3, 5, 2 ],
    [ 4, 5, 2 ]
  ]

router_url = "http://127.0.0.1:8080/router/"

def exist_link(num1, num2):
  for i in distance_list:
    if (num1 == i[0] and num2 == i[1]) or\
       (num1 == i[1] and num2 == i[0]):
      return True
  return False

def get_router_address(num1, num2, prefix=False):
  a = max(num1, num2)
  b = min(num1, num2)
  if prefix:
    return "192.168.{}.{}/24".format(b * 10 + a, num1 + 1)
  else:
    return "192.168.{}.{}".format(b * 10 + a, num1 + 1)

def get_router_host_address(num):
  return "172.18.{}.0/24".format(num)

def get_router_address_for_host(num):
  return "172.18.{}.2/24".format(num)

def make_router_url(num):
  return router_url + format(num + 1, "016d")

def router_add_address(num):
  for i in node_list:
    data = { "address": get_router_address_for_host(num) }
    requests.post(url=make_router_url(num), json=data)
    if exist_link(num, i):
      data = { "address": get_router_address(num, i, prefix=True) }
      requests.post(url=make_router_url(num), json=data)

def router_add_route(src, by, dst):
  data = { "gateway": get_router_address(by, src), 
           "destination": get_router_host_address(dst) }
  requests.post(url=make_router_url(src), json=data)

graph = dijkstra.Graph()

for i in node_list:
  router_add_address(i)

for i in distance_list:
  graph.add_edge(i[0], i[1], i[2])
  graph.add_edge(i[1], i[0], i[2])
  
for i in node_list:
  dij = dijkstra.DijkstraSPF(graph, i)
  for j in network_list:
    path = dij.get_path(j)
    if len(path) >= 2:
      router_add_route(i, path[1], j)
