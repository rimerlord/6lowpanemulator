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

# checking if program was invoked with correct set of arguments
if len(sys.argv) != 4:
	print("Usage: python %s <slavesocket> <mastersocket> <slavename>" % sys.argv[0])
	sys.exit()

# Defining system variables
localhost = '127.0.0.1'
rfd_address = (localhost, int(sys.argv[1]))
ffd_address = (localhost, int(sys.argv[2]))
rfd_identity = sys.argv[3]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(rfd_address)
rfd_info= ""

# Setting timeout and non-blocking condition
sock.setblocking(0)
sock.settimeout(7)

########################################### Functions ##########################################################
#function to set sequence no.of next packet
def set_seq():
	sql = "UPDATE register set sequence = sequence + 1 where cli_name = '%s'" % rfd_identity
	cursor.execute(sql)

# function to send next packet in sequence
def send_next():
	set_seq()
	string = rfd_identity
	sock.sendto(string, ffd_address)

# function to fetch client row from table "register"
def fetch_register(cli_name):
	sql = "select * from register where cli_name = %s" % cli_name
	cursor.execute(sql)
	res = cursor.fetchall()
	return res

# function to generate next hash
def get_hash(update):
	res = fetch_register(rfd_identity)
	if update == False:
		for i in [res[4], res[3], res[2]]:
			hash_obj.update(str(i))
	else:
		hash_obj.update(res[2])
	hash_str = hash_obj.digest()
	print("Hashing %s" % hash_str)
	return hash_str
	
# function to get rfd info from database
def get_info():
	sql = "select info from rfd where name = '{}'".format(rfd_identity)
	cursor.execute(sql)
	res = cursor.fetchone()
	return res[0]

# function to send registration request
def send_reg_request():
	auth_code = "0"*16
	string = auth_code + "||" + rfd_identity + "||" + get_info()
	sock.sendto(string, ffd_address)

# function to handle reception of packet
def recv_packet():
	try:
		data, address = sock.recvfrom(1024)
	except socket.timeout:
		return 'socket timeout'
	if address == ffd_address:
		return data
	else:
		return 'not server'

# function to listen if beacon has been broadcasted
def listen_beacon():
	data = recv_packet()
	if data == "reg_cycle_start":
		print("Registration cycle has started")
		return True
	else:
		False
