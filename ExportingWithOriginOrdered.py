import rhinoscriptsyntax as  rs
import Rhino as rh
from System.Drawing import Color


X_ST = 0
Y_ST = 0
X_Step = 9000
Y_Step = 10000
Sail_Name = rs.GetString("Input Sail Number")
x = rs.GetInteger("Number of Drawings in X direction")
y = rs.GetInteger("Number of Drawings in Y direction")
direct = rs.BrowseForFolder(None,"Choose a folder",None)

#Define color to exort geometry to DWG cause cannot see black in DWG
Black = Color.Black
White = Color.White

#Change black color to white
layers = rs.LayerIds()
for layer in layers:
    print rs.LayerColor(layer)
    if rs.LayerColor(layer) == Black:
        rs.LayerColor(layer, White)

#Select the drawings which are in grid and export.
for j in range(y):
    for i in range(x):
        x_cnt = X_ST + i*X_Step
        y_cnt = Y_ST + j*Y_Step
        x1 = x_cnt - X_Step/2
        x2 = x_cnt + X_Step/2
        y1 = y_cnt -2300
        y2 = y_cnt + 4900
        k = str(int(i +1)).zfill(2)
        l = str(int(j +1)).zfill(2)
        path = direct + "/" + Sail_Name + "-" + l + k + ".dwg"
        rs.WindowPick((x1,y1,0), (x2,y2,0),  "Top", True)
        org = '{},{},0'.format(x_cnt,y_cnt)
        CommandLine = '_-ExportWithOrigin {} "{}" _Enter'.format(org,path)
        rs.Command(CommandLine)
        rs.Command("_Hide")
rs.Command("_Show")

#Reset color to black
for layer in layers:
    if rs.LayerColor(layer) == White:
        rs.LayerColor(layer, Black)