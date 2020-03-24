#!/usr/bin/env expect

spawn openssl req -nodes -x509 -newkey rsa:4096 -keyout crypt/key.pem -out crypt/cert.pem
expect -re "Country Name .*:"
send -- "GB\n"
expect -re "State or Province Name .*:"
send -- "West Midlands\n"
expect -re "Locality Name .*:"
send -- "Birmingham\n"
expect -re "Organization Name .*:"
send -- "Banana Town\n"
expect -re "Organizational Unit Name .*:"
send -- "41464e4f4d7b314d5f6333727431463134384c595f38346e344e34737d\n"
expect -re "Common Name .*:"
send -- "wt.ctf\n"
expect -re "Email Address .*:"
send -- "monkey@wt.ctf\n"
interact