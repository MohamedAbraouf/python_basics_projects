print("this tool to get the ip of a domain name ")
print("created  by  ENG mohamed abdelraouf")

import socket 

domain = input("enter the domain name to get the ip ")
ipOfDomain = socket.gethostbyname(domain)
print(ipOfDomain)
