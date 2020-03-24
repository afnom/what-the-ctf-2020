import struct
import socket
import random as ran

debug_on = False

def debug(string):
	if debug_on:
		print(string)

class XorSocket(socket.socket):

	enabled = True

	key = b'xord'

	PACKET_SIZE = 58

	buffer = bytes()

	debug = True

	def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
		super().__init__(family, type, proto, fileno)
		self.enabled = True
	
	def get_enabled(self):
		return self.enabled

	def set_enabled(self, enabled):
		debug("SETTING ENABLED " + str(enabled))
		self.enabled = enabled

	def xor(self, data):
		xord = bytes(''.join([chr((self.key[i%len(self.key)]) ^ (data[i])) for i in range(max(len(self.key), len(data)))]), 'utf-8')
		return xord

	def pad(self, data, size, random):
		if len(data) > size:
			raise Exception("Cannot pad data size " + str(len(data)) + " to " + str(size))

		if random:
			r = ran.Random()
			data += bytes(''.join([chr(r.randint(0, 8)) for i in range(size-len(data))]), 'utf-8')
		else:
			data += bytes('\x00' * (size-len(data)), 'utf-8')

		return data

	def chunk(self, data, random):
		copy = data
		chunks = []

		data_size = self.PACKET_SIZE - 4

		while len(copy) > data_size:
			chunk = struct.pack("I", data_size)
			chunk += (copy[:data_size])

			chunks.append(chunk)

			copy = copy[data_size:]

		debug(struct.pack("I", len(copy)))
		chunk = struct.pack("I", len(copy))
		chunk += self.xor(self.pad(copy, data_size, random))

		chunks.append(chunk)

		return chunks

	def send(self, data):
		debug("Sending " + str(len(data)))
		if self.enabled:
			for chunk in self.chunk(data, random=False):
				debug(chunk)
				part_size = super().send(chunk)
				debug(part_size)

			debug("return " + str(len(data)))
			return len(data)
		else:
			size = super().send(data)

		return size

	def recv(self, size):
		#debug("RECV CALLED " + str(size))
		if self.enabled:
			if len(self.buffer) >= size:
				data = self.buffer[:size]
				self.buffer = self.buffer[size:]
				
			else:

				# receive new chunks until our buffer can be returned
				newchunk = super().recv(self.PACKET_SIZE)
				debug("RECEIVED PACKET: " + str(newchunk))
				if len(newchunk)==0:
					raise socket.timeout
				header_size = struct.calcsize("I")
				debug("header size: " + str(header_size))
				debug("header: " + str(newchunk[:header_size]))
				l = struct.unpack("I", newchunk[:header_size])[0]
				debug("len recvd: " + str(l))
				self.buffer += self.xor(newchunk[header_size:header_size+l])

				debug(str(len(self.buffer)) + " out of " + str(size))
				data = self.buffer[:size]
				self.buffer = self.buffer[size:]

		else:
			data = super().recv(size)
		debug("Returning: ")
		debug(data)
		return data


	def accept(self):
		fd, addr = self._accept()
		sock = XorSocket(self.family, self.type, self.proto, fileno=fd)
		if socket.getdefaulttimeout() is None and self.gettimeout():
			sock.setblocking(True)

		return sock, addr



if __name__ == '__main__':
	pass
	# debug([(chr(i)) for i in range(256)])
	

