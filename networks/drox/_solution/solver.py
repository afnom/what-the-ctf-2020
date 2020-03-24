import pyshark
cap = pyshark.FileCapture('drox.pcapng')

key = b'xord'

for packet in cap:
	try:
		data = bytes([int(x, 16) for x in packet.tcp.payload.split(":")])
		r = range(max(len(key), len(data)))
		print(''.join([chr((key[i%len(key)]) ^ (data[i])) for i in r]))
		

	except Exception as e:
		print(e)
