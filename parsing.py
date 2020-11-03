from lxml import etree, objectify
import sys
import daemons

# def mydeamon(deam):
#     print(deam)

def validate(xmlfile, dtdfile):
    dtd = etree.DTD(dtdfile)
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    status = dtd.validate(root) 
    if status:
        print("validate successfully")
    else:
        print("Problem validating")

if __name__ == "__main__":
    xmlfile = "/Users/yabakhar/Desktop/task-master_python/kk.xml"
    dtdfile = "/Users/yabakhar/Desktop/task-master_python/product.dtd"
    validate(xmlfile,dtdfile)
    # mydeamon("yabakhar")
