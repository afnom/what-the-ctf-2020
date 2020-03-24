#!/usr/bin/python3

import os
import random
import sys
import subprocess

# Not sure our computer has enough memory to load this file into memory, let's use head to only get some of it

command = "/opt/head " + os.environ['quotes_file'] + " > /tmp/file"
command_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=30, executable='/bin/bash')

with open("/tmp/file", encoding='utf-8') as f:
	lines = f.readlines()
	sys.stdout.buffer.write(lines[random.randint(0, len(lines)-1)].encode('utf-8'))
