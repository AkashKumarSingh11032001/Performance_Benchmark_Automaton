from mainbcp0 import ExeBPC0
from mainbcp1 import ExeBPC1

from os.path import dirname
# x= dirname(__file__)
# print("{}\\burst.txt".format(x))

user_server = input("Please Enter Ip address: ")

print("\n1 - Both BPC0 and BPC1")
print("2 - Only BPC0")
print("3 - Only BPC1\n")
Opr = input("Select Opration you want to Perform on your drive: ")


if Opr == "1":
    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server)
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server)
elif Opr == "2":
    print("\n<<<<<<<< BPC0 Triggered! >>>>>>>>\n")
    ExeBPC0(user_server)
elif Opr == "3":
    print("\n<<<<<<<< BPC1 Triggered! >>>>>>>>\n")
    ExeBPC1(user_server)
else:
    print("Please choose Appropiate option!")
    exit()