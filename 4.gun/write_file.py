#import json

def write_file(file_dir,data):

    with open(f"{file_dir}", "w+") as mywrittenfile:
        mywrittenfile.write(data)

write_file(file_dir="/home/pi/Desktop/os_website/infos",data="hello worlds!")