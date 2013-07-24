import arcpy
import os

theIC = c = arcpy.da.InsertCursor(r"C:\Data\ExtentPolygons.gdb\ExtentPolygons", ("SCALE", "ScaleNum", "SHAPE@"))

logDirectory = "c:\\temp\\IISLogs2\\"

files_in_dir = os.listdir(logDirectory)
for file_in_dir in files_in_dir:
	print file_in_dir
	f = open(logDirectory+file_in_dir,"r")
	for line in f:
		try:
			if ("NSPI_ElectricDistribution" in line and "&bbox=" in line and "&size=" in line):
				startbbox = line.find('&bbox=')+6
				nextAmp = line.find('&',startbbox)
				nextSpace = line.find(' ',startbbox)
				stopPoint = nextAmp
				if (nextAmp == -1):
					stopPoint = nextSpace
				#print nextAmp
				extents = line[startbbox:stopPoint].replace("%2D","-").replace("%2C",",").replace("%2E",".").split(",")
				#print extents
				
				mapWidth = float(extents[2]) - float(extents[0])
				#print mapWidth
				
				
				#3779.5 pixels / meter
				
				startSize = line.find('&size=')+6
				nextAmp = line.find('&',startSize)
				nextSpace = line.find(' ',startSize)
				stopPoint = nextAmp
				if (nextAmp == -1):
					stopPoint = nextSpace
				size = line[startSize:stopPoint].replace("%2C",",").split(',')
				
				screenWidthInMeters = float(size[0])/3779
				scale = mapWidth / screenWidthInMeters
				
				#print scale
				
				#&size=1655%2C765
				
				array = arcpy.Array([arcpy.Point(extents[0], extents[1]),arcpy.Point(extents[0], extents[3]),arcpy.Point(extents[2],extents[3]),arcpy.Point(extents[2],extents[1])])
				polygon = arcpy.Polygon(array)
				
				c.insertRow([str(scale),float(scale),polygon])
		except Exception,e:
			print str(e)
