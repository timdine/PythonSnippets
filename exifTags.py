from __future__ import division
from PIL import Image
from PIL.ExifTags import TAGS
import arcgisscripting
import dircache


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag,tag)
        ret[decoded] = value
        print tag, value
    return ret
    
def DMStoDD(D, M, S):
    decSec = S / 60
    print decSec
    decMin = (M + decSec) / 60.
    print decMin
    decDeg = D + decMin
    print decDeg
    return decDeg

##Sample EXIF tags
##{0: (2, 2, 0, 0), 1: 'N', 2: ((45, 1), (17, 1), (34279, 2817)), 3: 'W', 4: ((62, 1), (40, 1), (8821, 356)), 5: 0, 6: (111199, 508), 7: ((16, 1), (3, 1), (46, 1)), 18: 'WGS-84', 29: '2010:07:15'}

#get_exif("c:\\PythonCode\\0022.jpg")

gp = arcgisscripting.create(9.3)
gp.workspace = "C:\\Data\\TransmissionPhotos"

theLayerName = "TransmissionPhotos5.shp"

if (gp.exists(theLayerName)):
    gp.delete(theLayerName)
gp.createfeatureclass(gp.workspace,theLayerName, "POINT")
gp.addfield(theLayerName, "PhotoName", "TEXT", "","","20")
gp.addfield(theLayerName, "DateTime", "TEXT", "", "", "20")

theIC = gp.insertcursor(theLayerName)

filelist = dircache.listdir("c:\\Data\\TransmissionPhotos")
print filelist

for file in filelist:
    try:
        print "-----------------------"
        print file
        theImage = Image.open("c:\\Data\\TransmissionPhotos\\"+file)

        info = theImage._getexif()

        latDeg = info[34853][2][0][0]/info[34853][2][0][1]
        latMin = info[34853][2][1][0]/info[34853][2][1][1]
        latSec = info[34853][2][2][0]/info[34853][2][2][1]
        
        lonDeg = info[34853][4][0][0]/info[34853][4][0][1]
        lonMin = info[34853][4][1][0]/info[34853][4][1][1]
        lonSec = info[34853][4][2][0]/info[34853][4][2][1]

        
        print "Hem Lat ", info[34853][1]
        print "Deg Lat ", latDeg
        print "Min Lat ", latMin
        print "Sec Lat ", latSec
        print "Hem Lon ", info[34853][3]
        print "Deg Lon ", lonDeg
        print "Min Lon ", lonMin
        print "Sec Lon ", lonSec
        print "Timestamp ", info[34853][7][0][0], ":", info[34853][7][1][0], ":", info[34853][7][2][0], " UTC"
        print "Datum ", info[34853][18]
        print "Datestamp ", info[34853][29]

        theDateTime = str(info[34853][29]) + " " + str(info[34853][7][0][0]) + ":" + str(info[34853][7][1][0]) + ":" + str(info[34853][7][2][0])

        theRow = theIC.NewRow()
        theRow.PhotoName = file
        thePoint = gp.createobject("Point")
        theX = DMStoDD(lonDeg, lonMin, lonSec) * -1. #We should check to see which hemisphere we're in and multiply based on that, but all data will be NW unless error.  Ignore errors for demo.
        print theX
        thePoint.X = theX
        theY = DMStoDD(latDeg, latMin, latSec)
        thePoint.Y = theY
        print thePoint.X
        print thePoint.Y
        theRow.SHAPE = thePoint
        theRow.setvalue("DateTime", theDateTime)
        theIC.InsertRow(theRow)
    except Exception, ex:
        print "Exception: ", str(ex)


