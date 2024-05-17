
def cpuinfo():
    with open("/proc/cpuinfo","r") as procCpuInfo:
        theOuput = procCpuInfo.read()

    splitList = theOuput.split("\n\n")[-2:-1]
    lastSplitlist = splitList[0].split("\n")
    lastSplitlist = lastSplitlist[0]
    lastSplitlist = lastSplitlist.split(":")
    lastSplitlist = str(lastSplitlist[1])
    lastSplitlist = int(lastSplitlist.strip())
    print(lastSplitlist)
    return lastSplitlist + 1


def os_release():
    with open("/etc/os-release", "r") as osr:
        theList = osr.readlines()
    os_s_names = []
    print(type(theList))
    for i in theList:
        if i.startswith("PRETTY_NAME"):
            prettyNameSplited = i.split("=")
            print(prettyNameSplited)
            prettyNameresult = prettyNameSplited[1].strip()


        if i.startswith("NAME"):
            nameSplit = i.split("=")
            nameResult = nameSplit[1]
        if i.startswith("VERSION"):
            versionSplitted = i.split("=")
            versionResult = versionSplitted[1].strip()


        

def meminfo():
    # /proc/meminfo
    with open("/proc/meminfo", "r") as memInfo:
        theInfo=memInfo.readline()
    
        if theInfo.startswith("MemTotal"):
            memInfoSplited = theInfo.split(":")
            memInfoResult=memInfoSplited[1].strip()

        forShowGb = memInfoResult.split(" ")
        MemSizeValue = forShowGb[0]
        MemSizeValue =round(int(MemSizeValue) / 1024 /1024, 2) 
        showAllGbInfo = "%s Gb" % MemSizeValue
    print(memInfoResult, showAllGbInfo)

        
    #print(prettyNameresult, nameResult,versionResult,memInfoResult)


os_release()
cpuinfo()
meminfo()