[global]
thread
ioengine=libaio
direct=1
size=100%
rw=read
numjobs=1
bs=128KB
iodepth=8
threads=1
randrepeat=0
lat_percentiles=1
percentile_list=50:75:99:99.9:99.99:99.999:99.9999

[job1]
filename=/dev/nvme0n1