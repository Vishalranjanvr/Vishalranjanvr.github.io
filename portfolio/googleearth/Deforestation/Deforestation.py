import xml.etree.ElementTree as ET
tree = ET.parse('/Users/aaronsletten/Desktop/PRODES_deforestation.kml')
root = tree.getroot()

#Settings
height = 10000

#for elem in root.iter():
#    print elem.tag

count = 0

#For coordinates
boundingBoxes = []

for elem in root.iter():
    if elem.tag == "{http://www.opengis.net/kml/2.2}coordinates":
        if count >= 50000:
            break
        count += 1
        
        #Split by space
        commaStr = elem.text.split()
        latList = []
        longList = []
        for i in range(0,len(commaStr)):
            #Split by comma
            temp = commaStr[i].split(",")
            longList.append(float(temp[0]))
            latList.append(float(temp[1]))

        #Get bounding box

        maxLong = max(longList)
        minLong = min(longList)
        maxLat = max(latList)
        minLat = min(latList)

#        print "Max long: " + str(maxLong)
#        print "Min long: " + str(minLong)
#        print "Max Lat: " + str(maxLat)
#        print "Min Lat: " + str(minLat)

        #Set bounding box values
        #Order: Top left, top right, bottom right, bottom left
        boundingBoxes.append(((maxLong,maxLat), (minLong, maxLat), (minLong,minLat), (maxLong, minLat)))


#for i in range(0, len(boundingBoxes)):
#    print(boundingBoxes[i][0])


#BUILD KML

# build a tree structure
root = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
#Use document for multiple placemarkers
document = ET.SubElement(root, "Document")

#Go through all animals
for i in range(0, len(boundingBoxes)):
    
    placemark = ET.SubElement(document, "Placemark")
    
    #PLACEMARK STYLE
    style = ET.SubElement(placemark, "Style")
    polyStyle = ET.SubElement(style, "PolyStyle")
    color = ET.SubElement(polyStyle, "color")
    color.text = "321400FF"
#    <Polygon><outerBoundaryIs><LinearRing>
    polygon = ET.SubElement(placemark, "Polygon")
    extrude = ET.SubElement(polygon, "extrude")
    extrude.text = "1"
    altitudeMode = ET.SubElement(polygon, "altitudeMode")
    altitudeMode.text = "relativeToGround"
    outerBoundary = ET.SubElement(polygon, "outerBoundaryIs")
    linearRing = ET.SubElement(outerBoundary, "LinearRing")
    coordinates = ET.SubElement(linearRing, "coordinates")
    
    tempStr = ""
    
    for j in range(0, len(boundingBoxes[i])):
        #print boundingBoxes[i][j]
        tempStr += str(boundingBoxes[i][j][0]) + "," + str(boundingBoxes[i][j][1]) + "," + str(height) + "\n"
    
    coordinates.text = tempStr

    #PLACEMARK TEXT
    #    name = ET.SubElement(placemark, "name")
    #    name.text = animals[i].name

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("/Users/aaronsletten/Desktop/Deforestation.kml")



