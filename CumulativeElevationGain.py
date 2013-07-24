import arcpy

inFC = r"C:\Data\GrosMorneDEM\DEM.gdb\RouteWithZ_interp"
SR = arcpy.Describe(inFC).spatialReference

array = arcpy.da.FeatureClassToNumPyArray(inFC,["SHAPE@Z"], spatial_reference=SR, explode_to_points=True)

totalElevationGain = 0

for i in range(array.size):
	if i > 0:
		if array[i][0] > array[i-1][0]:
			print array[i][0], array[i-1][0]
			totalElevationGain += (array[i][0] - array[i-1][0])
print totalElevationGain
