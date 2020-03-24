#!/usr/bin/python3
import os
import sys
import time
import pipes
import socket
import traceback
import threading
import subprocess
from colorama import Fore, Style

RESET = Fore.RESET+ Style.NORMAL
BRIGHT_GREEN = Fore.GREEN + Style.BRIGHT
BRIGHT_RED = Fore.RED + Style.BRIGHT


symbols = (u"абвгдеёжзийклмнопрстуфхцчшщыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcssyeuaABVGDEEJZIJKLMNOPRSTUFHZCSSYEUA")
# u'Добрый Ден'

def eng_to_ru(text):
    return text.translate({ord(b):ord(a) for a, b in zip(*symbols)})

def ru_to_eng(text):
    return text.translate({ord(a):ord(b) for a, b in zip(*symbols)})

def banner():
    return '''
    WELCOME COMRADE!!!!
'''

def delete_source():
    """delete our own source code to stop naughty users getting hold of us ;)"""
    subprocess.run("rm -f /home/comrade/russia.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                                            timeout=30, executable='/bin/bash')

class socket_nice_wrapper():

    def __init__(self, sock):
        self.sock = sock

    def send(self, data):
        if isinstance(data, bytes):
            self.sock.send(data)
        elif isinstance(data, str):
            for x in data:
                self.sock.send(x.encode('utf-8'))
                time.sleep(0.1)

class Interpreter():

    commands = ["ls", "ll", "la", "cat", "pwd", "fortune", "help", "which", "wisdom", "echo", "whoami", "groups", "export"]
    banned = set("?&><|;`{}()^")
    def __init__(self):
        self.env = os.environ.copy()

    def execute(self, command):
        try:
            command_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30, shell=True, env=self.env)
            # send back the resulting output
            if len(command_output.stderr.decode('utf-8')):
                return (command_output.stderr.decode('utf-8'))
            elif len(command_output.stdout.decode('utf-8')):
                return (command_output.stdout.decode('utf-8'))
            else:
                return ('')
        except subprocess.CalledProcessError as err:
            return (str(err))

    def run(self, command):
        parts = command.split()
        if len(parts) == 0:
            return ""
        if parts[0] not in self.commands:
            return "command is not allowed, use the help command for more information"
        elif set(command) & self.banned != set():
            return "characters " + ", ".join(set(command) & self.banned) + " are not allowed"
        else:
            parts = [p for p in parts if p.strip() != ""]
           
            if parts[0] == "help" and len(parts) == 1:
                return "Available commands:\n" + "\n".join([("  - " + c) for c in self.commands])
            
            # actually using shell export function won't work, so here's a hacky workaround
            elif parts[0] == "export" and len(parts) == 2:
                sides = parts[1].split("=")
                if len(sides) == 2:
                    variable = parts[1].split("=")[0]
                    value = parts[1].split("=")[1]
                    self.env[variable]=value
                    return str(variable) + "=" + str(self.env[variable])
            
            # hacks to make ll and la work
            elif parts[0] == "ll":
                if len(parts) == 1:
                    parts.append("")
                return self.execute("ls -l " + parts[1])
            elif parts[0] == "la":
                if len(parts) == 1:
                    parts.append("")
                return self.execute("ls -a " + parts[1])
            elif parts[0] == "fortune":
                return "fortune is not patriotic enough! use glorious wisdom russian quote generator instead!"
            elif len(parts) > 2:
                return "Command too long, usage = <command> <data>"
            else:
                return self.execute(command)

def run_server():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        sock.bind(("", 1111))
    except Exception as e:
        print("[!] Bind Error: " + str(e))
        traceback.print_exc()
        sys.exit(1)

    try:
        sock.listen(100)
        while True:
            print("[*] Listening")
            client, addr = sock.accept()
            client.settimeout(60);
            threading.Thread(target=communicate_with_client, args=(client,addr)).start()
    except Exception as e:
        print("[!] Listen/accept failed: " + str(e))
        traceback.print_exc()
        sys.exit(1)

def communicate_with_client(client, addr):
    
    try:
        s = socket_nice_wrapper(client)
        print("[*] Connection accepted")
        interpreter = Interpreter()
        s.send((BRIGHT_RED + eng_to_ru(banner()) + RESET).encode('utf-8'))
        while True:
            s.send(eng_to_ru("Enter command> "))
            command = client.recv(1024).decode('utf-8')
            s.send(eng_to_ru(interpreter.run(command) + "\n"))
    except Exception as e:
        print("EXCEPTION!")
        print(traceback.format_exc())
        print(e)

    client.close()
    return

if __name__ == "__main__":
    delete_source()
    run_server()