from conectionBetweenTwoHost import HostsConnectionandCommandExecution
from conectionBetweenTwoHost import HostsFileTransfer
from BPC1 import bpc1



fio = [
    "Performance_Benchmark_Automaton\\preCondition\\bpc1.bash"
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randrd_oio.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randrd.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randwr_oio.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_randwr.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_seqrd.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\burst_seqwr.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\sus_seqrd.sh",
    "Performance_Benchmark_Automaton\\fioScripts\\sus_seqwr.sh",
]

# <--------- test-fio script --------->
x = ["C:\\Users\\1000300665\\Desktop\\FVT\\Performance_Benchmark_Automaton\\preCondition\\x.sh"]
y = ["Performance_Benchmark_Automaton\\preCondition\\bpc1.bash"]

server = "10.207.48.244"  # "10.207.48.182"
user = "root"
passd = "12"

dirx = "/root/test/"

# <------------------> BPC1 ------------------>
bpc1(server, user, passd, dirx, y[0])
# # <--------- BURST SEQUENTIAL WRITE --------->
# burst_seqwr(server, user, passd, dirx, y[0])
# # <--------- BURST SEQUENTIAL READ --------->
# burst_seqrd(server, user, passd, dirx, y[0])
# # <--------- BURST RANDOM WRITE --------->
# burst_randwr(server, user, passd, dirx, y[0])
# # <--------- BURST RANDOM READ --------->
# burst_randrd(server, user, passd, dirx, y[0])
# # <--------- SUSTAINED SEQUENTIAL WRITE --------->
# sus_seqwr(server, user, passd, dirx, y[0])
# # <--------- SUSTAINED SEQUENTIAL READ --------->
# sus_seqrd(server, user, passd, dirx, y[0])
# # <--------- BURST RANDOM WRITE OIO --------->
# burst_randwr_oio(server, user, passd, dirx, y[0])
# # <--------- BURST RANDOM READ OIO --------->
# burst_randrd_oio(server, user, passd, dirx, y[0])

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
