import time
from urllib2 import urlopen

urlList = []
#urlList.append(["Scripted Service", r"http://emagissvr01/ArcGIS/rest/services/OutageServiceToolbox/GPServer/outageSummaryScript/execute"])
#urlList.append(["Original Service",r'http://emagissvr01/ArcGIS/rest/services/OutageServiceToolboxRebuild/GPServer/getOutageStats_originalDev/execute'])
#urlList.append(["Modified Service",r'http://emagissvr01/ArcGIS/rest/services/OutageServiceToolboxRebuild/GPServer/getOutageStats_modifiedDev/execute'])

#urlList.append(["Scripted Service", r"http://emaapp19/ArcGIS/rest/services/OutageServiceToolboxRebuildDev/GPServer/outageSummaryScriptProd/execute"])
#urlList.append(["Account Number Query", r"http://emagissvr01/ArcGIS/rest/services/customerLocation/MapServer/0/query?text=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&objectIds=&where=accountnumber+%3D+%271158284%27&time=&returnCountOnly=false&returnIdsOnly=false&returnGeometry=true&maxAllowableOffset=&outSR=&outFields=&f=html"])

#urlList.append(["Optimized Outages", r"http://emagisrr01/arcgis/rest/services/OutagesAndAbnormalProd_opt/MapServer/export?size=1440%2C760&format=png24&f=image&transparent=true&dpi=96&bboxSR=102100&%5Fts=1362513834068&imageSR=102100&bbox=%2D7449399%2E534219122%2C5443434%2E39868965%2C%2D6568844%2E968373934%2C5908171%2E5306635"])
urlList.append(["Regular Outages", r"http://emagisrr01/arcgis/rest/services/OutagesAndAbnormalProd/MapServer/export?size=1440%2C760&format=png24&f=image&transparent=true&dpi=96&bboxSR=102100&%5Fts=1362513834068&imageSR=102100&bbox=%2D7449399%2E534219122%2C5443434%2E39868965%2C%2D6568844%2E968373934%2C5908171%2E5306635"])

theLoops = range(5)


for theURL in urlList:
	theTimes = []
	print theURL[0]
	for i in theLoops:
		startTime = time.time()
		try:
			page = urlopen(theURL[1])
		except Exception,e:
			print str(e)
		stopTime = time.time()
		theTime = stopTime - startTime
		theTimes.append(theTime)
		print round(theTime,2)
	print "Average Time:", round(sum(theTimes) / float(len(theTimes)),2)