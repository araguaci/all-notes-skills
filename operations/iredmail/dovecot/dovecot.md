# Dovecot
_dovecot.conf_
```
userdb {
    args = /etc/dovecot/dovecot-ldap-ou.conf
    driver = ldap
}
passdb {
    args = /etc/dovecot/dovecot-ldap-ou.conf
    driver = ldap
}
```

_dovecot.conf_
mailbox directory via /
```
mail_location = maildir:%Lh/Maildir/:INDEX=%Lh/Maildir:LAYOUT=fs
```

_dovecot.conf_
```
mailbox Отправленные {
        auto = subscribe
        special_use = \Sent
    }
mailbox Черновики {
        auto = subscribe
        special_use = \Drafts
    }
mailbox Удаленные {
        auto = subscribe
        special_use = \Trash
    }
mailbox "Нежелательная почта" {
        auto = no
        special_use = \Junk
    }
```

_dovecot.conf_
plugins
```
mail_plugins = quota mailbox_alias acl mail_log notify stats
```

imap
```
mail_plugins = $mail_plugins imap_quota imap_acl imap_stats
```

return when quota full
```
quota_full_tempfail = yes
```

_dovecot.conf_
Maximum number of simultaneous client connections per process.
```
client_limit =
```

Number of client connections to handle until the process kills itself.
```
service_count =
```

Minimum number of processes that always should be available to accept more client connections.
```
process_min_avail =
```

Maximum number of processes that can exist for this service.
```
process_limit =
```

Limit the process's address space (both RLIMIT_DATA and RLIMIT_AS if available).
```
vsz_limit =
```

Authentication cache size
```
auth_cache_size =
```

Time to live in seconds for cache entries.
```
auth_cache_ttl =
```

Time to live in seconds for negative cache entries.
```
auth_cache_negative_ttl =
```

Maximum number of worker processes.
```
auth_worker_max_count =
```

Maximum number of concurrent connections
```
mail_max_userip_connections =
```

Password hash verifications are done by the auth master process by default
```
auth_cache_verify_password_with_worker =
```

Copy a message with hard links
```
maildir_copy_with_hardlinks=
```

_dovecot.conf_
```
quota = maildir:User quota
quota_rule = *:storage=2G
```

_dovecot.conf_
```
service anvil {
    process_limit = 1
    client_limit = 4096
}

service auth-worker {
    client_limit = 1
    service_count = 1
    process_limit = 60
}

service imap {
    service_count = 10
    process_min_avail = 2 # number of CPU cores
    process_limit = 4096
    client_limit = 10 # 1
}
```
````
auth_cache_size = 50331648
auth_cache_negative_ttl = 300
auth_worker_max_count = 30
```

_dovecot-ldap.conf_
```
hosts           = host:389
ldap_version    = 3
auth_bind       = yes
#auth_bind_userdn = %u
dn              = user
dnpass          = password
base            = ou=,dc=,dc=,dc=
scope           = subtree
deref           = never

user_filter     = (&(mail=%u)(objectClass=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
pass_filter     = (&(mail=%u)(objectClass=person)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))
user_attrs      = =home=/var/vmail/vmail1/%Ld/%Ln/Maildir/,=mail=maildir:/var/vmail/vmail1/%Ld/%Ln/Maildir/:UTF-8,=quota_rule=*:bytes=%{ldap:postOfficeBox}
pass_attrs      = userPassword=password, mail=user

default_pass_scheme = CRYPT
```
