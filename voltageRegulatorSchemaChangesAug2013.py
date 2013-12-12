#!/usr/bin/env python

"""schemaUpdatesJuly2013.py: Makes a number of schema updates to the geodatabase.  Fields are needed to support new functionality."""


__author__      = "Tim Dine"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Development"

import arcpy

geodatabaseConnection = r'Database Connections\gis@gisdev01_dg.sde'
arcpy.env.workspace = geodatabaseConnection + "\\GIS.Electric"

#~ domDict = {"131":"131", "271":"271", "300":"300"}
#~ for code in domDict:
	#~ arcpy.AddCodedValueToDomain_management(geodatabaseConnection, "VolRegNominalAmpRating", code, domDict[code])
#~ print "Creating Domain"
#~ arcpy.CreateDomain_management(geodatabaseConnection, "Voltage Regulator Unit RatedKVA", "VoltageRegulatorUnit RatedKVA", "DOUBLE", "CODED")
	
#~ domDict = {"0":"0","18":"18", "19":"19", "24":"24", "28.1":"28.1", "36":"36", "38":"38", "38.1":"38.1", "38.5":"38.5", "48":"48","50":"50", "57":"57", "72":"72", "75":"75", "76":"76", "76.2":"76.2",
		#~ "90":"90", "114":"114", "114.3":"114.3", "141":"141", "144":"144", "150":"150","152":"152", "156":"156", "157":"157", "167":"167","216":"216", "228":"228", "250":"250","288":"288", "300":"300","333":"333","432":"432",
		#~ "500":"500","501":"501", "684":"684", "864":"864", "1000":"1000","1200":"1200", "1296":"1296", "12000":"12000"}
#~ for code in domDict:
	#~ print "Adding", code
	#~ arcpy.AddCodedValueToDomain_management(geodatabaseConnection, "Voltage Regulator Unit RatedKVA", code, domDict[code])
	#~ print arcpy.GetMessages()
	
##Ensure the calculate is done on the appropriate version.	
	
arcpy.env.workspace = geodatabaseConnection
#~ arcpy.AddMessage("Adding Field")
#~ arcpy.AddField_management("VoltageRegulatorUnit", "TempRatedKVA", "DOUBLE")
#~ arcpy.AddMessage("Calculating Field")
#~ arcpy.CalculateField_management("VoltageRegulatorUnit", "TempRatedKVA", "[RATEDKVA]")
#~ arcpy.AddMessage("Removing Field")
#~ arcpy.DeleteField_management("VoltageRegulatorUnit", "RATEDKVA")
#~ arcpy.AddField_management("VoltageRegulatorUnit", "RATEDKVA", "DOUBLE")
#~ arcpy.CalculateField_management("VoltageRegulatorUnit", "RATEDKVA", "[TempRatedKVA]")
#~ arcpy.DeleteField_management("VoltageRegulatorUnit", "TempRatedKVA")

##Make sure to reassign ArfFM Rated KVA Field model name.
	
arcpy.AssignDomainToField_management("VoltageRegulatorUnit", "RATEDKVA", "Voltage Regulator Unit RatedKVA")
arcpy.AssignDomainToField_management("VoltageRegulatorUnit", "RATEDKVA", "Voltage Regulator Unit RatedKVA",1)