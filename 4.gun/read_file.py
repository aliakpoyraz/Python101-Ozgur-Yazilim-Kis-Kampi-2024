
def read_file():
    with open("/home/pi/Desktop/os_website/infos", "r") as myfile:
        inside = myfile.readlines()

    return inside


myspecsfile = read_file()
print(type(myspecsfile))
print(myspecsfile)
