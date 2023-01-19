from mainbcp0 import ExeBPC0
from mainbcp1 import ExeBPC1
from hmb import HmbOnOff
from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from os.path import dirname

# x= dirname(__file__)
# print("{}\\burst.txt".format(x))

user_server = input("\nPlease Enter Ip address: ")

print("\n1 - BPC1")
print("2 - Both (BPC0 + Fios) and (BPC1 + Fios) For HMB On / OFF")
print("3 - Both (BPC0 + Fios) and (BPC1 + Fios) For HMB On")
print("4 - Both (BPC0 + Fios) and (BPC1 + Fios) For HMB OFF")
print("5 - Only (BPC0 + Fios) For HMB On / OFF")
print("6 - Only (BPC1 + Fios) For HMB On / OFF")
print("7 - Only (BPC0 + Fios) For HMB On")
print("8 - Only (BPC1 + Fios) For HMB On")
print("9 - Only (BPC0 + Fios) For HMB OFF")
print("10 - Only (BPC1 + Fios) For HMB OFF\n")
Opr = input("Select Opration you want to Perform on your drive: ")

if Opr == "1":
    pass
elif Opr == "3":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server, "HMB_ON")
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "HMB_ON")

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
    ExeBPC0(user_server, "HMB_OFF")
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "HMB_OFF")

    print("\n ************ Task Accomplished ************ ")

elif Opr == "2":
    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "3":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "4":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "5":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "6":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "7":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "8":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "9":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "")
    print("\n ************ Task Accomplished ************ ")
else:
    print("Please choose Appropiate option!")
    exit()
