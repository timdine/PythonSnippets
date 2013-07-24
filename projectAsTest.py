import arcpy
theFC = r"c:\data\UTM_1km_21n_U_Project.shp"
g = arcpy.Geometry()
to_sr = arcpy.SpatialReference('WGS 1984')

geometryList = arcpy.CopyFeatures_management(theFC, g)
for geometry in geometryList:
	projectedGeometry = geometry.projectAs(to_sr,r'NAD_1983_HARN_To_WGS_1984')
	#projectedGeometry = geometry.projectAs(to_sr,'NAD_1983_To_NAD_1983_CSRS_4 + NAD_1983_CSRS_To_WGS_1984_2')
	
	print projectedGeometry.centroid.X, projectedGeometry.centroid.Y
	