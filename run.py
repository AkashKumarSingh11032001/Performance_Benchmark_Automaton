from mainbcp0 import ExeBPC0
from mainbcp1 import ExeBPC1
from hmb import HmbOnOff
from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from os.path import dirname

# x= dirname(__file__)
# print("{}\\burst.txt".format(x))

user_server = input("\nPlease Enter Ip address: ")

print("\n1 - Both BPC0 and BPC1")
print("2 - Only BPC0")
print("3 - Only BPC1\n")
Opr = input("Select Opration you want to Perform on your drive: ")


if Opr == "1":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")
    
    
    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    # ExeBPC0(user_server)
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    # ExeBPC1(user_server)
    
    # <<<<< HMB Condition >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tTurning HMB ON -> HMB OFF\t")
    print("\n|||||||||||||||||||||\n")
    
    
    HmbOnOff(user_server, "root", "12", "/root/fio/")
    
    # <<<<< HMB OFF >>>>>
    # print("\n||||||||||||||||||||| HMB OFF |||||||||||||||||||||\n")
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB OFF\t ")
    print("\n|||||||||||||||||||||\n")
    
    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    # ExeBPC0(user_server)
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    # ExeBPC1(user_server)
    
    print("\n ************ Task Accomplished ************ ")
    
elif Opr == "2":
    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server)
    print("\n ************ Task Accomplished ************ ")
    
elif Opr == "3":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server)
    print("\n ************ Task Accomplished ************ ")
    
else:
    print("Please choose Appropiate option!")
    exit()