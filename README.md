# open-relay
Script to test SMTP Open Relay (Great for Social Engineering Engagements)
# Help Menu:
```# ./open-relay.py -h
usage: open-relay.py [-h] -t TARGET -p PORT -s SENDER -r RECEIVER -d DOMAIN

SMTP Username Enumeration

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP
  -p PORT, --port PORT  SMTP PORT
  -s SENDER, --sender SENDER
                        Senders email
  -r RECEIVER, --receiver RECEIVER
                        Receivers email
  -d DOMAIN, --domain DOMAIN
                        HELO domain.com
```
# Example Usage:
```
./open-relay.py -t <TARGET-IP> -p 25 -s <SPOOFEDEMAIL@CLIENT.COM> -r <TARGETEMAIL@CLIENT.COM> -d <DOMAIN-USED-FOR-HELO>
```
