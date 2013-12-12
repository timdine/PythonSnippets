#!/usr/bin/env python

"""schemaUpdatesJuly2013.py: Makes a number of schema updates to the geodatabase.  Fields are needed to support new functionality."""


__author__      = "Tim Dine"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Development"

import arcpy

geodatabaseConnection = r'Database Connections\gis@gisprd01.sde'
arcpy.env.workspace = geodatabaseConnection + "\\GIS.Electric"

workdepotFCs = [
'riser',
'supportstructure',
'anchorguy',
'spanguy',
'warningsign',
'abandonedelectriclinesegment',
'scadameasurement',
'pushbrace',
'kirkkeyinterlock',
'conductorjunction',
'communicationcable',
'deliverypoint',
'servicepoint',
'primarymeter',
'streetlight',
'aerialmarker']

admsIDFCs = [
'dynamicprotectivedevice',
'transformer',
'switch',
'fuse',
'voltageregulator']

print "Adding WorkDepot"
for fc in workdepotFCs:
	print fc
	arcpy.AddField_management(fc, "WORKDEPOT", "TEXT", "", "", 20,"Work Depot")

print "Adding ADMSID"	
for fc in admsIDFCs:
	print fc
	arcpy.AddField_management(fc, "ADMSID", "TEXT", "", "", 20,"ADMS ID")
	


arcpy.AddField_management("conductorjunction", "StitchingPoint", "TEXT", "", "", 3,"Stitching Point")

arcpy.CreateDomain_management(geodatabaseConnection, "Stitching Point", "Stitching Point", "TEXT", "CODED")

print arcpy.GetMessages()

domDict = {"FH":"Feeder Head", "FE":"Feeder End", "NA":"Not Applicable"}
for code in domDict:
	arcpy.AddCodedValueToDomain_management(geodatabaseConnection, "Stitching Point", code, domDict[code])
	print arcpy.GetMessages()

arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point")
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",1)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",2)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",3)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",4)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",5)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",6)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",7)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",8)
arcpy.AssignDomainToField_management("conductorjunction", "StitchingPoint", "Stitching Point",9)

arcpy.CreateDomain_management(geodatabaseConnection, "Communication Method", "Communication Method", "TEXT", "CODED")
domDict = {"RAD":"Radio", "CEL":"Cellular", "FIB":"Fibre", "HAR":"Hardwired", "NA":"Not Applicable", "UNK":"Unknown", "NO":"No Communication"}
for code in domDict:
	arcpy.AddCodedValueToDomain_management(geodatabaseConnection, "Communication Method", code, domDict[code])
	print arcpy.GetMessages()
	

arcpy.AddField_management("dynamicprotectivedevice", "ControlManufacturer", "TEXT", "", "", 25,"Control Manufacturer")
arcpy.AddField_management("dynamicprotectivedevice", "ControlCatNum", "TEXT", "", "", 25,"Control Catalog Number")
arcpy.AddField_management("dynamicprotectivedevice", "ControlSerialNum", "TEXT", "", "", 20,"Control Serial Number")
arcpy.AddField_management("dynamicprotectivedevice", "ControlDOM", "DATE", "", "", "","Control Date of Manufacture")
arcpy.AddField_management("dynamicprotectivedevice", "SCADAComms", "TEXT", "", "", 1,"SCADA Communications","NULLABLE","NON_REQUIRED","Yes or No")
arcpy.AddField_management("dynamicprotectivedevice", "EngineeringAccess", "TEXT", "", "", 1,"Engineering Access","NULLABLE","NON_REQUIRED","Yes or No")
arcpy.AddField_management("dynamicprotectivedevice", "CommMethod", "TEXT", "", "", 3,"Communication Method","NULLABLE","NON_REQUIRED","Communication Method")
arcpy.AddField_management("dynamicprotectivedevice", "Standalone", "TEXT", "", "", 1,"Standalone","NULLABLE","NON_REQUIRED","Yes or No")
arcpy.AddField_management("dynamicprotectivedevice", "AssessmentDate", "Date", "", "", "","AssessmentDate")

arcpy.env.workspace = geodatabaseConnection

arcpy.AddField_management("recloserunit", "LastMaintained", "Date", "", "", "","LastMaintained")
arcpy.AddField_management("recloserunit", "BypassFuseSize", "Long", 10, "", "","Bypass Fuse Size")
arcpy.AddField_management("recloserunit", "BypassNotes", "Text", "", "", 150,"Bypass Notes")

arcpy.CreateTable_management(geodatabaseConnection, "RecloserProtection")

arcpy.AddField_management("RecloserProtection", "DPDObjectID", "Long", 10, "", "", "Dynamic Protective Device ObjectID")
arcpy.AddField_management("RecloserProtection", "PhaseTrip", "Long", 10, "", "","Phase Trip Current")
arcpy.AddField_management("RecloserProtection", "TCCPhaseFast", "Text", "", "", 4,"Phase Fault Fast Curve")
arcpy.AddField_management("RecloserProtection", "TCCPhaseFastOps", "Long", 5, "", "","Phase Fault Fast Operations")
arcpy.AddField_management("RecloserProtection", "TCCPhaseSlow", "Text", "", "", 4,"Phase Fault Slow Curve")
arcpy.AddField_management("RecloserProtection", "TCCPhaseSlowOps", "Long", 5, "", "","Phase Fault Slow Operations")
arcpy.AddField_management("RecloserProtection", "GroundTrip", "Long", 10, "", "","Ground Trip Current")
arcpy.AddField_management("RecloserProtection", "TCCGroundFast", "Text", "", "", 4,"Ground Fault Fast Curve")
arcpy.AddField_management("RecloserProtection", "TCCGroundFastOps", "Long", 5, "", "","Ground Fault Fast Operations")
arcpy.AddField_management("RecloserProtection", "TCCGroundSlow", "Text", "", "", 4,"Ground Fault Slow Curve")
arcpy.AddField_management("RecloserProtection", "TCCGroundSlowOps", "Long", 5, "", "","Ground Fault Slow Operations")

arcpy.CreateRelationshipClass_management("gis.electric\\gis.dynamicprotectivedevice", "gis.recloserprotection", "GIS.DynProtDev_RecloserProt", "COMPOSITE", "Recloser Protection", "Recloser", "NONE", "ONE_TO_MANY", "NONE", "OBJECTID", "DPDObjectID")

