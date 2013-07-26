import urllib2, urllib
from BeautifulSoup import BeautifulSoup
from xml.dom import minidom
import re

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {}
data = urllib.urlencode(values)
headers = { 'User-Agent' : user_agent }
requestString = "http://imc/messageCriteria.do"
req = urllib2.Request(requestString, data, headers)
response = urllib2.urlopen(req)
thePage = response.read()
#print thePage
thePage = thePage.replace('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">', '')
thePage = thePage.replace('class', 'htmlclass')

theSoup = BeautifulSoup(thePage)
theFeederTable = theSoup.findAll('', id="feedersTable")

outfile = open("C:\\projects\\IMC.csv","w")

#print theFeederTable

theTable = theFeederTable[0]
outfile.write("Territory,Depot,Substation,Feeder,Description,Occured,Customers,EstimatedRestore\n")
for row in theTable:
    #print row
    print "-------------"
    theRowSoup = BeautifulSoup(str(row))
    theColumns = theRowSoup.findAll('td')
    if(len(theColumns) > 0):
        territory = theColumns[1].text
        depot = theColumns[2].text
        substation = theColumns[3].text
        theFeeder = theColumns[4].text
        theDescription = theColumns[5].text
        occured = theColumns[6].text
        customers = theColumns[8].text
        cause = theColumns[10].text
        estimatedRestore = theColumns[12].text
        outfile.write(territory+","+depot+","+substation+","+theFeeder+","+theDescription+","+occured+","+customers+","+estimatedRestore+"\n")
    #for column in theColumns:
    #    print column.text
