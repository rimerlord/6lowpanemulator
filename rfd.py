import slaveutils as slave
import sys

#system boot
listen = 1
print("***************************Slave device Online****************************************")
while 1:
	while listen:
		print("Waiting for registration to start")
		if slave.listen_beacon():
			print("Attempting registration")
			slave.send_reg_request()
			data = slave.recv_packet()
			if data == "not server":
				print("Received packet from a non-server device, rejecting")
			elif data == "socket timeout":
				print("Registration failed, timeout")
			elif data == "reg":
				print("Already registered")
				listen = 0
			else:
				try:
					reg_or_not, hash_str, euid = data.split("||")
				except ValueError:
					print("Received '%s', unexpected") % data
					continue
				if reg_or_not == "not":
					print("Registered")
					listen = 0
		else:
			print("Received something else, rejecting")
	print("Waiting for wake up call ")
	data = slave.recv_packet()
	if data == "not server":
		print("Contacting device isn't server, rejecting the packet")
	elif data == "socket timeout":
		print("Socket timeout")
	elif data == "wake up":
		print("Wake up call received")
		print("Sending next packet")
		slave.send_next()
	else:
		print("Unexpected reception, rejecting")
