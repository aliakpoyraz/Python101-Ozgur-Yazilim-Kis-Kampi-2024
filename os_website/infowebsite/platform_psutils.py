import platform
import psutil



def platformsOutputs():
    outputs = [platform.system(), # ilk satir sistem
         platform.version(), # bu satır ubuntunun versionunu
         platform.architecture(), #  tuple türünde bit verisyonu
         ]

    return outputs


def aboutCpus():
    return psutil.cpu_count(logical=True), # toplam islemci sayisi
            


def aboutNetwork():
    return psutil.net_if_addrs() # network kartı bilgilerini  veririr.

print(platformsOutputs(),"\n", aboutCpus(), "\n", aboutNetwork())
    