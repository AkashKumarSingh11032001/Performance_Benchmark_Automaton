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


fio = [
    "Performance_Benchmark_Automaton\\preCondition\\bpc1.bash"
    "Performance_Benchmark_Automaton\\fioScripts\\burst_seqwr.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_seqrd.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randwr.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randrd.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\sus_seqwr.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\sus_seqrd.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randwr_oio.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randrd_oio.sh",
]

# <--------- testing-fio script --------->
x = ["C:\\Users\\1000300665\\Desktop\\FVT\\Performance_Benchmark_Automaton\\preCondition\\x.sh"]
y = ["Performance_Benchmark_Automaton\\preCondition\\bpc1.bash"]

server = "10.207.48.244"  # "10.207.48.182"
user = "root"
passd = "12"

dirx = "/root/fio/"

# <------------------> BPC1 ------------------>
bpc1(server, user, passd, dirx, fio[0])
# <--------- BURST SEQUENTIAL WRITE --------->
burst_seqwr(server, user, passd, dirx, fio[1])
# <--------- BURST SEQUENTIAL READ --------->
burst_seqrd(server, user, passd, dirx, fio[2])
# <--------- BURST RANDOM WRITE --------->
burst_randwr(server, user, passd, dirx, fio[3])
# <--------- BURST RANDOM READ --------->
burst_randrd(server, user, passd, dirx, fio[4])
# <--------- SUSTAINED SEQUENTIAL WRITE --------->
sus_seqwr(server, user, passd, dirx, fio[5])
# <--------- SUSTAINED SEQUENTIAL READ --------->
sus_seqrd(server, user, passd, dirx, fio[6])
# <--------- BURST RANDOM WRITE OIO --------->
burst_randwr_oio(server, user, passd, dirx, fio[7])
# <--------- BURST RANDOM READ OIO --------->
burst_randrd_oio(server, user, passd, dirx, fio[8])

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
#     remoteFileNameWithLocation="/root/test/a.txt",  # /home/qa/test/preCondition/bpc0.sh",
# )
# HostsConnectionandCommandExecution(
#     server=server,
#     username=user,
#     password=passd,
#     directoryx=dirx,
#     commandx="chmod -R 777 a.txt",
# )

# # x = HostsConnectionandCommandExecution(
# #     server=server,
# #     username=user,
# #     password=passd,
# #     directoryx=dirx,
# #     commandx="cat a.txt",
# # )
# # print(x)

# HostsConnectionandCommandExecution(
#     server=server,
#     username=user,
#     password=passd,
#     directoryx=dirx,
#     commandx="fio a.txt --eta-newline=1 --eta=always | tee res.log",
# )

# HostsFileTransfer(
#     server=server,
#     username=user,
#     password=passd,
#     localFileNameWithLocation="Performance_Benchmark_Automaton/logs/res.log",
#     remoteFileNameWithLocation="/root/test/res.log",
#     copyToServer=False,
# )
