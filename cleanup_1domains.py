__author__ = "Tim Dine"
__version__ = "0.1"
__email__ = "timdine@hotmail.com"
__status__ = "Sample"

import arcpy
import re

arcpy.env.workspace = r"PathToGeodatabase"

fcList = arcpy.ListFeatureClasses() + arcpy.ListTables()

for fc in fcList:
	print "--------------------------------------"
	print fc
	theFields = arcpy.ListFields(fc)
	for field in theFields:
		if (field.domain):
			match = re.search('_[0-9]',field.domain)
			if match != None:
				try:
					print "Assigning", field.domain[:-2], "to", fc, field.name
					arcpy.AssignDomainToField_management(fc, field.name, field.domain[:-2])
				except:
					print "Error", arcpy.GetMessages()
	
#Optional Enhancements	
#Add code for if the domain doesn't exist, export out the existing domain and reimport in the new name
#Add code to remove the domains if they are no longer used.