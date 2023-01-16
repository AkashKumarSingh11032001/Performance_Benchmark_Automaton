from supportFunction_performance import removeExtraSpace
from supportFunction_performance import stringToList
from os.path import dirname


def parseControlerData():
    
    localPath= dirname(__file__)

    file = ["{0}\\logs\\ctrl_res.txt".format(localPath)]   

    mylines = []
    with open(file[0]) as fp:
        for x in fp:
            mylines.append(removeExtraSpace(x))
 
    mylines = stringToList(mylines[2], " ") 
    # print(mylines)
    capacity = mylines[4] + " " + mylines[5] 
    firmware = mylines[-2]  

    # print("Firmware Rev. : ".format(firmware))
    # print("Capacity : ".format(capacity))   

    proData_2 = [firmware, capacity]
    
    return proData_2


# data_2 = parseControlerData()
# print(data_2)


