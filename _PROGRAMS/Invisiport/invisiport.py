# -*- coding: utf-8 -*-
#!/usr/bin/env python
import socket
import os
import argparse

#블랙리스트에 들어가지 않을 호스트들 
whitelist = ['127.0.0.1','localhost']

#블랙리스트에 오른 클라이언트에게 열린 것처럼 보여줄 포트들
#ports = ['21','80','445']


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--triggerport", type=int, help="A scan here will trigger the defenses", required=True)
parser.add_argument("-f", "--fakeport", type=int, nargs='+', help="ports to show as up to blacklisted clients", required=True)
parser.add_argument("-a", "--allowport", type=int,  nargs='+', help="ports not to fake")
parser.add_argument("-r", "--redirectport", type=int, help="port to redirect")
args = parser.parse_args()

#IP to bind to.  Leave as empty string to bind to all available IPs
ADDR=''


#Name of blacklist file
filename = "blacklist"

def add_blacklist(ip):
	fi = open(filename,"a")
	fi.write(" "+ip)
	fi.close()

def check_blacklist(ip):
	fi = open(filename,"r")
	data = fi.read()
	fi.close()
	return ip in data

def blacklist(ip):
	if ip in whitelist or check_blacklist(ip):
		return False
	else:
		
		#drop except cowrie and portspoof
		query = "iptables -A INPUT -s %s -p tcp" % (ip) 
		if args.allowport :
			query += " -m multiport ! --destination-port " + str(args.allowport)[1:-1].replace(" ", "")
		query +=  " -j DROP"
		os.system(query)

		#config redirect
		for port in args.fakeport:
			query = "iptables -t nat -A PREROUTING -s %s -p tcp --dport %s -j REDIRECT --to-port %s" % (ip,port, str(args.redirect))
			os.system(query)

		add_blacklist(ip)
	return True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ADDR, args.triggerport))
s.listen(5)

while True:
	con, adr = s.accept()
	try:
		data = con.recv(2048)
		con.send("Protocol Error")
		con.close()
	except:
		print "Socket error"
	blacklist(adr[0])
