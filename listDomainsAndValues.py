import arcpy
arcpy.env.overwriteOutput = True
theWorkspace = ""
desc = arcpy.Describe(theWorkspace)
for theDomain in desc.domains:
	if "fcode" in theDomain:
		print "---------------"
		print theDomain
		arcpy.DomainToTable_management(theWorkspace, theDomain, "in_memory/aDomain", "code", "desc")
		cursor = arcpy.da.SearchCursor("in_memory/aDomain", ["code", "desc"])
		for row in cursor:
			print row[0], row[1]