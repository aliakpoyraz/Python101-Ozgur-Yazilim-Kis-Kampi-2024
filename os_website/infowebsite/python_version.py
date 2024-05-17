import sys

def version():
    versionInfoMajor = sys.version_info.major
    versionInfoMinor = sys.version_info.minor
    versionInfoMicro = sys.version_info.micro

    version_list = [versionInfoMajor, versionInfoMinor, versionInfoMicro]
    
    return version_list


