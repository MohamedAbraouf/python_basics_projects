#simple python code to get hostname and address of host name

import socket 

my_pc_name = socket.gethostname()
print("local host name is ", my_pc_name)


IP = socket.gethostbyname(my_pc_name)
print("the address of the local host is ",IP)

 
