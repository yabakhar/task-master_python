from lxml import etree, objectify
from io import StringIO
import sys



def validate(xmlfile, dtdfile):
    dtd = etree.DTD(dtdfile)
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    status = dtd.validate(root) 
    if status:
        print("ok")
    else:
        print("Problem validating")

if __name__ == "__main__":
    xmlfile = "/Users/yabakhar/Desktop/task-master_python/kk.xml"
    dtdfile = "/Users/yabakhar/Desktop/task-master_python/product.dtd"
    validate(xmlfile,dtdfile)

