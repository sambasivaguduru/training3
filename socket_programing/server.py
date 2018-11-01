"""
hostname, port
url: bind(host,port)
wait for client request
got request-> accpet-> process the request-> send response back to client
"""
import socket
import json
from time import sleep
hostname = socket.gethostname()
port=9999
try:
	s=socket.socket()
	s.bind((hostname,port))
	print "service running in %s:%s"%(hostname,port)
	while 1:
		s.listen(12)
		print "waiting for the client request..."
		client_socket,client_info = s.accept()
		resp="connected successfully"
		client_socket.send(json.dumps(resp))
		number = client_socket.recv(10)
		resp = "EVEN" if int(number)%2==0 else "ODD"
		sleep(3)
		client_socket.send(resp)

except Exception as err:
	print "something went wrong"
	print err
finally:
	s.close()
