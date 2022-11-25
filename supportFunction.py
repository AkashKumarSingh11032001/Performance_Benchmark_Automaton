import os
from datetime import date
import binascii
import time


def stringRepToZero(str):
    return str.replace(str, "0"*32)


def todaysDate():
    today = date.today()
    return "{:02d}{:02d}".format(today.month, today.day)


def stringToHex(str):
    s = ''
    for c in str:
        s += hex(ord(c)).replace('0x', '')
    return s


def HexToAscii(str):
    return bytearray.fromhex(str).decode()


def serialUpdate(str, level):
    newSerial = "{1}{0}".format(str, level)
    return newSerial[:]


def updateDriveCap(cap):
    str = "WDSSDATPCM"
    newDriveCap = "{0}{1}".format(str, cap)
    return newDriveCap[:]


def updateFirmware(firmware, date):
    newFirmware = "{0}{1}".format(firmware, date)
    return newFirmware[:]


def updateModel(serial):
    str = "nqn.2018-01.com.wdc:guid:E8238FA6BF53-0001-001B44"
    newModel = "{0}{1}".format(str, serial)
    return newModel[:]


def hexToBytes(hex):
    x = str(hex)
    x = x.replace("\\x", '')
    x = str.encode(x[0:len(x)])
    return x


def pathConvertion(path):
    supportedPath = path.replace("\\", "\\\\")
    return supportedPath


def status(str, times):
    print(str)
    time.sleep(times)
    return


def checkString(str):

    count_alpha = 0
    count_digit = 0

    for i in str:

        # if string has letter
        if i.isalpha():
            count_alpha = count_alpha + 1

        # if string has number
        if i.isdigit():
            count_digit = count_digit + 1

    return count_alpha,count_digit
