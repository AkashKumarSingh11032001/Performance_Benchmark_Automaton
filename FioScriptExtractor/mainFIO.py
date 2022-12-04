from pathlib import Path
from edit_fio_Scripts import ScriptFIO
import ast
import json


def twoListToDictionary(test_keys, test_values):
    res = dict(zip(test_keys, test_values))
    return res


def mergeDict(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def dictToFIOFile(dictonary,file):
    pass
    
    


fio_default = [
    "FioScriptExtractor\\fio_default\\burst_seqwr.txt",
    "FioScriptExtractor\\fio_default\\burst_seqrd.txt",
    "FioScriptExtractor\\fio_default\\sus_seqwr.txt",
    "FioScriptExtractor\\fio_default\\sus_seqrd.txt",
    "FioScriptExtractor\\fio_default\\burst_randwr.txt",
    "FioScriptExtractor\\fio_default\\burst_randrd.txt",
    "FioScriptExtractor\\fio_default\\burst_randwr_oio.txt",
    "FioScriptExtractor\\fio_default\\burst_randrd_oio.txt",
]

fio_updated = [
    "FioScriptExtractor\\fio_updated\\burst_seqwr.txt",
    "FioScriptExtractor\\fio_updated\\burst_seqrd.txt",
    "FioScriptExtractor\\fio_updated\\sus_seqwr.txt",
    "FioScriptExtractor\\fio_updated\\sus_seqrd.txt",
    "FioScriptExtractor\\fio_updated\\burst_randwr.txt",
    "FioScriptExtractor\\fio_updated\\burst_randrd.txt",
    "FioScriptExtractor\\fio_updated\\burst_randwr_oio.txt",
    "FioScriptExtractor\\fio_updated\\burst_randrd_oio.txt",
]


ScriptFIO()

sc_data_loc = "FioScriptExtractor\\Scriptdata.txt"
with open(sc_data_loc, 'r') as f:
    ScriptData = f.readlines()


test = []
for s in ScriptData:
    l = s.split(",")
    test.append(l)

test[0][len(test[0])-1] = test[0][len(test[0]) - 1][:-1]  # removing \n from first line
# print(test[0])
key = test[0]
value = test[1:]

keep = True
while keep:
    user = input("\nDo you want to edit any fio scripts? ")
    if user == "yes" or user == "y":
        print("")

        for i in range(len(fio_updated)):
            # list fio_updated name to be edit
            print("{} - {}".format(i, Path(fio_updated[i]).stem))

        indx = int(input("\nSelect File you want to edit. "))
        print("\nDefault File content of {0} \n".format(
            Path(fio_updated[indx]).stem))

        res_dict = twoListToDictionary(key, value[indx])
        # print(res_dict)
        print("PARAMETER - DEFAULT VALUE\n")
        for i in res_dict:
            print(i, " - ", res_dict[i])

        edit_para = input(
            "Please enter the PARAMETER (seprated by space, if multiple parameters to be edited). ")
        if len(edit_para) == 1:
            par = edit_para
        else:
            par = edit_para.split(" ")

        print("\nSelected PARAMETER to be edited are {0}\n".format(par))

        for i in par:
            if i not in res_dict:
                print("Invalid PARAMETER! Please Verify again.")
                exit()
            else:
                inp_par = input("Please enter new {0} value = ".format(i))
                res_dict[i] = inp_par

        print("\nUpdated fio_updated Script : \n")
        print("PARAMETER - UPDATED VALUE\n")
        for i in res_dict:
            print(i, " - ", res_dict[i])

        d1 = {"[global]": "", "thread": ""}
        d2 = mergeDict(d1, res_dict)
        last_d = d2.popitem()
        d3 = {last_d[0]: last_d[1]}
        d4 = {"": "", "[job1]": ""}
        d5 = mergeDict(d2, d4)
        final_dict = mergeDict(d5, d3)
        print(final_dict)
        dictToFIOFile(final_dict,fio_updated[indx])

    else:
        keep = False
