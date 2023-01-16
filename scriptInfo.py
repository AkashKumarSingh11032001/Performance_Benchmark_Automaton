import xlsxwriter
import re
from supportFunction_performance import removeExtraSpace
from supportFunction_performance import stringToList
from supportFunction import pickNum
from os.path import dirname

localPath= dirname(__file__)

fio = [
    "{0}\\fioScripts\\burst_seqwr.txt".format(localPath),
    "{0}\\fioScripts\\burst_seqrd.txt".format(localPath),
    "{0}\\fioScripts\\sus_seqwr.txt".format(localPath),
    "{0}\\fioScripts\\sus_seqrd.txt".format(localPath),
    "{0}\\fioScripts\\burst_randwr.txt".format(localPath),
    "{0}\\fioScripts\\burst_randrd.txt".format(localPath),
    "{0}\\fioScripts\\burst_randwr_oio.txt".format(localPath),
    "{0}\\fioScripts\\burst_randrd_oio.txt".format(localPath),
    ]

def element(pattern,mylines):
    res = []
    for word in mylines:
        if re.search(pattern[0], word):
            res.append(word)
        elif re.search(pattern[1], word):
            res.append(word)
        elif re.search(pattern[2], word):
            res.append(word)
        elif re.search(pattern[3], word):
            res.append(word)
            
    return res

def infoScriptEntry(fio):

    file = fio  

    pattern_1 = re.compile(r'^bs=')
    pattern_2 = re.compile(r'^iodepth=')
    pattern_3 = re.compile(r'^threads=')
    pattern_4 = re.compile(r'^size=')
    pattern = [pattern_1, pattern_2, pattern_3, pattern_4]  
    
    proData_3 = []
    
    for i in range(len(file)):
        mylines = []
        with open(file[i]) as fp:
            for x in fp:
                mylines.append(x)
        if file[i] in ["{0}\\fioScripts\\burst_randwr.txt".format(localPath),"{0}\\fioScripts\\burst_randrd.txt".format(localPath)]:
            res = element(pattern,mylines)
            size = pickNum(res[0][:-1])
            block = pickNum(res[1][-6:-1])+"KB"
            iodepth = res[2][-3:-1]
            threads = res[3][-3:-1] 

            info = [size,block,iodepth,threads]
            proData_3.append(info)
        else:
            res = element(pattern,mylines)
            size = pickNum(res[0][:-1])
            block = pickNum(res[1][-6:-1])+"KB"
            iodepth = res[2][-2:-1]
            threads = res[3][-2:-1] 

            info = [size,block,iodepth,threads]
            proData_3.append(info)
        
    for i in range(len(proData_3)):
        if (i == 2) or (i == 3):
            proData_3[i][0] = proData_3[i][0] + "%"
        else:
            proData_3[i][0] = proData_3[i][0] + "GB"
    
    return proData_3


# x = infoScriptEntry(fio)
# print(x)
        
# print([ele for ele in mylines if "bs=" in ele])
        
# mylines = stringToList(mylines[2], " ")