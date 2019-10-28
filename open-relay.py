#!/usr/bin/python

import socket
import sys
import argparse
import time

class bcolors:
        HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def get_args():
	parser = argparse.ArgumentParser(description="SMTP Username Enumeration")
	parser.add_argument("-t", "--target", type=str, help="Target IP", required=True)
	parser.add_argument('-p', '--port', type=str, help='SMTP PORT', required=True)
	parser.add_argument('-s', '--sender', type=str, help="Senders email", required=True)
	parser.add_argument('-r', '--receiver', type=str, help="Receivers email", required=True)
	parser.add_argument('-d', '--domain', type=str, help="HELO domain.com", required=True)
	args = parser.parse_args()

	target = args.target
	port = args.port
	sender = args.sender
	receiver = args.receiver
	domain = args.domain

	return target, port, sender, receiver, domain

def main():
	target, port, sender, receiver, domain = get_args()

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect((target, int(port)))

	banner=s.recv(1024)
	print bcolors.OKBLUE+banner+bcolors.ENDC

	print 'HELO '+domain+'<CRLF>'
	s.send('HELO '+domain+'\r\n')
	result=s.recv(1024)
	print result

	print 'MAIL FROM: '+sender+'<CRLF>'
	s.send('MAIL FROM: '+sender+'\r\n')
	result=s.recv(1024)
	print result

	print 'RCPT TO: '+receiver+'<CRLF>'
	s.send('RCPT TO: '+receiver+'\r\n')
	result=s.recv(1024)
	print result

	print 'DATA<CRLF>'
	s.send('DATA\r\n')
	result=s.recv(1024)
	print result

	print 'Subject: test<CRLF>'
	print 'Hello,\r\nThis is a mail spoofing test.  If the mail is delivered, please inform <YOUR NAME> at <YOUR CONTACT EMAIL>\r\n.\r\n'
	s.send('Subject: test\r\n')
	s.send("Hello,\r\nThis is a mail spoofing test.  If the mail is delivered, please inform <YOUR NAME> at <YOUR CONTACT EMAIL>\r\n.\r\n")
	result=s.recv(1024)
	print result

	s.close()

if __name__ == '__main__':
	main()
