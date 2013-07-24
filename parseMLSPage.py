import os
import string
import sys, httplib,urllib
from xml.dom import minidom
import time



REQUEST_TEMPLATE = """<soap:Envelope
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetCivicAddress xmlns="http://142.176.62.103/Geonova_WS/CivicAddressPointRange">
        <Version>%s</Version>
        <MUN_CODE>%s</MUN_CODE>
        <MUN_NAME>%s</MUN_NAME>
        <GSA_KEY>%s</GSA_KEY>
        <GSA_NAME>%s</GSA_NAME>
        <STR_KEY>%s</STR_KEY>
        <STR_NAME>%s</STR_NAME>
        <STR_TYPE>%s</STR_TYPE>
        <F_STR_TYPE>%s</F_STR_TYPE>
        <STR_DIR>%s</STR_DIR>
        <CIVIC_NUM>%s</CIVIC_NUM>
        <UNIT_NUM>%s</UNIT_NUM>
        <NAMECODE>%s</NAMECODE>
        <GEOMETRY>%s</GEOMETRY>
        </GetCivicAddress>
    </soap:Body>
</soap:Envelope>"""


version = "1.00"
mun_code = ""
mun_name = ""
gsa_key = ""
gsa_name = "Stewiacke%20East"
str_key = ""
str_name = "Cloverdale"
str_type = ""
f_str_type = ""
str_dir = ""
civic_num = "4505"
unit_num = ""
namecode = ""
geometry = "1"

#conn = httplib.HTTPConnection("142.176.62.103")
#params = urllib.urlencode({'Version': '1.00','MUN_CODE': '', 'MUN_NAME': '', 'GSA_KEY': '','GSA_NAME': 'Stewiacke East', 'STR_KEY': '', 'STR_NAME': 'Cloverdale', 'STR_TYPE': '', 'F_STR_TYPE': '', 'STR_DIR': '', 'CIVIC_NUM': '4505', 'UNIT_NUM': '', 'NAMECODE': '', 'GEOMETRY': '1'})
#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

#conn.request("POST","/GEONOVA_WS/CivicAddressPointRange.asmx/GetCivicAddress",params,headers)
#response = conn.getresponse()
#dom = minidom.parse(response)
#print dom.toxml()


#print ""
#addresses = dom.getElementsByTagName("CivicAddress")
#for address in addresses:
#    civicNums = address.getElementsByTagName("CIVICNUM")
#    streets = address.getElementsByTagName("STR_NAME")
#    streetType = address.getElementsByTagName("STR_TYPE")
#    addressPoint = address.getElementsByTagName("CivicAddressPoint")
#    XCoord = addressPoint[0].getElementsByTagName("X")
#    YCoord = addressPoint[0].getElementsByTagName("Y")
    
    
#    print civicNums[0].firstChild.data + " " + streets[0].firstChild.data + " " + streetType[0].firstChild.data + " - " + XCoord[0].firstChild.data + "," + YCoord[0].firstChild.data

#print response.status, response.reason


#data = response.read()
#print dom
#thePostString = "/GEONOVA_WS/CivicAddressPointRange.asmx/GetCivicAddress?Version=1.00&MUN_CODE=&MUN_NAME=&GSA_KEY=&GSA_NAME=Stewiacke%20East&STR_KEY=&STR_NAME=Cloverdale&STR_TYPE=&F_STR_TYPE=&STR_DIR=&CIVIC_NUM=4505&UNIT_NUM=&NAMECODE=&GEOMETRY=1"




infilename = "c:\\temp\\LargeTest.txt"
outfilename = "c:\\temp\\Large_1.csv"
outfilenameNotFound = "c:\\temp\\LargeNotFound_1.csv"
outfileStreets = "c:\\temp\\LargeNoCivic.csv"
infile = open(infilename, "r")
outfile = open(outfilename, "w")
outfileNotFound = open(outfilenameNotFound, "w")
outfileNoCivic = open(outfileStreets, "w")

outfile.write("Price,Address,Community,Province,MLS,Hyperlink,Description,X,Y,Accuracy\n")
outfileNotFound.write("Price,Address,Community,Province,MLS,Hyperlink,Description,X,Y,Accuracy\n")
outfileNoCivic.write("Price,Address,Community,Province,MLS,Hyperlink,Description,X,Y,Accuracy\n")

validStreetSuffix = [["Avenue","Ave"],["Court","Crt"],["Crescent","Cres"],["Drive","Dr"],["LANE","LANE"],["RD","Rd"],["Road","Rd"],["ROAD","Rd"],["ST","St"],["Street","St"],["Way","Way"]]
highwayAlias = ["HIGHWAY", "HWY", "NO"]

i=0
test = "PlaceHolder"
while (test != ""):
    #print "Sleeping"
    #time.sleep(5)
    #print "Done"
    try:
        test = infile.readline()
        if (test[0] == "$"):
            priceAddress = test.split(" ")
            price = priceAddress[0].replace(",","") #gets the address from the first line
            #print "Price: " + price

            priceAddress.pop(0)     #removes the address from the array
            address = string.join(priceAddress, " ").strip()    #merges the rest of the line back into the street address
            print "Address: " + address

            addressNoPound = address.replace("#","")
            addressArray = addressNoPound.split(" ")
            geoCivicNum = ""
            geoStreet = ""
            geoStreetType = ""
            geoGSA = ""

            x="0"
            y="0"

            found = 0

            print addressArray
            
            if (addressArray[0].isdigit()): #Leading number is usually a civic address
                geoCivicNum = addressArray[0]
                addressArray.pop(0)
            
            
            if addressArray[len(addressArray) - 1].isdigit(): #Trailing number is a Highway number
                geoStreet = string.join(addressArray, " ").strip()
                for hwyAlias in highwayAlias:
                    geoStreet = geoStreet.replace(hwyAlias, "Highway")
                    print "Highway Replace: " + geoStreet
            else:
                for suffix in validStreetSuffix:
                    if (addressArray[len(addressArray) - 1] == suffix[0]):
                        if (len(suffix[0]) > 1):
                            geoStreetType = suffix[1]
                        else:
                            geoStreetType = addressArray[len(addressArray) - 1]
                        addressArray.pop(len(addressArray) - 1)
                if (len(addressArray) > 1):
                    geoStreet = string.join(addressArray," ").strip()
                else:
                    geoStreet = addressArray[0]
                
            communityProvince = infile.readline().split(",")
            community = communityProvince[0]
            province = communityProvince[1].strip()
            print community
            print province
            
            blank = infile.readline()
            blank = infile.readline()

            mls = infile.readline()
            mls = mls.replace('MLS®: ','')
            mlsarray = mls.split(" ")
            mls = mlsarray[2]
            #print mlsarray
            print "MLS: " + mls
            
            description = infile.readline()
            description = description.replace(","," ")
            description = ""
            print "Description: " + description
            
            if (geoCivicNum != ""):
                
                print "geoCivic: " + geoCivicNum
                print "geoStreet: " + geoStreet
                print "geoStreetType: "+ geoStreetType    
                
                params = urllib.urlencode({'Version': '1.00','MUN_CODE': '', 'MUN_NAME': '', 'GSA_KEY': '','GSA_NAME': '', 'STR_KEY': '', 'STR_NAME': geoStreet, 'STR_TYPE': geoStreetType, 'F_STR_TYPE': '', 'STR_DIR': '', 'CIVIC_NUM': geoCivicNum, 'UNIT_NUM': '', 'NAMECODE': '', 'GEOMETRY': '1'})
                headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                conn = httplib.HTTPConnection("142.176.62.103")
                conn.request("POST","/GEONOVA_WS/CivicAddressPointRange.asmx/GetCivicAddress",params,headers)
                response = conn.getresponse()
                print response.status, response.reason
                dom = minidom.parse(response)
                #print dom.toxml()
                
                addresses = dom.getElementsByTagName("CivicAddress")
                for addressGeo in addresses:
                    try:
                        civicNums = addressGeo.getElementsByTagName("CIVICNUM")
                        streets = addressGeo.getElementsByTagName("STR_NAME")
                        streetType = addressGeo.getElementsByTagName("STR_TYPE")
                        addressPoint = addressGeo.getElementsByTagName("CivicAddressPoint")
                        XCoord = addressPoint[0].getElementsByTagName("X")
                        YCoord = addressPoint[0].getElementsByTagName("Y")
                        print civicNums[0].firstChild.data + " " + streets[0].firstChild.data + " " + streetType[0].firstChild.data + " - " + XCoord[0].firstChild.data + "," + YCoord[0].firstChild.data
                        if (XCoord[0].firstChild.data == "0"): #In case there is more then one point for the address and some are zerod.  If there are more then one any are as valid as any other
                            print "Invalid Coordinates"
                        else:
                            x = XCoord[0].firstChild.data
                            y = YCoord[0].firstChild.data
                        #found = 1
                    except:
                        #found = 0
                        print "Except"
                            #outfile.write("Test\n")
                if (x == "0"):
                    outfileNotFound.write(price +","+ address +","+ community +","+ province +","+ mls +","+ "http://www.mls.ca/propertyResults.aspx?Mode=5&id="+ mls +"," + description +","+ x + "," + y + ",None\n")
                    print "--------"
                else:
                    outfile.write(price +","+ address +","+ community +","+ province +","+ mls +","+ "http://www.mls.ca/propertyResults.aspx?Mode=5&id="+ mls +"," + description + "," + x + "," + y + ",Civic\n")
                    print "--------"
            else:
                geoGSA = community
                geoStreet = geoStreet
                geoStreetType = geoStreetType
                print "geoGSA: " + geoGSA
                print "geoStreet: " + geoStreet
                print "geoStreetType: "+ geoStreetType     
                
                #Version=string&MUN_CODE=string&MUN_NAME=string&GSA_KEY=string&GSA_Name=string  &STR_KEY=string &STR_NAME=string&STR_TYPE=string&F_STR_TYPE=string&STR_DIR=string&NAME_CODE=string&GEOMETRY=string 
                #Version=1.00&MUN_CODE=&MUN_NAME=&GSA_KEY=&GSA_Name=ENFIELD&STR_KEY=&STR_NAME=BAKERY&STR_TYPE=&F_STR_TYPE=&STR_DIR=&NAME_CODE=&GEOMETRY=2
                params = urllib.urlencode({'Version': '1.00','MUN_CODE': '', 'MUN_NAME': '', 'GSA_KEY': '','GSA_NAME': 'ENFIELD', 'STR_KEY': '', 'STR_NAME': '', 'STR_TYPE': '', 'F_STR_TYPE': '', 'STR_DIR': '','NAMECODE': '', 'GEOMETRY': '0'})
                headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                conn = httplib.HTTPConnection("142.176.62.103")
                getRequest = "/GEONOVA_WS/CivicAddressPointRange.asmx/GetStreets?Version=1.00&MUN_CODE=&MUN_NAME=&GSA_KEY=&GSA_Name="+geoGSA+"&STR_KEY=&STR_NAME="+geoStreet+"&STR_TYPE="+geoStreetType+"&F_STR_TYPE=&STR_DIR=&NAME_CODE=&GEOMETRY=2"
                getRequest = getRequest.replace(" ","%20")
                conn.request("GET",getRequest)
                
                #http://142.176.62.103/GEONOVA_WS/CivicAddressPointRange.asmx/GetStreets?Version=1.00&MUN_CODE=&MUN_NAME=&GSA_KEY=&GSA_Name=ENFIELD&STR_KEY=&STR_NAME=BAKERY&STR_TYPE=&F_STR_TYPE=&STR_DIR=&NAME_CODE=&GEOMETRY=0
                response = conn.getresponse()
                print response.status, response.reason
                dom = minidom.parse(response)
                foundStreet = dom.getElementsByTagName("Street")
                for eachStreet in foundStreet:
                    foundStreetBoundingBox = eachStreet.getElementsByTagName("BoundingBox")
                    foundXCoords = foundStreetBoundingBox[0].getElementsByTagName("X")
                    foundYCoords = foundStreetBoundingBox[0].getElementsByTagName("Y")
                minX = 0.0
                minY = 0.0
                maxX = 0.0
                maxY = 0.0

                #print float(foundXCoords[0].firstChild.data)

                if (minX == 0.0):
                    minX = float(foundXCoords[0].firstChild.data)
                    maxX = float(foundXCoords[0].firstChild.data)
                else:
                    if (float(foundXCoords[0].firstChild.data) < minX):
                        minX = float(foundXCoords[0].firstChild.data)
                    if (float(foundXCoords[0].firstChild.data) > maxX):
                        maxX = float(foundXCoords[0].firstChild.data)                        
                if (minY == 0.0):
                    minY = float(foundYCoords[0].firstChild.data)
                    maxY = float(foundYCoords[0].firstChild.data)
                else:
                    if (float(foundYCoords[0].firstChild.data) < minY):
                        minY = float(foundYCoords[0].firstChild.data)
                    if (float(foundYCoords[0].firstChild.data) > maxY):
                        maxY = float(foundYCoords[0].firstChild.data)
                
                x = str((minX/2) + (maxX/2))
                y = str((minY/2) + (maxY/2))
                
                #print minX,minY,maxX,maxY
                print address + " - " + x + "," + y
                if (x == "0"):
                    outfileNotFound.write(price +","+ address +","+ community +","+ province +","+ mls +","+ "http://www.mls.ca/propertyResults.aspx?Mode=5&id="+ mls +"," + description +","+ x + "," + y + ",None\n")
                else:
                    outfile.write(price +","+ address +","+ community +","+ province +","+ mls +","+ "http://www.mls.ca/propertyResults.aspx?Mode=5&id="+ mls +"," + description +","+ x + "," + y + ",Street\n")
                    #outfileNoCivic.write(price +","+ address +","+ community +","+ province +","+ mls +","+ "http://www.mls.ca/propertyResults.aspx?Mode=5&id="+ mls +"," + description +","+ x + "," + y + ",Street\n")
                print "--------"
    except:
        test = ""
