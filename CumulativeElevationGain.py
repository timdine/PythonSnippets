#!/usr/bin/env python

"""CumulativeElevationGain.py: Calculates the cumulative elevation gain of a 3D feature class.  Used for calculating vertical of a hiking route."""

__author__      = "Tim Dine"
#__copyright__ = "Copyright 2013"
#__credits__ = []
#__license__ = ""
#__version__ = "1.0.1"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Experimental"


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
