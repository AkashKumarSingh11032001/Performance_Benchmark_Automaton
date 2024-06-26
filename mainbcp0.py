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


fio = [
    "fioScripts\\burst_seqwr.txt",
    "fioScripts\\burst_seqrd.txt",
    "fioScripts\\sus_seqwr.txt",
    "fioScripts\\sus_seqrd.txt",
    "fioScripts\\burst_randwr.txt",
    "fioScripts\\burst_randrd.txt",
    "fioScripts\\burst_randwr_oio.txt",
    "fioScripts\\burst_randrd_oio.txt",
]

# <--------- testing-fio script --------->
x = ["C:\\Users\\1000300665\\Desktop\\FVT\\Performance_Benchmark_Automaton\\preCondition\\x.sh"]
y = ["Performance_Benchmark_Automaton\\preCondition\\bpc1.bash"]

server = "10.207.48.142"#"10.207.50.183" #"10.207.48.244"  # "10.207.48.182"
user = "root"
passd = "12"

dirx = "/root/fio/"


def FIOexecution(server, user, passd, dirx, fio):
    
    # <<< DRIVE FORMAT >>>
    driveFormat(server, user, passd, dirx)
    status("FORMAT DONE!", 0.5)

    # <--------- BURST SEQUENTIAL WRITE --------->
    burst_seqwr(server, user, passd, dirx, fio[0])
    status("<--------- BURST SEQUENTIAL WRITE is been implemented! --------->", 1)

    # <--------- BURST SEQUENTIAL READ --------->
    burst_seqrd(server, user, passd, dirx, fio[1])
    status("<--------- BURST SEQUENTIAL READ is been implemented! --------->", 1)

    # # <<< DRIVE FORMAT >>>
    # driveFormat(server, user, passd, dirx)
    # status("FORMAT DONE!", 0.5)

    # <--------- SUSTAINED SEQUENTIAL WRITE --------->
    sus_seqwr(server, user, passd, dirx, fio[2])
    status("<--------- SUSTAINED SEQUENTIAL WRITE is been implemented! --------->", 1)

    # <--------- SUSTAINED SEQUENTIAL READ --------->
    sus_seqrd(server, user, passd, dirx, fio[3])
    status("<--------- SUSTAINED SEQUENTIAL READ is been implemented! --------->", 1)

    # # <<< DRIVE FORMAT >>>
    # driveFormat(server, user, passd, dirx)
    # status("FORMAT DONE!", 0.5)

    # <--------- BURST RANDOM WRITE --------->
    burst_randwr(server, user, passd, dirx, fio[4])
    status("<--------- BURST RANDOM WRITE is been implemented! --------->", 1)

    # <--------- BURST RANDOM READ --------->
    burst_randrd(server, user, passd, dirx, fio[5])
    status("<--------- BURST RANDOM READ is been implemented! --------->", 1)

    # # <<< DRIVE FORMAT >>>
    # driveFormat(server, user, passd, dirx)
    # status("FORMAT DONE!", 0.5)

    # <--------- BURST RANDOM WRITE OIO --------->
    burst_randwr_oio(server, user, passd, dirx, fio[6])
    status("<--------- BURST RANDOM WRITE OIO is been implemented! --------->", 1)

    # <--------- BURST RANDOM READ OIO --------->
    burst_randrd_oio(server, user, passd, dirx, fio[7])
    status("<--------- BURST RANDOM READ OIO is been implemented! --------->", 1)


# ............................. <<< Controler Identify >>>  ............................. #
identifyCtrl(server, user, passd, dirx)
data_a = parseControlerData()  # single list data
status("<--------- Controler Identify Data Structure is been implemented! --------->", 1)

# ............................. <<< FIO SCRIPT EXECUTION >>>.............................
FIOexecution(server, user, passd, dirx, fio)

# ............................. <<< PERFORMANCE ENTRY DATA COLLECTION >>> ............................. #
data_b = performanceEntry()  # list of list data
status("<--------- Performance Entry Data Collection Completed! --------->", 1)

# ............................. <<< SCRIPT ENTRY DATA COLLECTION >>> ............................. #
data_c = infoScriptEntry(fio)  # list of list data
status("<--------- Script Entry Data Completed! --------->", 1)

# ............................. <<< MERGING DATA[A-C] >>> ............................. #
# data_a = [Firmware, capacity]
# data_b = [Iops, Bandwidth, AVg. latecy, 50th-99.9999th ]
# data_c = [Size, Block size, IO-DEPTH, Thread]


final = [data_a, data_b, data_c]
# print(final)
excelPlot(final)
status("<--------- Excel Ready! --------->", 1)


# create a list of cmd to perform in list and pass them one by one int Exection.
# HostsConnectionandCommandExecution(
#     server=server,
#     username=user,
#     password=passd,
#     directoryx=dirx,
#     commandx="sudo su",
# )
# HostsFileTransfer(
#     server=server,
#     username=user,
#     password=passd,
#     localFileNameWithLocation=y[0],
#     remoteFileNameWithLocation="/root/fio/a.txt",  # /home/qa/test/preCondition/bpc0.sh",
# )
# HostsConnectionandCommandExecution(
#     server=server,
#     username=user,
#     password=passd,
#     directoryx=dirx,
#     commandx="chmod -R 777 a.txt",
# )

# x = HostsConnectionandCommandExecution(
#     server=server,
#     username=user,
#     password=passd,
#     directoryx=dirx,
#     commandx="cat a.txt",
# )
# print(x)

# HostsConnectionandCommandExecution(
#     server=server,
#     username=user,
#     password=passd,
#     directoryx=dirx,
#     commandx="( nvme id-ctrl /dev/nvme0 ; nvme list ) >> controlerData.txt",
# )

# HostsFileTransfer(
#     server=server,
#     username=user,
#     password=passd,
#     localFileNameWithLocation="Performance_Benchmark_Automaton/logs/ctrl_res.txt",
#     remoteFileNameWithLocation="/root/fio/controlerData.txt",
#     copyToServer=False,
# )
