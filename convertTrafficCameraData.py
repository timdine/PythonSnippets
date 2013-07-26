import arcgisscripting
gp = arcgisscripting.create(9.3)

infile = open("c:\\projects\\trafficCamera.txt")

theCur = gp.insertcursor("c:\\projects\\TrafficCameras.shp")

camera = infile.readline()
while camera:
    #print camera
    firstSplit = camera.split(" N ")
    cameraName = firstSplit[0]
    cameraCoordinates = firstSplit[1].split(" W ")
    
    ysplit = cameraCoordinates[0].split(" ")
    lat = float(ysplit[0]) + (float(ysplit[1]) / 60)
    xsplit = cameraCoordinates[1].split(" ")
    lon = float(xsplit[0]) + (float(xsplit[1]) / 60)
    theRow = theCur.newrow()
    thePoint = gp.createobject("Point")
    thePoint.X = -1 * lon
    thePoint.Y = lat
    theRow.Shape = thePoint
    theRow.Location = cameraName
    theCur.insertrow(theRow)
    camera = infile.readline()