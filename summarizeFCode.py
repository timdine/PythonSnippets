import arcpy
import os

def listFcsInGDB(gdb):
	''' list all Feature Classes in a geodatabase, including inside Feature Datasets '''
	arcpy.env.workspace = gdb
	print 'Processing ', arcpy.env.workspace

	fcs = []

	for table in arcpy.ListTables():
		fcs.append(table)

	
	for fds in arcpy.ListDatasets('','feature') + ['']:
		print "-Processing", fds
		for fc in arcpy.ListFeatureClasses('','',fds):
			#yield os.path.join(fds, fc)
			fcs.append(os.path.join(fds, fc))
		
	return fcs

FCODEList = []
theFCList = listFcsInGDB(r"GeodatabasePath")
theFCList.sort()
print theFCList
for fc in theFCList:
	print fc
	fields = arcpy.ListFields(fc)

	for field in fields:
		if field.name == "FCODE":
			print "--", fc, field.name
			with arcpy.da.SearchCursor(fc, ['FCODE']) as cursor:
				for row in cursor:
					if (row[0] not in FCODEList):
						FCODEList.append(row[0])
	
	#print FCODEList
	
FCODEList.sort()
for item in FCODEList:
	print item