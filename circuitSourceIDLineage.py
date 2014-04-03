import arcpy

class aCircuitSource:
    def __init__(self, objectID, name, parentCircuitSourceID):
	    self.objectID = objectID
	    self.name = name
	    self.parentCircuitSourceID = parentCircuitSourceID

def lookForChildSources(objectID, circuitSources, indentLevel):
	for circuitSource in circuitSources:
		if (circuitSource.parentCircuitSourceID == objectID and circuitSource.objectID != objectID):
			print indentLevel, circuitSource.name
			lookForChildSources(circuitSource.objectID, circuitSources, indentLevel+"  ")


fc = r"Database Connections\gis@gisprd01.sde\GIS.CircuitSourceID"
fields = ["OBJECTID", "FEEDERNAME", "PARENTCIRCUITSOURCEID"]

circuitSources = []


with arcpy.da.SearchCursor(fc, fields) as cursor:
	for row in cursor:
		#print("{0}, {1}, {2}".format(row[0], row[1], row[2]))
		circuitSources.append(aCircuitSource(row[0], row[1], row[2]))
		
for circuitSource in circuitSources:
	if (circuitSource.parentCircuitSourceID == circuitSource.objectID):
		print circuitSource.name
		lookForChildSources(circuitSource.objectID, circuitSources,"	")
			