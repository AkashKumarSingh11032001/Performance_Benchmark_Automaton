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
from os.path import dirname


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


def FIOexecutionBPC1(server, user, passd, dirx, fio):
    
    localPath= dirname(__file__)
    
    # <------------------> BPC1 ------------------>
    bpc_1 = "{0}\\preCondition\\bpc1.txt".format(localPath)
    bpc1(server, user, passd, dirx, bpc_1)
    status("<--------- Precondition BPC1 is been implemented! --------->", 1)

    # <--------- BURST SEQUENTIAL WRITE --------->
    burst_seqwr(server, user, passd, dirx, fio[0])
    status("<--------- BURST SEQUENTIAL WRITE is been implemented! --------->", 1)

    # <--------- BURST SEQUENTIAL READ --------->
    burst_seqrd(server, user, passd, dirx, fio[1])
    status("<--------- BURST SEQUENTIAL READ is been implemented! --------->", 1)

    # <--------- SUSTAINED SEQUENTIAL WRITE --------->
    sus_seqwr(server, user, passd, dirx, fio[2])
    status("<--------- SUSTAINED SEQUENTIAL WRITE is been implemented! --------->", 1)

    # <--------- SUSTAINED SEQUENTIAL READ --------->
    sus_seqrd(server, user, passd, dirx, fio[3])
    status("<--------- SUSTAINED SEQUENTIAL READ is been implemented! --------->", 1)

    # <--------- BURST RANDOM WRITE --------->
    burst_randwr(server, user, passd, dirx, fio[4])
    status("<--------- BURST RANDOM WRITE is been implemented! --------->", 1)

    # <--------- BURST RANDOM READ --------->
    burst_randrd(server, user, passd, dirx, fio[5])
    status("<--------- BURST RANDOM READ is been implemented! --------->", 1)


    # <--------- BURST RANDOM WRITE OIO --------->
    burst_randwr_oio(server, user, passd, dirx, fio[6])
    status("<--------- BURST RANDOM WRITE OIO is been implemented! --------->", 1)

    # <--------- BURST RANDOM READ OIO --------->
    burst_randrd_oio(server, user, passd, dirx, fio[7])
    status("<--------- BURST RANDOM READ OIO is been implemented! --------->", 1)


def ExeBPC1(Userserver):

    server = Userserver
    user = "root"
    passd = "12"

    dirx = "/root/fio/"
    
    localPath= dirname(__file__)
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
    # FIOexecutionBPC1(server, user, passd, dirx, fio)

    # ............................. <<< PERFORMANCE ENTRY DATA COLLECTION >>> ............................. #
    data_b = performanceEntry()  # list of list data
    status("<--------- Performance Entry Data Collection Completed! --------->", 1)

    # ............................. <<< SCRIPT ENTRY DATA COLLECTION >>> ............................. #
    data_c = infoScriptEntry(fio)  # list of list data
    status("<--------- Script Entry Data Completed! --------->", 1)


    final = [data_a, data_b, data_c]
    # print(final)
    excelPlot(final,"BPC1")
    status("<--------- Excel Ready! --------->", 1)

# ExeBPC1("10.207.48.244")

