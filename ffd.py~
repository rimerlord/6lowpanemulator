import masterutils as master
import sys

#System boot
print("**************************Master device online*******************************")
while 1:
	print("**************************Registration mode online***************************")
	rounds = 0
	master.send_beacon()
	master.found_cli = 0
	while master.get_reg_cli() < master.max_cli and master.found_cli != -1 and rounds < 7:
		cli_name, cli_data, address = master.listen_attempt()
		if cli_name != "socket timeout" and cli_name != None:
			state, cli_name = master.verify_identity(cli_name)
			if state == "is registered":
				print("Device is already registered")
				master.ack_device(address, "is registered", "reg")
				master.found_cli = -1
			elif state == "is valid":
				print("Device is valid, registering")
				master.register(cli_name, cli_data, address)
				master.ack_device(address, "is valid", "not")
				master.found_cli = 1
			elif state == "is invalid":
				print("is invalid, rejecting the packet")
				master.found_cli = -1
		elif cli_name == "socket timeout":
			print("Socket timeout, No attempt made")
			master.found_cli = -1
		else:
			print("Unexpected packet received")
		rounds = rounds + 1
	print("************************Master Mode online***********************************")
	for client in master.fetch_clients():
		master.wake_up(client[5])
		print("Waking up client %s") % client[1]
		data = master.recv_packet()
		if data == client[1]:
			print("Packet successfully received from %s") % client[1]
		elif data == "socket timeout":
			print("Socket timeout")
		else:
			print("Illegal sender, rejecting")
