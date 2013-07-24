from urllib2 import urlopen
from ClientForm import ParseResponse
import sys

if len(sys.argv) == 1:
    centerY = "450000"
    centerX = "650000"
    radius = "500"
    stationType = "broadcast"
    outputXYFile = "C:\\PythonCode\\RadioTower.csv"
elif len(sys.argv) == 6:
    centerY = sys.argv[1]
    centerX = sys.argv[2]
    radius = sys.argv[3]
    stationType = sys.argv[4]
    outputXYFile = sys.argv[5]
else:
    print "You have entered incorrect parameters"
    sys.exit

def DMStoDD(degrees, minutes, seconds):
    #print Degrees + " " + Minutes + " " + Seconds
    DecimalDegrees = float(degrees) + (float(minutes) * 1/60) + (float(seconds) * 1/60 * 1/60)
    return DecimalDegrees

response = urlopen("https://apollo.ic.gc.ca/pls/engdoc_anon/web_search.geographical_input")
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]

print form

form["frequency_1"] = "1"
form["frequency_2"] = "9999"
form["txrx"] = ["TXRX"]
form["p_centre_latitude"] = centerY
form["p_centre_longitude"] = centerX
form["radius"] = radius
#form["station_type"] = [stationType]
form["output_format"] = ["2"]

outFileName = outputXYFile
outFile = open(outFileName, "w")
outFile.write("Frequency,Location,X,Y\n")

theReturnedRawData = urlopen(form.click())
inData = 0
for line in theReturnedRawData:
    if line.find("[DATA]") >= 0:
        inData = 1
        #print "Started"
    elif line.find("[/DATA]") >= 0:
        inData = 0
        #print "Stopped"
    #print inData

    #print line
    
    if inData == 1 and line <> "" and line.find("[DATA]") <> 0:
        #print line[1:15] + " " + line[81:88] + " " + line[89:96] + " " + line[96:131]
        frequency = line[1:15].strip()
        location = line[96:131].strip()
        yCoord = line[81:88].strip()
        xCoord = line[89:96].strip()
        callsign = line
        yDD = DMStoDD(yCoord[0:2], yCoord[2:4], yCoord[4:])
        xDD = -1 * DMStoDD(xCoord[0:2], xCoord[2:4], xCoord[4:])
        outFile.write(str(frequency)+","+str(location)+","+str(xDD)+","+str(yDD)+"\n")
