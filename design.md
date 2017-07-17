## Design of the system
-------------------
### Design of FFD
-------------------
1. It can be designed simply as a TCP server socket (Really going with the simplest design right now)
2. Though the actual functioning here would be point-to-point, we shall aim for what we intend to display and work accordingly
3. What shall be our output?
    1. FFD online
    2. Going through system status
    3. Master mode running || Install mode running || Can't get system status, **PRINT ERROR**
    4. **IF MASTER MODE**
        1. Contacting Device $i
        2. Connection successful || Failed to connect, Device $i not in range
        3. Receiving Data || Waiting to receive response from device $i
        4. Data successfully received || Couldn't receive data from $i, aborting
        5. Partition line for next device initiation
        6. Partition line for registration mode
    5. **IF INSTALL MODE**
        1. Sending beacon, registration cycle started
        2. Device has contacted
        3. Initiation verification of packet
        4. Displaying device info, please authenticate
        5. **DISPLAY DEVICE INFO**
        6. Authenticate? (Y/N)
        7. Registration request accepted || Registration request refused
        8. Registration period expired
        9. Partition line for master mode
    6. **IF ALERT MODE**
        1. Devices **LIST OF $i** not responding || **ATTACK NAME** signature detected 
        2. Continue normal operation? (Y/N)
        3. System under attack, lock down all systems
        4. Attempt recovery? (Y/N)
        5. Initiating recovery mode
        6. Partition line for alert mode
        
---------------------
### Design of RFD
---------------------
1. Designed simply as a TCP client and always connects to FFD
2. What shall be shown in output?
    1. **RUN ARGUMENT(device file)**
    2. RFD online
    3. Waiting for registration cycle || Preparing next sequence to be sent
    4. **IF REGISTERED**
        1. Reading device info from $device_file
        2. Preparing first packet to be sent
        3. **PREPARE PACKET**
        4. **SEND PACKET**
        5. Sending packet...
        6. Sent successfully || Couldn't send successfully.
        7. Partition line for sleep mode
