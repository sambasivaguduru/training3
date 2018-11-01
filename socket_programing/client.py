import socket
hostname="sambaemc"
port=9999
s=socket.socket()
s.connect((hostname,port))
resp=s.recv(1024)
print resp
n=raw_input("enter number:")
s.send(n)
resp = s.recv(10)
print "response:",resp
s.close()