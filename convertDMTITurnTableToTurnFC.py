#!/usr/bin/env python

"""convertDMTITurnTableToTurnFC.py: Convert the information found in DMTI's CanMap Route Logistics turn table into a turn feature class"""
"""which can be used by ArcGIS Network Analyst.  Combining this with the One Way restriction on To/From and the time in minutes as an """
"""impedance made it possible to turn the data into a routable network supporting directions.  The target feature class for the insert cursor"""
"""must be a Turn Feature Class created with the 'Create Turn Feature Class' tool.  I also had to run this script 'in process' from my map"""
"""document to update the feature class in an edit session.  The script should technically be able to be rewritten to support starting an edit"""
"""session."""


__author__      = "Tim Dine"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Sample"




import arcpy

class aTurnRestriction:
    def __init__(self, fromNode, toNode, restricted):
	    self.fromNode = fromNode
	    self.toNode = toNode
	    self.restricted = restricted
	    

targetTurnFC = r"C:\Data\NS\Streets\RoadNetwork.gdb\RoadNet\theTurns"
sourceRoadEdges = r"C:\Data\NS\Streets\RoadNetwork.gdb\RoadNet\NSrte"
sourceTurnTable = r"C:\Data\NS\Streets\NStrn.dbf"

lineDict = {}
lineOIDDict = {}

theLineIC = arcpy.da.InsertCursor(targetTurnFC, 
	("SHAPE@", "Edge1FID", "Edge2FID", "Edge1End", "Edge1FCID", "Edge1Pos", "Edge2FCID", "Edge2Pos"))

arcpy.AddMessage("Loading Roads")
lineCountRead = 0
with arcpy.da.SearchCursor(sourceRoadEdges, ("UNIQUEID", "SHAPE@", "OBJECTID")) as cursor:
	for row in cursor:
		lineDict[row[0]] = row[1].positionAlongLine(0.5,True)
		lineOIDDict[row[0]] = row[2]
		lineCountRead += 1
		if (lineCountRead % 10000 == 0):
			arcpy.AddMessage(lineCountRead)

arcpy.AddMessage("Building Lines")
lineCountBuilt = 0
with arcpy.da.SearchCursor(sourceTurnTable, ("TURN_ID", "RDS_ID", "RES_RDS_ID")) as cursor:
	for row in cursor:
		try:
			#print row
			#print lineDict[row[1]], lineDict[row[2]]
			
			lineArray = []
			
			#thePoint = arcpy.Point(lineDict[row[1]][0],lineDict[row[1]][1])
			thePoint = lineDict[row[1]].firstPoint
			lineArray.append(thePoint)	
			
			#thePoint = arcpy.Point(lineDict[row[2]][0],lineDict[row[2]][1])
			thePoint = lineDict[row[2]].firstPoint
			lineArray.append(thePoint)	
			
			array = arcpy.Array(lineArray) 
			polyline = arcpy.Polyline(array)
			
			#theShape = lineDict[row[1]] + lineDict[row[2]]
			#print theShape
			theLineIC.insertRow([polyline, lineOIDDict[row[1]], lineOIDDict[row[2]], "N", 9, 0.5, 9, 0.5])
		except Exception,e:
			arcpy.AddMessage(str(e))
		if (lineCountBuilt % 1000 == 0):
			arcpy.AddMessage(lineCountBuilt)
		lineCountBuilt += 1

arcpy.AddMessage("Done")