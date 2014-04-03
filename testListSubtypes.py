import arcpy
arcpy.env.workspace = r"Database Connections\gis@gisprd01.sde\electric"

for fc in arcpy.ListFeatureClasses():
	try:
		subtypes = arcpy.da.ListSubtypes(fc)
		for stcode in subtypes.keys():
			#print stcode
			stvalues = subtypes[stcode]
			for infos in stvalues.keys():
				if infos == "Name":
					print fc, "-", stvalues[infos]
			
			#for st in stdict.keys():
			#	if stkey == "Name":
			#		print stdict[stkey]
	except:
		print "Error"
			
