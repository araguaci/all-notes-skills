# Centos
## MOUNT
CIFS
```
//"host"/"path" /"path" cifs domain="",username="",password="",file_mode=0760,dir_mode=0760,vers=3.0,gid="" 0 0
```

## Network

_/etc/sysconfig/network-scripts/_
```
TYPE=Ethernet
PROXY_METHOD=static
BROWSER_ONLY=no
BOOTPROTO=none
IPV6_AUTOCONF=no
DEFROUTE=yes
IPV6INIT=yes
IPV6ADDR=
IPV6_DEFAULTGW=
IPV6_PRIVACY=no
DNS0=""
DNS1=""
DNS2=""
DOMAIN=""
```

IPv4 static
_/etc/sysconfig/network-scripts/_
```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
NAME=""
UUID=""
DEVICE=""
ONBOOT=yes
IPADDR=
PREFIX=
#NETMASK=
GATEWAY=
DNS1=
DNS2=
DOMAIN=
ZONE=internal
```

IPv4 dinamic
_/etc/sysconfig/network-scripts/_
```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
NAME=
UUID=
DEVICE=
ONBOOT=yes
ZONE=internal
```

VLAN
```
modprobe --first-time 8021q
```

_/etc/sysconfig/network-scripts/ifcfg-enpX_
```
TYPE=Ethernet
NAME=
DEVICE=
ONBOOT=yes
UUID=
```

_/etc/sysconfig/network-scripts/ifcfg-enpX.X_
```
TYPE=VLAN
ONBOOT=yes
VLAN=yes
DEVICE=enpX.X
```

_/etc/sysconfig/network-scripts/ifcfg-vlanX_
```
ONBOOT=yes
TYPE=VLAN
VLAN=yes
VLAN_NAME_TYPE=VLAN_PLUS_VID_NO_PAD
DEVICE=vlan5
PHYSDEV=ens32
VLAN_ID=5
```

Bridge
_/etc/sysconfig/network-scripts/ifcfg-brX_
```
DEVICE=
TYPE=Bridge
ONBOOT=yes
BOOTPROTO=none
IPV6INIT=no
IPV6_AUTOCONF=no
DELAY=5
STP=yes
```

_/etc/sysconfig/network-scripts/ifcfg-enpX_
```
DEVICE=enpX
BOOTPROTO=none
TYPE=Ethernet
NAME=
DEVICE=
ONBOOT=yes
UUID=
HOTPLUG=no
BRIDGE=brX
```

## File, socket limits
_/etc/sysctl.conf_

Maximum of objects inotify per user
```
fs.inotify.max_user_instances=
```

Maximum of watch files and directories per object inotify
```
fs.inotify.max_user_watches=
```

Maximum of events in queued
```
fs.inotify.max_queued_events=
```

Maximum of open descriptors
```
fs.file-max=
```

Maximum queue size of packet
```
net.core.netdev_max_backlog =
```

Maximum number of open sockets waiting to be connected
```
net.core.somaxconn =
```

## PAM limits configuration
_/etc/security/limits.conf_, _/etc/security/_
```
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
```

_/etc/systemd/system.conf_, _/etc/systemd/user.conf_,  _/etc/systemd/<systemd_unit>/override.conf_
```
DefaultLimitNOFILE=
```

_/lib/systemd/system/<service>_, _/etc/systemd/*_, _/usr/lib/systemd/system/<service>_
```
LimitNOFILE=
```

_override.conf_
```
mkdir /etc/systemd/system/service_name.service.d/
```
```
[Service]
LimitNOFILE=100000
```

## Swap

_/etc/sysctl.conf_
```
vm.swappiness=10
```

## Environment

_/etc/environment_
```
export PYTHONPATH=/data/libraries_and_modules/python
```

## TFTP
```
server_args             = -u tftpd -s /var/lib/tftpboot --verbose/-vvv
disable                 = no
```

## PHP-FPM
```
rpm -Uhv http://rpms.remirepo.net/enterprise/remi-release-7.rpm
yum install yum-utils
yum-config-manager --enable remi-php72
yum install php72
yum install -y php-mysql php-mbstring php-mcrypt php-devel php-xml php-gd
```

## Kernels
 Remove old kernels
```
yum install yum-utils
package-cleanup --oldkernels --count=2
```

Automatic remove old kernels
_/etc/yum.conf_
```
installonly_limit=3
```

## SysRq
Enable
* On work
```
sysctl kernel.sysrq=1
echo "1" > /proc/sys/kernel/sysrq
```

* On boot
```
echo "kernel.sysrq = 1" >> /etc/sysctl.d/99-sysctl.conf
```

* Before mounting and ini

_Kernel_
```
sysrq_always_enabled=1
```

## Sudoers
_/etc/sudoers_
Write logs
```
Defaults  log_host, log_year, logfile="/var/log/sudo.log"
```

Run command with sudo without password
```
notify ALL=(ALL) NOPASSWD:path_to_command, path_to_command
```

## Entropy
Install
```
yum/dnf install haveged
```

Start
```
systemctl enable haveged
systemctl start haveged
```
