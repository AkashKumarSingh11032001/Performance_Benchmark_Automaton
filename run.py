from mainbcp0 import ExeBPC0
from mainbcp1 import ExeBPC1
from hmb import HmbOnOff
from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from os.path import dirname
from BPC1 import bpc1

localPath = dirname(__file__)
# print("{}\\burst.txt".format(x))

# Firmware_release = input("\nPlease Enter Firmware Release(eg. FC3 / FC3.3): ")

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
    bpc_1 = "{0}\\preCondition\\bpc1.txt".format(localPath)
    bpc1(user_server, "root", "12", "/root/fio/", bpc_1)
    status("<--------- Precondition BPC1 is been implemented! --------->", 1)

elif Opr == "2":
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

elif Opr == "3":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server, "HMB_ON")
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "HMB_ON")
    print("\n ************ Task Accomplished ************ ")
elif Opr == "4":
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

elif Opr == "5":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server, "HMB_ON")

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

    print("\n ************ Task Accomplished ************ ")
elif Opr == "6":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")

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

    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "HMB_OFF")

    print("\n ************ Task Accomplished ************ ")
elif Opr == "7":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server, "HMB_ON")

    print("\n ************ Task Accomplished ************ ")
elif Opr == "8":
    # <<<<< HMB ON >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB ON\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "HMB_ON")

    print("\n ************ Task Accomplished ************ ")
elif Opr == "9":

    # <<<<< HMB Condition >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tTurning HMB ON -> HMB OFF\t")
    print("\n|||||||||||||||||||||\n")

    # HmbOnOff(user_server, "root", "12", "/root/fio/")

    # <<<<< HMB OFF >>>>>
    # print("\n||||||||||||||||||||| HMB OFF |||||||||||||||||||||\n")
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB OFF\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server, "HMB_OFF")

    print("\n ************ Task Accomplished ************ ")
elif Opr == "10":

    # <<<<< HMB Condition >>>>>
    print("\n|||||||||||||||||||||\n")
    print(" \tTurning HMB ON -> HMB OFF\t")
    print("\n|||||||||||||||||||||\n")

    # HmbOnOff(user_server, "root", "12", "/root/fio/")

    # <<<<< HMB OFF >>>>>
    # print("\n||||||||||||||||||||| HMB OFF |||||||||||||||||||||\n")
    print("\n|||||||||||||||||||||\n")
    print(" \tHMB OFF\t ")
    print("\n|||||||||||||||||||||\n")

    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server, "HMB_OFF")

    print("\n ************ Task Accomplished ************ ")
else:
    print("Please choose Appropiate option!")
    exit()
