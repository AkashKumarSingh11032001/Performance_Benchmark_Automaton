from pathlib import Path
from edit_fio_Scripts import ScriptFIO
import ast
import json

def twoListToDictionary(test_keys,test_values):
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

test[0][len(test[0])-1] = test[0][len(test[0])-1][:-1]
# print(test[0])
key = test[0]
value = test[1:]

user = input("\nDo you want to edit any FIO scripts? " )
if user == "yes" or user == "y":
    print("")
    for i in range(len(fio)):
        print("{} - {}".format(i,Path(fio[i]).stem))
    indx = int(input("\nSelect File you want to edit. " ))
    print("\nDefault File content of {0} \n".format(Path(fio[indx]).stem))
    res_dict = twoListToDictionary(key, value[indx])
    print("PARAMETER - DEFAULT VALUE\n")
    for i in res_dict:
        print(i," - ", res_dict[i])
else:
    pass
