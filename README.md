## TODO
- [x] make our custom topology work with controller `Ryu`
- [x] classic routing
- [x] classic routing performance testing
- [x] SDN routing with varied strategies
- [x] SDN routing performance testing
## Tutorial || Q&A
### create topology from mininet

A possible simple solution to solve ["loop switches"](https://github.com/mininet/mininet/wiki/FAQ#ethernet-loops) problem.
``` bash
$ sudo mn --custom ~/create_topo.py --topo mytopo --switch ovsbr,stp=1 --controller remote
```
And wait for STP to converge.
```bash
mininet> py net.waitConnected()
```
Then 'ping' is available.

### install Ryu
https://ernie55ernie.github.io/sdn/2019/03/25/install-mininet-and-ryu-controller.html
https://ryu.readthedocs.io/en/latest/getting_started.html

