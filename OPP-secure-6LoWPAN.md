# DENYING THE DENIAL - SECURING 6LOWPAN AGAINST DOS
===================================================
Mitigation strategies to minimise vulnerabilities in IoT 802.15.4 protocol stack

## Objective
============
In wireless communication models, eavesdropper or malicious user can spoof identities freely, capture transmitted information and is free to carry out a wide range of attacks that are a bottleneck in industry implementation of Internet of Things models. Hence in this proposal we aim  
To come up with a secure protocol suite enabling mitigation strategies against
1. Layer 2, 3, 4 Denial of service vulnerabilities
2. Identity spoofing attacks  

==============================================================================================================================================
**How shall we do it?**
Allow the master device to validate/invalidate a packet in just 16 bytes, no need of deep packet inspection.
Packet structure
> 16 bytes hash || AES encrypted packet(Follows IPv6 packaging)  

**How are these hash bytes useful?**
This 16 bytes hash is
1. Unique to each device and provides context to communication between the master and slave devices.
2. This provided context helps against identity spoofing, denial of service through flooding and packet replay attacks.
3. Changes every time master and slave devices talk (One-time pad's provable security)
4. Even on capturing packets, no critical information can be revealed  
This 16 bytes hash F_H is
> F_H(RFD(slave) information, Sequence of packet, 16 bit right shifted unique identifier)  
*Sequence of packet* and *shifting of unique identifier* are two variables which change every time.
==============================================================================================================================================

## Costs - Long term and short term
===================================
**Short Term**
1. This system is implementable in hardware as well as software and hence can be adopted easily.
2. Computation requirements are added for every packet validation (*Creation of hash for every transmission on RFDs(slave) and Creation of hash + Comparison of hash for every device on master device*).
3. These added computation requirements mean the master device needs to be a capable device whereas slave devices are relatively free pf these.
**Long Term**
1. Once adopted this system will remove the bottleneck in IoT industry as a billion dollar business can't be built over an insecure model.
2. In critical systems where network layer vulnerability kills IoT implementation, this implementation is much cheaper as it allows sustainability in the long run.

## State-of-the-Art advancements which exist
============================================
1. IEEE 802.15.4 doesn't propose any solution for denial of service, identity spoofing and other network layer vulnerabilities.
2. Key exchange is a challenge as no official protocols have been declared for it.
3. Identity verification can be bypassed easily in the current existing recommendations.
4. Any solutions which exist are non-uniform in applicability and either do not deal with practical and industrial needs or leave a lot of loopholes by covering only a few problems.

## Limitations
1. So far only intra-PAN systems can b made secure with this proposed scheme.
2. In a global model of IoT, i.e where you need every device to be connected to every other device, it is not appliable. As it allows the slave devices to only talk to the master device.
3. Work needs to be done for extending the scheme to complex IoT challenges such as vehicular systems which have high security demands and identity verification techniques are at a loss.
