import xml.dom.minidom
import sys
import os
import time

_POSIX_OPEN_MAX = 16
def createDaemon():
    pid = os.fork()
    if pid < 0:
        sys.exit(0)
    if pid > 0:
        sys.exit(0)
    os.setsid()
    npid = os.fork()
    if npid < 0:
        sys.exit(0)
    if npid > 0:
        sys.exit(0)
    os.umask(0)
    os.chdir("/")
    print("current  id" , os.getpid())
    print("group    id" , os.getgid())  
    # x = os.sysconf(16)
    # k = 0
    # while (x >= k):
    #     print(k)
    #     sys.stdin.close()
    #     k += 1

def getcommand():
    doc = xml.dom.minidom.parse("kk.xml");
    name = doc.getElementsByTagName("name")[0]
    cmd = doc.getElementsByTagName("cmd")[0]
    numprocs = doc.getElementsByTagName("numprocs")[0]
    umask = doc.getElementsByTagName("umask")[0]
    workingdir = doc.getElementsByTagName("workingdir")[0]
    print(name.firstChild.data)
    print(cmd.firstChild.data)
    print(numprocs.firstChild.data)
    print(umask.firstChild.data)
    print(workingdir.firstChild.data)

def validate(xmlfile, dtdfile):
    dtd = etree.DTD(dtdfile)
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    status = dtd.validate(root) 
    if status:
        return(1)
    else:
        return(0)

if __name__ == "__main__":
    # xmlfile = "/Users/yabakhar/Desktop/task-master_python/kk.xml"
    # dtdfile = "/Users/yabakhar/Desktop/task-master_python/product.dtd"
    # x = validate(xmlfile,dtdfile)
    # if x == 1:
    #     getcommand()
    # else:
    #     print("Problem validating")
    while (1):
        createDaemon()
