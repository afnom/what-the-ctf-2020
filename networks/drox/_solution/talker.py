import socket
from xor import XorSocket
import sys


def listen():
	sock = XorSocket(socket.AF_INET, socket.SOCK_STREAM)
	sock.random=False
	sock.bind(("", 1337))
	sock.listen()
	client, _ = sock.accept()

	
	client.send("Hey mate, I heard you've been working on something new".encode('utf-8'))
	print(client.recv(1024).decode('utf-8'))
	client.send("idk, seems kind of insecure, what did you pad it with?".encode('utf-8'))
	print(client.recv(1024).decode('utf-8'))
	client.send("what was that super secret thing you wanted to tell me".encode('utf-8'))
	print(client.recv(1024).decode('utf-8'))
	sock.close()


def connect():
	sock = XorSocket(socket.AF_INET, socket.SOCK_STREAM)
	sock.random = False
	print(sock.get_enabled())
	sock.connect(("localhost", 1337))
	print("[*] Connected")
	print(sock.recv(1024).decode('utf-8'))
	sock.send("Yeah, do u like my new super secure secret encryption?".encode('utf-8'))
	print(sock.recv(1024).decode('utf-8'))
	sock.send("Zeros of course! What are you talking about?".encode('utf-8'))
	print(sock.recv(1024).decode('utf-8'))
	sock.send("anyway heres my cool flag AFNOM{S3curity_by_ob5curity}".encode('utf-8'))
	print("[*] Sent")
	sock.close()


if __name__ == "__main__":
	if "-l" in sys.argv:
		listen()
	else:
		connect()









