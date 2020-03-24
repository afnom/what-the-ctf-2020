import pexpect

import hashlib
import string

# cache all printable character hashes
letters = {}
for ch in string.printable:
    hasher = hashlib.sha1()
    hasher.update(ch.encode())
    digest = hasher.digest().hex()

    letters[digest] = ch

# connect to ssh server
child = pexpect.spawn('ssh sha@localhost -p 4000')
child.expect('password: ')
child.sendline('ilikehashbrowns')

# run command
CMD = r"sed 's/./\0\n/g' flag.txt"
child.sendline(CMD)

# discard useless output
for i in range(3):
    child.readline()

# iterate through output lines
while (line := child.readline().decode().strip('$').strip()):
    print(letters[line], end='', flush=True)

    if letters[line] == '}':
        print()
        break

child.terminate()
