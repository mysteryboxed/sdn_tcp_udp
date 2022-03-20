import requests

url = "http://localhost:8080/stats/flowentry/add"
schemes = {
  1 : [
    ([1], 2, "tcp"),
    ([1], 3, "udp")
  ],
  6 : [
    ([1, 4], 2, "tcp"),
    ([1, 4], 3, "udp")
  ],
  5 : [
    ([1], 4, "tcp"),
    ([1], 3, "udp")
  ]
}

def make_data(switch_id, in_ports, out_port, proto_type):
  for in_port in in_ports:
    yield {
      "dpid": switch_id,
      "cookie": 1,
      "cookie_mask": 1,
      "table_id": 0,
      "idle_timeout": 0,
      "hard_timeout": 0,
      "priority": 10000,
      "flags": 1,
      "match":{
          "in_port": in_port,
          "dl_type": int("800", 16),
          "nw_proto": 6 if proto_type == "tcp" else 17
      },
      "actions":[
          {
            "type":"OUTPUT",
            "port": out_port
          }
      ]
    }

for (num, datas) in schemes.items():
  for i in datas:
    in_ports, out_port, proto_type = i
    for data in make_data(num, in_ports, out_port, proto_type):
      requests.post(url=url, json=data)