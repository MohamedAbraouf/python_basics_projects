print("hello, world!!")
print("this python tool is a simple terminal...")
print("created by ENG: Mohamed Abdelraouf")
print("===========================================")

while True :
    import os 
    command = input("enter a command for execution \n>>   ")
    result = os.system(command)
    print(result)
