from subprocess import Popen, PIPE
import time
import sys

cmd = [
  "u1 ip route add default via 172.18.0.2",
	"u2 ip route add default via 172.18.1.2",
	"u3 ip route add default via 172.18.2.2",
	"u4 ip route add default via 172.18.3.2",
	"u5 ip route add default via 172.18.4.2",
	"u6 ip route add default via 172.18.2.2",
	"u7 ip route add default via 172.18.2.2",
  "u8 ip route add default via 172.18.2.2"
]

test_cmd = [
  "u3 iperf3 -s -D",
	"u6 iperf3 -s -D",
	"u7 iperf3 -s -D",
	"u8 iperf3 -s -D",
	"u1 iperf3 -c u3 -t 20 > u1.tcp &",
	"u1 iperf3 -c u6 -u -b 40M > u1.udp &",
	"u5 iperf3 -c u8 -u -b 40M > u5.udp &",
  "u5 iperf3 -c u7 -t 20 > u5.tcp &"
]

proc = "sudo mn --custom create_topo.py --topo mytopo \
--switch ovs --controller remote,ip=192.168.1.223 --link tc"

def write_and_flush(proc, st):
  proc.stdin.write(bytearray(st + "\n", "utf-8"))
  proc.stdin.flush()

arg = proc.split()
p = Popen(arg, stdin=PIPE)

try:
  input("")
  for i in cmd:
    write_and_flush(p, i)
  write_and_flush(p, "pingall")
  for i in test_cmd:
    write_and_flush(p, i)
  time.sleep(24)
finally:
  p.kill()
