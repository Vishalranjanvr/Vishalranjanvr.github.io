import csv
import xml.etree.cElementTree as ET
import os
import string

#Define a station class
class Station:
    def __init__(self, latitude = 0, longitude = 0, temperature = 0, name = "", date = ""):
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature
        self.name = name
        self.date = date

def fareheit(number):
    return number * 1.8 + 32

#COLOR STUFF
def make_color_tuple( color ):
    """
        turn something like "#000000" into 0,0,0
        or "#FFFFFF into "255,255,255"
        """
    R = color[1:3]
    G = color[3:5]
    B = color[5:7]
    
    R = int(R, 16)
    G = int(G, 16)
    B = int(B, 16)
    
    return R,G,B

def interpolate_tuple( startcolor, goalcolor, steps ):
    """
        Take two RGB color sets and mix them over a specified number of steps.  Return the list
        """
    # white
    
    R = startcolor[0]
    G = startcolor[1]
    B = startcolor[2]
    
    targetR = goalcolor[0]
    targetG = goalcolor[1]
    targetB = goalcolor[2]
    
    DiffR = targetR - R
    DiffG = targetG - G
    DiffB = targetB - B
    
    buffer = []
    
    for i in range(0, steps +1):
        iR = R + (DiffR * i / steps)
        iG = G + (DiffG * i / steps)
        iB = B + (DiffB * i / steps)
        
        hR = string.replace(hex(iR), "0x", "")
        hG = string.replace(hex(iG), "0x", "")
        hB = string.replace(hex(iB), "0x", "")
        
        if len(hR) == 1:
            hR = "0" + hR
        if len(hB) == 1:
            hB = "0" + hB
        
        if len(hG) == 1:
            hG = "0" + hG
        
        color = string.upper("#"+hR+hG+hB)
        buffer.append(color)
    
    return buffer

def interpolate( startcolor, goalcolor, steps ):
    """
        wrapper for interpolate_tuple that accepts colors as html ("#CCCCC" and such)
        """
    start_tuple = make_color_tuple(startcolor)
    goal_tuple = make_color_tuple(goalcolor)
    
    return interpolate_tuple(start_tuple, goal_tuple, steps)





#LOAD CVS

#Get file names
fileNames = os.listdir("/Users/aaronsletten/Desktop/gsom-latest")

#Create new list on Stations
stations = []

for i in range(0,5000):
    with open(str('/Users/aaronsletten/Desktop/gsom-latest/' + fileNames[i]), 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        #Flag for temp in file
        tempInFile = False
        tempIndex = 0

        #Find TAVG in first row
        firstRow = reader.next()
        
        for j in range(0, len(firstRow)):
            #if firstRow[j] == "TAVG":
            if firstRow[j] == "TMAX":
                tempInFile = True
                tempIndex = j
                break
    
        #If there is a TAVG get the first value
        #If there is a TAVG get the first value
        if tempInFile:
            #Find year 1960
            containsYear = False
            yearRow = []
            
            #Look for 1960 in year string
            for row in reader:
                if row[1].find("1960-01") != -1:
                    if row[tempIndex] != "":
                        containsYear = True
                        yearRow = row
                    break
            #If row was found add it to the stations array
            if containsYear:
                tempStation = Station()
                tempStation.name = yearRow[5]
                tempStation.date = yearRow[1]
                tempStation.latitude = yearRow[2]
                tempStation.longitude = yearRow[3]
                tempStation.temperature = yearRow[tempIndex]
                stations.append(tempStation)

#Get list of temps
temps = []
for i in range(0, len(stations)):
    if stations[i].temperature != "":
        temps.append(float(stations[i].temperature))

max = max(temps)
min = min(temps)

#Create color map
colors = interpolate("#0061ff","#ff0000" , 100)

#BUILD KML

# build a tree structure
root = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
#Use document for multiple placemarkers
document = ET.SubElement(root, "Document")

#Go through all stations
for i in range(0, len(stations)):
    #Calculate color -50 to pos 50
    actColor = "00ffffff"
    
    if stations[i].temperature != "":
        tem = int((float(stations[i].temperature) + abs(min)) / (max-min) * 100)
        tempColor = colors[tem]

        actColor = "ff" + tempColor[5:] + tempColor[3:-2] + tempColor[1:-4]

    
    placemark = ET.SubElement(document, "Placemark")

    #PLACEMARK STYLE
    style = ET.SubElement(placemark, "Style")
    iconStyle = ET.SubElement(style, "IconStyle")
    color = ET.SubElement(iconStyle, "color")
    #aabbggrr
    #color.text = "FF1400FF"
    color.text = actColor
    icon = ET.SubElement(iconStyle, "Icon")
    scale = ET.SubElement(iconStyle, "scale")
    scale.text = "2"
    href = ET.SubElement(icon, "href")
    href.text = "Fire.png"

    #PLACEMARK TEXT
    name = ET.SubElement(placemark, "name")
    name.text = str(fareheit(float(stations[i].temperature)))

    description = ET.SubElement(placemark, "description")
    description.text = "This is a cool description"

    #PLACEMARK POSISTION
    point = ET.SubElement(placemark, "Point")

    coordinates = ET.SubElement(point, "coordinates")
    coordinates.text = str(stations[i].longitude) + ","+ str(stations[i].latitude) +",0"


# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("test.kml")



