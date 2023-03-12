## fiz systemclt for wsl2

```
mv /usr/bin/systemctl /usr/bin/systemctl.old
```

```
curl https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py > /usr/bin/systemctl
```

```
chmod +x /usr/bin/systemctl
```

