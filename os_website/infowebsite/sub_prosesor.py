#Bir komutun çıktıları nasıl alınır nasıl gösterilir
#OS kütüphanesinden sistem verilerini nasıl alabilirim

import subprocess
import os

def lsblk():
    lsblk_output= subprocess.getoutput("lsblk")
    lines = lsblk_output.split('\n')
    for line in lines:
        columns = line.split()
        if len(columns) > 4 and "disk" in columns[5]:
            gigabyteSize = columns[3].strip()

    return gigabyteSize
#print("CPU Sonuçları:\n", subprocess.getoutput("lscpu"))

def lscpu():
    lscpu_output=subprocess.getoutput("lscpu")
    lscpuSplited=lscpu_output.split("\n")
    for i in lscpuSplited:
        print(i)
        if i.startswith("Model name:"):
            lsCpuResult = i.split(":")
            #lsCpuResult = lsCpuResult
            lscpuValue = lsCpuResult[1].strip()
            #print("CPU Sonuçları:\n", lscpuValue)
    return lscpuValue

