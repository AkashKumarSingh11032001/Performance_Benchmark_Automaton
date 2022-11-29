import csv
import math
import re
import os


def removeExtraSpace(s):
    s = re.sub(" +", " ", s)
    return s


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def stringToList(s, deli):
    li = list(s.split(deli))
    return li


def removeUnwantercharater(s):
    removeChar = "?:!/;|\n'th'[]"
    s = "".join(c for c in s if c not in removeChar)
    return s


def removeExtraSpace(s):
    s = re.sub(" +", " ", s)
    return s


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def stringToList(s, deli):
    li = list(s.split(deli))
    return li


# <------------- RATIO -------------------->
def removeUnwantercharater_IOPS(s):
    removeChar = "=?:!;[]|\n'write''IOPS''MB/s''read'"
    s = "".join(c for c in s if c not in removeChar)
    return s


res = []


def ratios_IOPS(reqIndex):
    s = listToString(reqIndex)
    s = removeUnwantercharater_IOPS(s)
    s = removeExtraSpace(s)

    s = stringToList(s, ",")

    mainList = []
    for i in s:
        a = stringToList(i, "=")
        mainList = mainList + a
    print()

    newList = []
    for i in mainList:
        newList.append(removeUnwantercharater_IOPS(i))

    return newList


# <------------- Latency -------------------->
def removeUnwantercharater_Lat(s):
    removeChar = "=?:!;[]|\n()'clat''usec''min''max''avg''stdev'"
    s = "".join(c for c in s if c not in removeChar)
    return s


res = []


def ratios_Lat(reqIndex):
    s = listToString(reqIndex)
    s = removeUnwantercharater_Lat(s)
    s = removeExtraSpace(s)

    s = stringToList(s, ",")

    mainList = []
    for i in s:
        a = stringToList(i, "=")
        mainList = mainList + a

    newList = []
    for i in mainList:
        newList.append(removeUnwantercharater_Lat(i))

    return newList


# <------------- RATIO -------------------->
def removeUnwantercharater_Ratio(s):
    removeChar = "?:!/;[]|\n'th'"
    s = "".join(c for c in s if c not in removeChar)
    return s


res = []


def ratios_Ratio(reqIndex):
    s = listToString(reqIndex)
    s = removeUnwantercharater_Ratio(s)
    s = removeExtraSpace(s)
    # print(s)

    s = stringToList(s, ",")
    # print(s)
    mainList = []
    for i in s:
        a = stringToList(i, "=")
        mainList = mainList + a

    newList = []
    for i in mainList:
        newList.append(float(removeUnwantercharater_Ratio(i)))

    a = newList[::2]
    b = newList[1::2]
    res.append(b)
    return res


def delLines(file):
    with open(file, "r") as fin:
        data = fin.read().splitlines(True)
    with open(file, "w") as fout:
        fout.writelines(data[1:])


def prepend_line(file_name, line):
    dummy_file = file_name + ".bak"  # define name of temporary dummy file
    with open(file_name, "r") as read_obj, open(
        dummy_file, "w"
    ) as write_obj:  # open original file in read mode and dummy file in write mode
        write_obj.write(line + "\n")
        for (
            line
        ) in (
            read_obj
        ):  # Read lines from original file one by one and append them to the dummy file
            write_obj.write(line)

    os.remove(file_name)  # remove original file
    os.rename(dummy_file, file_name)  # rename dub file
