import csv
import math
import re
import numpy as np
from supportFunction_performance import *
from csv import DictWriter
from os.path import dirname

localPath= dirname(__file__)


def listToCSV(lis):
    csv_file = "performance.csv"

    field_names = [
        "LEVEL",
        "IOPS(K)",
        "BW(MB/s)",
        "Avg.Lat(usec)",
        "50.0000th",
        "75.0000th",
        "99.0000th",
        "99.9000th",
        "99.9900th",
        "99.9990th",
        "99.9999th",
    ]

    dict = {
        "LEVEL": "PF",
        "IOPS(K)": lis[0],
        "BW(MB/s)": lis[1],
        "Avg.Lat(usec)": lis[2],
        "50.0000th": lis[3],
        "75.0000th": lis[4],
        "99.0000th": lis[5],
        "99.9000th": lis[6],
        "99.9900th": lis[7],
        "99.9990th": lis[8],
        "99.9999th": lis[9],
    }

    with open(csv_file, "a") as file:

        dictwriter_object = DictWriter(file, fieldnames=field_names)

        dictwriter_object.writerow(dict)

        file.close()


def iterFile(mylines, fileLoc):
    
    no_of_jobs_files = 1

    for indx in range(len(mylines)):
        if "job1: (groupid=0, jobs=1)" in mylines[indx]:
            index = indx + 1

    percentile_res = []
    iops_res = []
    for i in range(no_of_jobs_files):
        reqIndex = []
        iops_list = []
        lat_list = []

        reqIndex.append(mylines[index + 5 + (i * 19)])
        reqIndex.append(mylines[index + 6 + (i * 19)])
        reqIndex.append(mylines[index + 7 + (i * 19)])
        iops_list.append(mylines[index + (i * 19)])
        lat_list.append(mylines[index + 2 + (i * 19)])

        percentile = ratios_Ratio(reqIndex)
        iops = ratios_IOPS(iops_list)
        latency = ratios_Lat(lat_list)

        rows = len(percentile)
        cols = len(percentile[0])
        n = 7

        if "usec" in mylines[index + 4]:
            for i in range(n):
                percentile_res.append(percentile[rows - 1][i])
        else:
            for i in range(n):
                percentile_res.append((percentile[rows - 1][i]) / 1000)

        percentile_res = np.reshape(percentile_res, (-1, 7))

        if "k" not in iops[0]:
            iops[0] = str(int(iops[0]) / 1000)
        else:
            iops[0] = iops[0].rstrip(iops[0][-1])

        iops_res.append(iops[0])
        string = "".join(iops)
        start = string.find("(")
        end = string.find(")")
        iops_res.append(string[start + 1: end])

        ls = [eval(ele) for ele in iops_res]
        if "usec" in mylines[index + 2]:
            ls.append(latency[2])
        else:
            ls.append(float(latency[2]) / 1000)

        ls = np.reshape(ls, (-1, 3))

    percentile_resx = [item for i in percentile_res for item in i]
    ls = [item for i in ls for item in i]

    return percentile_resx, ls


def performanceEntry():
    files = [
        "{0}\\logs\\burst_seqwr.log".format(localPath),
        "{0}\\logs\\burst_seqrd.log".format(localPath),
        "{0}\\logs\\sus_seqwr.log".format(localPath),
        "{0}\\logs\\sus_seqrd.log".format(localPath),
        "{0}\\logs\\burst_randwr.log".format(localPath),
        "{0}\\logs\\burst_randrd.log".format(localPath),
        "{0}\\logs\\burst_randwr_oio.log".format(localPath),
        "{0}\\logs\\burst_randrd_oio.log".format(localPath),
    ]
    xt = "{0}\\logs\\burst_seqrd.log".format(localPath)
    
    points_ratio = []
    points_ls = []
    res = []
    for j in range(len(files)):
        mylines = []
        with open(files[j]) as fp:
            for x in fp:
                mylines.append(x)

        percentile_res, ls = iterFile(mylines, files[j])

        points_ratio.append(
            percentile_res
        )  # [[338.0, 367.0, 515.0, 603.0, 848.0, 922.0, 979.0], [90.0, 91.0, 93.0, 102.0, 212.0, 449.0, 3523.0]]
        points_ls.append(
            ls
        )  # [['23.8', '3119', ' 332.60'], ['12.2', '50.1', ' 80.17']]

    res = points_ratio + points_ls

    iterLen_list_1 = 0
    iterLen_list_2 = len(points_ratio)

    proData_1 = []
    while iterLen_list_2 < (len(points_ratio) * 2):
        Final = res[iterLen_list_2] + res[iterLen_list_1]
        Final = [float(i) for i in Final]
        iterLen_list_2 += 1
        iterLen_list_1 += 1
        proData_1.append(Final)
        # listToCSV(Final)
    
    # print(proData_1, "\n")
    return proData_1


# data_1 = performanceEntry()
# print(data_1)
