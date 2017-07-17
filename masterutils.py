import MySQLdb
import socket
import sys
import hashlib

# Open database connection
db = MySQLdb.connect("localhost","root","eighty8!","6lowpanemulator")

# Prepare a cursor object using cursor method
cursor = db.cursor()
db.autocommit(True)

#create a md5 hash object
hash_obj = hashlib.md5()
hash_obj.update("")

# Defining system variables
localhost = '127.0.0.1'
max_cli = 7
found_cli = 0

#create a udp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to the server
server_address = (localhost, 7777)
sock.bind(server_address)
# Create a non-blocking socket with a timeout of 5s
sock.setblocking(0)
sock.settimeout(5)

###################################################Functions############################################################
# function to remove clients that are above a certain threshold timeout
def remove_idle():
	sql = "delete from register where idle > 5"
	cursor.execute()

# function to validate hash received in the packet
def validate_hash(hash_str, cli_name):
	if hash_str == get_hash(cli_name, True):
		print("Received hash validated")
		return True
	else:
		return False

# function to increment idle value in client
def idle(cli_id):
	sql = "update register set idle = idle + 1 where cli_id = {}".format(cli_id)
	cursor.execute(sql)

# function to receive packet from a client and see if from the intended receiver
def recv_packet():
	try:
		data, address = sock.recvfrom(1024)
		return data
	except socket.timeout:
		return 'socket timeout'

# function to wake up sockets for communication
def wake_up(address):
	serv = (localhost, address)
	sock.sendto("wake up", serv)

# function to fetch all clients from table "register"
def fetch_clients():
	sql = "select * from register"
	cursor.execute(sql)
	res = cursor.fetchall()
	return res

# function to fetch client row from table "register"
def fetch_register(cli_name):
	sql = "select * from register where cli_name = %s" % cli_name
	cursor.execute(sql)
	res = cursor.fetchall()
	return res

# function to send ack packet with hash in it
def ack_device(address, in_str, reg_or_not):
	if reg_or_not == "reg":
		string = reg_or_not
	elif reg_or_not == "not":
		string = reg_or_not + "||" + in_str + "||" + str(get_euid())
	sock.sendto(string, address)

# function to get md5 hash
def get_hash(cli_name, update):
	res = fetch_register(cli_name)
	if update == False:
		for i in [res[4], res[3], res[2]]:
			hash_obj.update(str(i))
	else:
		hash_obj.update(res[2])
	hash_str = hash_obj.digest()
	print("Hashing %s" % hash_str)
	return hash_str

#function to get latest meuid
def get_euid():
	sql = "select max(euid) from register"
	cursor.execute(sql)
	res = cursor.fetchone()[0]
	if res == None:
		return 1
	else:
		return res

# function to register a client in the system
def register(cli_name, cli_data, address):
	sql = "INSERT INTO register (cli_name, euid, info, address) VALUES ('%s', '%s', '%s', '%s')"
	meuid = get_euid()
	val = (cli_name, meuid + 1, cli_data, address[1])
	cursor.execute(sql % val)

#function to check if a device is already registered or not
def is_registered(client_name):
	sql = "select idle from register where cli_name = '%s'" % client_name
	cursor.execute(sql)
	try:
		res = cursor.fetchone()[0]
		if res == 1:
			print("Device has timed out, re-register.")
			return False
		elif res == 0:
			print("Device is registered, can't register.")
			return True
		else:
			print("Device is unregistered, register.")
			return False
	except TypeError:
		print("Device is unregistered, register.")
		return False

# function to verify identity of registration attempt
def verify_identity(cli_name):
	if is_registered(cli_name) == False:
		sql = "select val_inval from trust_auth where client_name = '%s'"
		cursor.execute(sql % (cli_name))
		res = cursor.fetchone()[0]
		a = [res, cli_name]
	else:
		a = ["is registered", cli_name]
	return a

# function to listen registration attempt
def listen_attempt():
	print("Listening for any registration attempts")
	try:
		data, address = sock.recvfrom(1024)
	except socket.timeout:
		print("Socket Timeout")
		return ("socket timeout", None, None)
	auth = "0"*16
	try:
		auth_code, rfd_identity, rfd_info = data.split("||")
	except ValueError:
		print("Received " + data)
		return [None, None, None]
	if auth_code == auth:
		return [rfd_identity, rfd_info, address]
	else:
		return [None, None, None]

# function to broadcast packets
def broadcast(packet, start_sock, end_sock):
	for i in range(start_sock, end_sock+1):
		address = (localhost, i)
		sent = sock.sendto(packet, address)
		if sent == len(packet):
			pass
		else:
			return False
	return True

def send_beacon():
	#broadcast beacon packet to all sockets
	success = broadcast("reg_cycle_start", 5001, 5007)
	if success == True:
		print("Beacon broadcasted for marking beginning of registration cycle")
	else:
		sys.exit()

# function to get no. of registered clients
def get_reg_cli():
	sql = "select count(*) from register"
	cursor.execute(sql)
	reg_cli = cursor.fetchone()[0]
	return reg_cli
