import os

def vali(tagid):
    id=[]
    if(tagid=="2400352DD4E8"):
        id=["Harsh","B","70331019003"]
    elif(tagid=="5800C9D9F5BD"):
        id=["Rachit","S","70331019040"]
    elif(tagid=="5800C9DC6429"):
        id=["Abhishek","G","70331019007"]
    else:
        id=[]
        

    return id


# while(True):
#     test=str(os.popen("sudo head -c 12 /dev/ttyUSB0").read())
#     print(vali(test))

#     break