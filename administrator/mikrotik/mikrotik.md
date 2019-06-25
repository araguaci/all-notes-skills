# PPPoE
###### IGMP Proxy
Address on interface

# IPv6

###### IPv6 MTU over PPPoE Interface
```
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn in-interface=6to4 tcp-mss=1221-65535 log-prefix=""
chain=forward action=change-mss new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn out-interface=6to4 tcp-mss=1221-65535 log-prefix=""
```

# NAT
###### Local network access to an external IP address
```
/ip firewall nat
```
```
add action=dst-nat chain=dstnat dst-address=remote_host dst-port=80,443 in-interface-list=LAN protocol=tcp src-address=10.0.192.0/20 to-addresses=local_host
add action=masquerade chain=srcnat dst-address=local_host dst-port=80,443 out-interface-list=LAN protocol=tcp src-address=10.0.192.0/20
```