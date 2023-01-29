from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from BPC1 import bpc1
from BURST_RAND_WR import burst_randwr
from BURST_RAND_RD import burst_randrd
from BURST_SEQ_WR import burst_seqwr
from BURST_SEQ_RD import burst_seqrd
from BURST_RAND_WR_OIO import burst_randwr_oio
from BURST_RAND_RD_OIO import burst_randrd_oio
from SUS_SEQ_WR import sus_seqwr
from SUS_SEQ_RD import sus_seqrd
from supportFunction import status
from ControlerIdentify import identifyCtrl
from parseControler import parseControlerData
from performance import performanceEntry
from scriptInfo import infoScriptEntry
from formatDrive import driveFormat
from dataOverview import excelPlot
from allLogSaving import logSaving
import os
import shutil
from os.path import dirname
localPath = dirname(__file__)
# print(localPath)



# fio = [
#     "Performance_Benchmark_Automaton\\fioScripts\\burst_seqwr.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\burst_seqrd.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\sus_seqwr.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\sus_seqrd.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\burst_randwr.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\burst_randrd.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\burst_randwr_oio.txt",
#     "Performance_Benchmark_Automaton\\fioScripts\\burst_randrd_oio.txt",
# ]

# # <--------- testing-fio script --------->
# x = ["C:\\Users\\1000300665\\Desktop\\FVT\\Performance_Benchmark_Automaton\\preCondition\\x.sh"]
# y = ["Performance_Benchmark_Automaton\\preCondition\\bpc1.bash"]

# server = "10.207.48.244"#"10.207.48.142"#"10.207.53.94"#"10.207.50.183" #  # "10.207.48.182"
# user = "root"
# passd = "12"

# dirx = "/root/fio/"

# def logSaving(bpc, hmb, firmwareFolder, fileName, copyFrom):
#     # create folder
#     path = "{0}\\results\\{1}".format(localPath, firmwareFolder)
#     # Check whether the specified path exists or not
#     isExist = os.path.exists(path)
#     if not isExist:
#         os.makedirs(path)  # Create a new directory because it does not exist
#         print("The new directory with {0} is created!".format(firmwareFolder))

#     # copy file "original loc" to "target loc"
#     fileName = "{0}_{1}_{2}.log".format(fileName, bpc, hmb)
#     original = copyFrom
#     target = "{0}\\{1}".format(path, fileName)
#     shutil.copy(original, target)


def FIOexecutionBPC1(server, user, passd, dirx, fio, data_a, hmb):
    
    log = [
        "{0}\\logs\\burst_seqwr.log".format(localPath),
        "{0}\\logs\\burst_seqrd.log".format(localPath),
        "{0}\\logs\\sus_seqwr.log".format(localPath),
        "{0}\\logs\\sus_seqrd.log".format(localPath),
        "{0}\\logs\\burst_randwr.log".format(localPath),
        "{0}\\logs\\burst_randrd.log".format(localPath),
        "{0}\\logs\\burst_randwr_oio.log".format(localPath),
        "{0}\\logs\\burst_randrd_oio.log".format(localPath),
    ]

    
    # <------------------> BPC1 ------------------>
    bpc_1 = "{0}\\preCondition\\bpc1.txt".format(localPath)
    bpc1(server, user, passd, dirx, bpc_1)
    status("<--------- Precondition BPC1 is been implemented! --------->", 1)

    # <--------- BURST SEQUENTIAL WRITE --------->
    burst_seqwr(server, user, passd, dirx, fio[0])
    status("<--------- BURST SEQUENTIAL WRITE is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "burst_seqwr", log[0])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- BURST SEQUENTIAL READ --------->
    burst_seqrd(server, user, passd, dirx, fio[1])
    status("<--------- BURST SEQUENTIAL READ is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "burst_seqrd", log[1])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- SUSTAINED SEQUENTIAL WRITE --------->
    sus_seqwr(server, user, passd, dirx, fio[2])
    status("<--------- SUSTAINED SEQUENTIAL WRITE is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "sus_seqwr", log[2])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- SUSTAINED SEQUENTIAL READ --------->
    sus_seqrd(server, user, passd, dirx, fio[3])
    status("<--------- SUSTAINED SEQUENTIAL READ is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "sus_seqrd", log[3])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- BURST RANDOM WRITE --------->
    burst_randwr(server, user, passd, dirx, fio[4])
    status("<--------- BURST RANDOM WRITE is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "burst_randwr", log[4])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- BURST RANDOM READ --------->
    burst_randrd(server, user, passd, dirx, fio[5])
    status("<--------- BURST RANDOM READ is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "burst_randrd", log[5])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- BURST RANDOM WRITE OIO --------->
    burst_randwr_oio(server, user, passd, dirx, fio[6])
    status("<--------- BURST RANDOM WRITE OIO is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "burst_randwr_oio", log[6])
    status("<--------- LOG SAVED!!! --------->", 1)

    # <--------- BURST RANDOM READ OIO --------->
    burst_randrd_oio(server, user, passd, dirx, fio[7])
    status("<--------- BURST RANDOM READ OIO is been implemented! --------->", 1)
    logSaving("BPC1", hmb, data_a, "burst_randrd_oio", log[7])
    status("<--------- LOG SAVED!!! --------->", 1)


def ExeBPC1(Userserver,hmb):

    server = Userserver
    user = "root"
    passd = "12"

    dirx = "/root/fio/"
    # localPath = dirname(__file__)
    # print(localPath)
    
    
    
    # print("{}\\burst.txt".format(x))
    
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

    # <--------- testing-fio script --------->
    x = ["{0}\\preCondition\\x.sh".format(localPath)]
    y = ["{0}\\preCondition\\bpc1.bash".format(localPath)]
    
    # ............................. <<< Controler Identify >>>  ............................. #
    identifyCtrl(server, user, passd, dirx)
    data_a = parseControlerData()  # single list data
    status("<--------- Controler Identify Data Structure is been implemented! --------->", 1)

    # ............................. <<< FIO SCRIPT EXECUTION >>>.............................
    FIOexecutionBPC1(server, user, passd, dirx, fio, data_a, hmb)

    # ............................. <<< PERFORMANCE ENTRY DATA COLLECTION >>> ............................. #
    data_b = performanceEntry()  # list of list data
    status("<--------- Performance Entry Data Collection Completed! --------->", 1)

    # ............................. <<< SCRIPT ENTRY DATA COLLECTION >>> ............................. #
    data_c = infoScriptEntry(fio)  # list of list data
    status("<--------- Script Entry Data Completed! --------->", 1)


    final = [data_a, data_b, data_c]
    # print(final)
    excelPlot(final,"BPC1",hmb)
    status("<--------- Excel Ready! --------->", 1)

# ExeBPC1("10.207.48.244","HMBON")

