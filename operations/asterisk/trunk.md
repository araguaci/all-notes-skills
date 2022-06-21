# Trunk
## IAX2 trunk
### Frieend
```
[SERVER2]
username=SERVER1
secret=
host=
type=friend
qualify=yes
trunk=yes
context=from-trunk
disallow=all
allow=alaw&ulaw
```

```
[SERVER1]
username=SERVER2
secret=
host=
type=friend
qualify=yes
trunk=yes
context=from-trunk
disallow=all
allow=alaw&ulaw
```

### Input, output
Outgoing server 1
```
[offise1]
username=user1
host=192.168.0.1
type=peer
secret=123
qualify=yes
conntext=from-trunk
disallow=all
allow=alaw&ulaw
```

Incoming server 2
```
[user1]
type=user
secret=123
context=from-internal
disallow=all
allow=alaw&ulaw
```

Outgoing server 2
```
[offise2]
username=user2
host=192.168.0.2
type=peer
secret=321
qualify=yes
conntext=from-trunk
disallow=all
allow=alaw&ulaw
```

Incoming server 1
```
[user2]
type=user
secret=321
context=from-internal
disallow=all
allow=alaw&ulaw
```

## LinkSYS
```
[username]
secret=
type=friend
username=
qualify=yes
port=5061
nat=no
host=
dtmfmode=inband
context=from-pstn
canreinvite=no
```
