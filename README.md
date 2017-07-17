## 6lowpanemulator

0. master ---> all slaves
Beacon to signify start of registration cycle

> "reg\_cycle\_start"

1. slave ---> master
Packet sent for registration

> "0"*16 + "||" + "rfd1" + "||" + "Reduced function device 1"  

2. master ---> slave
Packet sent for acknowledgement

> "reg_ok"  
if the device is already registered
> enc(hash_str + str(meuid[0]))  
if the device is successfully registered

3. master ---> slave
Packet sent for waking up from sleep

> "wake up"

4. slave ---> master
Packet sent in communication

> update(hash_str, seq++) + enc(data)
