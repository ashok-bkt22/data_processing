from xml.dom.minidom import parse
# Open XML document using minidom parser
DOMTree = parse("rect.xml")
collection = DOMTree.documentElement

# Get all the objects in the collection
objects = collection.getElementsByTagName("object")

# Print detail of each object.
for object in objects:
   type = object.getElementsByTagName('name')[0]
   print("Type: %s" % type.childNodes[0].data)

   xmin = object.getElementsByTagName('xmin')[0]
   print("Type: %s" % xmin.childNodes[0].data)

   ymin = object.getElementsByTagName('ymin')[0]
   print("Type: %s" % ymin.childNodes[0].data)

   xmax = object.getElementsByTagName('xmax')[0]
   print("Type: %s" % xmax.childNodes[0].data)

   ymax = object.getElementsByTagName('ymax')[0]
   print("Type: %s" % ymax.childNodes[0].data)

