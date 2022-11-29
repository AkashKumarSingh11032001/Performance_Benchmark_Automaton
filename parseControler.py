import xlsxwriter
from supportFunction_performance import removeExtraSpace
from supportFunction_performance import stringToList

def parseControlerData():

    file = ["logs\\ctrl_res.txt"]   

    mylines = []
    with open(file[0]) as fp:
        for x in fp:
            mylines.append(removeExtraSpace(x))

    mylines = stringToList(mylines[2], " ") 

    capacity = mylines[5] + " " + mylines[6]
    firmware = mylines[-2]  

    print("Firmware Rev. : ".format(firmware))
    print("Capacity : ".format(capacity))   

    proData_2 = [firmware, capacity]
    
    return proData_2


data_2 = parseControlerData()
print(data_2)


# workbook = xlsxwriter.Workbook('write_data.xlsx')
# worksheet = workbook.add_worksheet()

# worksheet.write(0, 0, "Standard Device Config.")
# worksheet.write(1, 0, "Firware Rev.")  
# worksheet.write(2, 0, "Drive Capacity")
# worksheet.write(1, 1, firmware)
# worksheet.write(2, 1, capacity)
# workbook.close()