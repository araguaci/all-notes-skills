mkdir /root/log/
cp `find /var/www/html/ -mtime -60` /var/log/ -n

## Find Files that have been modified in the last 14 days

```
find . -name "*.php" -mtime -14 -print
```

## Copying / Tarring Files that have been modified in the last 14 days

```
find . -name "*.php" -mtime -14 -print | xargs tar cvf /var/log/backup.tar
```
