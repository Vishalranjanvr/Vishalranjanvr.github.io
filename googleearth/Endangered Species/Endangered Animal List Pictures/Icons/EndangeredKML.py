import csv
import xml.etree.cElementTree as ET
import os
import string

#Define a Animal class
class Animal:
    def __init__(self, name = "", sciName = "", status = "", website = "", places = "",latitude = 0, longitude = 0):
        self.latitude = latitude
        self.longitude = longitude
        self.sciName = sciName
        self.name = name
        self.status = status
        self.website = website
        self.places = places

#LOAD CVS

#Create new list of Animals
animals = []

with open(str('C:\Users\Vishal Ranjan\Desktop\NDSU Courses\computational techno\Endangered Species\List.csv'), 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    #Get first row so its not read later
    firstRow = reader.next()

    #Look for 1960 in year string
    for row in reader:
        temp = Animal(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        animals.append(temp)
        #print(temp.name)

#BUILD KML

# build a tree structure
root = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
#Use document for multiple placemarkers
document = ET.SubElement(root, "Document")

#Go through all animals
for i in range(0, len(animals)):

    placemark = ET.SubElement(document, "Placemark")

    #PLACEMARK STYLE
    style = ET.SubElement(placemark, "Style")
    iconStyle = ET.SubElement(style, "IconStyle")
    icon = ET.SubElement(iconStyle, "Icon")
    scale = ET.SubElement(iconStyle, "scale")
    scale.text = "7"
    href = ET.SubElement(icon, "href")
    href.text = animals[i].name + ".png"
    
    #PLACEMARK TEXT
#    name = ET.SubElement(placemark, "name")
#    name.text = animals[i].name

    description = ET.SubElement(placemark, "description")
    description.text = "\n<h3>Name:</h3> " + animals[i].name + "\n<h3>Scientific Name:</h3> " + animals[i].sciName + " \n<h3>Status:</h3> " + animals[i].status + " \n<h3>Places: </h3>" + animals[i].places + " \n<h3>Website:</h3> " + animals[i].website
    
    #PLACEMARK POSISTION
    point = ET.SubElement(placemark, "Point")

    coordinates = ET.SubElement(point, "coordinates")
    coordinates.text = str(animals[i].latitude) + ","+ str(animals[i].longitude) +",0"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("Endangered Animals.kml")
