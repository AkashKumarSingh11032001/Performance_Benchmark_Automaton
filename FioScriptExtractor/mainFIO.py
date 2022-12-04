from pathlib import Path
from edit_fio_Scripts import ScriptFIO
import ast
import json


def twoListToDictionary(test_keys, test_values):
    res = dict(zip(test_keys, test_values))
    return res


fio = [
    "FioScriptExtractor\\fioS\\burst_seqwr.txt",
    "FioScriptExtractor\\fioS\\burst_seqrd.txt",
    "FioScriptExtractor\\fioS\\sus_seqwr.txt",
    "FioScriptExtractor\\fioS\\sus_seqrd.txt",
    "FioScriptExtractor\\fioS\\burst_randwr.txt",
    "FioScriptExtractor\\fioS\\burst_randrd.txt",
    "FioScriptExtractor\\fioS\\burst_randwr_oio.txt",
    "FioScriptExtractor\\fioS\\burst_randrd_oio.txt",
]


ScriptFIO()

sc_data_loc = "FioScriptExtractor\\Scriptdata.txt"
with open(sc_data_loc, 'r') as f:
    ScriptData = f.readlines()


test = []
for s in ScriptData:
    l = s.split(",")
    test.append(l)

test[0][len(test[0])-1] = test[0][len(test[0]) -
                                  1][:-1]  # removing \n from first line
# print(test[0])
key = test[0]
value = test[1:]

user = input("\nDo you want to edit any FIO scripts? ")
if user == "yes" or user == "y":
    print("")

    for i in range(len(fio)):
        # list fio name to be edit
        print("{} - {}".format(i, Path(fio[i]).stem))

    indx = int(input("\nSelect File you want to edit. "))
    print("\nDefault File content of {0} \n".format(Path(fio[indx]).stem))

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

    print("\nUpdated FIO Script : \n")
    for i in res_dict:
        print(i, " - ", res_dict[i])
else:
    pass
