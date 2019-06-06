
import os
import rhinoscriptsyntax as rs
import Rhino

#FolderLocation
mydir = rs.StringBox("Insert folder path")

def getRhinoFile(dir):
    pathList = []
    for file in os.listdir(dir):
        if file.endswith(".3dm"):
            path = dir + "\\" + file
            pathList.append(path)
            print (path)
    return (pathList)

test = getRhinoFile(mydir)

def insertFile(fList):
    for item in fList:
        origin = 0,0,0
        origin = str(origin)
        item = '"' + item + '"'
        #Defining Rhino command
        iCommand = "-insert F L L {} B 0 1 0 -Enter _Hide".format(item)
        rs.Command("%s" %iCommand)

insertFile(test)
#Show result after imported
rs.Command("_Show")