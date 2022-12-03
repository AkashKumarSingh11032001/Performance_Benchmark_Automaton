from pathlib import Path

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




user = input("Do you want to edit any FIO scripts?\n" )
if user == "yes" or user == "y":
    print("")
    for i in range(len(fio)):
        print("{} - {}".format(i,Path(fio[i]).stem))
    
else:
    pass
