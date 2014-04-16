import operator
import glob
#import parse

errorsDicOriginal = {}
#~ errorsDic["Skipping bad polyline geometry"] = "Skipping bad polyline geometry for GIS.{featureclass}.{fcoid}."
#~ errorsDic["FindValue encountered a nonunique"] = "FindValue encountered a nonunique {fieldname} following {relatedTable}.{relatedField} from {featureclass}.{id}"
#~ errorsDic["The Map"] = "The Map {mapname} does not map the value {mapvalue}, and the Map has no default. Using the unmapped value."
#~ errorsDic["FindValue found no "] = "FindValue found no {relatedrecord} following a {thefeatureclass} from {id}"
#~ errorsDic["Found no"] = "Found no {relatedrecord} from {featureclass}.{id}"
#~ errorsDic["Key"] = "Key {lookup} not found in lookup table {table}"

errorsDicOriginal["Skipping bad polyline geometry for GIS.SecOHElectricLineSegment"] = 0
errorsDicOriginal["FindValue encountered a nonunique PhaseDesignation following ServicePoint.Connected.PhaseDesignation from CISTable"] = 0
errorsDicOriginal["The Map NspConductorMaterial does not map the value NK, and the Map has no default. Using the unmapped value."] = 0
errorsDicOriginal["FindValue found no CONDUCTORINFO following a SecOHElectricLineSegment from"] = 0
errorsDicOriginal["Found no Connected from ServicePoint"] = 0
errorsDicOriginal["Found no TRANSFORMERUNIT from Transformer"] = 0
errorsDicOriginal["Key [37.5,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["FindValue found no Transformer following a Transformer from "] = 0
errorsDicOriginal["FindValue encountered a nonunique PhaseDesignation following CONDUCTORINFO.ConductorMaterial from SecOHElectricLineSegment"] = 0
errorsDicOriginal["FindValue encountered a nonunique PhaseDesignation following CONDUCTORINFO.ConductorSize from SecOHElectricLineSegment"] = 0
errorsDicOriginal["The Map NspConductorMaterial does not map the value Null, and the Map has no default. Using the unmapped value"] = 0
errorsDicOriginal["FindValue found no CONDUCTORINFO following a PriOHElectricLineSegment from "] = 0
errorsDicOriginal["Mandatory field SECTIONALIZERUNIT.NAUNIQUEID not found by following relationships from DynamicProtectiveDevice object"] = 0
errorsDicOriginal["Mandatory field Fuse.FeederID2 is Null on Fuse object"] = 0
errorsDicOriginal["Mandatory field Fuse.MAXCONTINUOUSCURRENT is Null on Fuse object "] = 0
errorsDicOriginal["Mandatory field Fuse.GANGOPERATED is Null on Fuse"] = 0
errorsDicOriginal["Mandatory field NOMINALVOLTAGE is Null on Generator"] = 0
errorsDicOriginal["Did not create an object of the CIM class cim:DistributedGenerator, because the mandatory property tdms:ConductingEquipment.ratedVoltage"] = 0
errorsDicOriginal["Mandatory field DynamicProtectiveDevice.COILSIZE is Null on DynamicProtectiveDevice"] = 0
errorsDicOriginal["A Multiply operand must be numeric"] = 0
errorsDicOriginal["Key [30,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [150,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [1000,1,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [1000,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["ValidateFeederModel: 1 terminals are not connected to the rest of the network."] = 0
errorsDicOriginal["Mandatory field GANGOPERATED is Null on Switch"] = 0
errorsDicOriginal["Mandatory field Switch.FeederID2 is Null on Switch"] = 0
errorsDicOriginal["Mandatory field Switch.MAXCONTINUOUSCURRENT is Null on Switch"] = 0
errorsDicOriginal["Key [112.5,3,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["No FeederNum for circuit source  at Primary Overhead Electric Line Segment"] = 0
errorsDicOriginal["Key [112.5,3,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field FUSEUNIT.NAUNIQUEID not found by following relationships from Fuse"] = 0
errorsDicOriginal["Create DataSource: "] = 0
errorsDicOriginal["Export Feeder: "] = 0
errorsDicOriginal["User: "] = 0
errorsDicOriginal["Server: "] = 0
errorsDicOriginal["Instance: "] = 0
errorsDicOriginal["Version: "] = 0
errorsDicOriginal["Transform to CIM: "] = 0
errorsDicOriginal["Mandatory field GANGOPERATED is Null on Fuse "] = 0
errorsDicOriginal["Mandatory field MAXCONTINUOUSCURRENT is Null on Fuse object "] = 0
errorsDicOriginal["Mandatory field PhaseDesignation is Null on CONDUCTORINFO"] = 0
errorsDicOriginal["Mandatory field PhaseDesignation is Null on TRANSFORMERUNIT "] = 0
errorsDicOriginal["Mandatory field Switch.GANGOPERATED is Null on Switch object "] = 0
errorsDicOriginal["Did not create an object of the CIM class cim:ACLineSegment, because the mandatory property tdms:ConductingEquipment.ratedVoltage could not be derived"] = 0
errorsDicOriginal["Key [10,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["[25,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field MAXCONTINUOUSCURRENT is Null on Switch object "] = 0
errorsDicOriginal["Mandatory field SWITCHUNIT.NAUNIQUEID not found by following relationships from Switch object"] = 0
errorsDicOriginal["Mandatory field DynamicProtectiveDevice.LOCKOUTTRIPCOUNT is Null on DynamicProtectiveDevice object"] = 0
errorsDicOriginal["Mandatory field DynamicProtectiveDevice.TRIPCURRENT is Null on DynamicProtectiveDevice object"] = 0
errorsDicOriginal["The Map NspConductorMaterial does not map the value HC, and the Map has no default. Using the unmapped"] = 0
errorsDicOriginal["Mandatory field COILSIZE is Null on DynamicProtectiveDevice object"] = 0
errorsDicOriginal["Mandatory field RECLOSERUNIT.NAUNIQUEID not found by following relationships from DynamicProtectiveDevice object"] = 0
errorsDicOriginal["Key [50,2,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [0,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [10,2,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [25,2,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [50,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [25,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [10,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [0,1,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field FEEDERNUM is Null on SecUGElectricLineSegment object"] = 0
errorsDicOriginal["Mandatory field FEEDERSECTIONID is Null on SecUGElectricLineSegment object"] = 0
errorsDicOriginal["Key [2000,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field FEEDERSECTIONID is Null on DynamicProtectiveDevice object"] = 0
errorsDicOriginal["Mandatory field RECLOSERUNIT.NAUNIQUEID not found by following relationships from DynamicProtectiveDevice object"] = 0
errorsDicOriginal["FindValue encountered a nonunique PhaseDesignation following CONDUCTORINFO.ConductorMaterial from PriOHElectricLineSegment"] = 0
errorsDicOriginal["FindValue encountered a nonunique PhaseDesignation following CONDUCTORINFO.ConductorSize from PriOHElectricLineSegment"] = 0
errorsDicOriginal["Mandatory field Kvar is Null on CAPACITORUNIT object"] = 0
errorsDicOriginal["Skipping bad polyline geometry for GIS.PriOHElectricLineSegment"] = 0
errorsDicOriginal["has more than one cim:ServiceLocation relationship"] = 0
errorsDicOriginal["The Map NspConductorMaterial does not map the value CUW, and the Map has no default. Using the unmapped value"] = 0
errorsDicOriginal["Mandatory field FEEDERNUM is Null on SecUGElectricLineSegment object "] = 0
errorsDicOriginal["Mandatory field FEEDERSECTIONID is Null on SecUGElectricLineSegment object"] = 0
errorsDicOriginal["Export complete: "] = 0
errorsDicOriginal["Skipping bad polyline geometry for GIS.SecUGElectricLineSegment"] = 0
errorsDicOriginal["Mandatory field PhaseDesignation is Null on ConductorJunction"] = 0
errorsDicOriginal["Mandatory field OPERATINGVOLTAGE is Null on OpenPoint object"] = 0
errorsDicOriginal["Mandatory field FEEDERNUM is Null on SecOHElectricLineSegment object"] = 0
errorsDicOriginal["Mandatory field FEEDERSECTIONID is Null on SecOHElectricLineSegment object"] = 0
errorsDicOriginal["FindValue found no CONDUCTORINFO following a SecUGElectricLineSegment"] = 0
errorsDicOriginal["Key [37.5,3,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [35,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [20,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [150,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [75,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["The Map NspConductorMaterial does not map the value AAC, and the Map has no default. Using the unmapped value."] = 0
errorsDicOriginal["Did not create an object of the CIM class cim:Disconnector, because the mandatory property cim:ConductingEquipment.phases could not be derived."] = 0
errorsDicOriginal["Mandatory field PhaseDesignation is Null on FUSEUNIT object"] = 0
errorsDicOriginal["Key [300,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [750,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field WORKDEPOT is Null on MiscNetworkFeature"] = 0
errorsDicOriginal["Key [3000,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field OPERATINGVOLTAGE is Null on MiscNetworkFeature"] = 0
errorsDicOriginal["Key [37,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [370,1,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [750,1,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [5000,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [1667,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [5000,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [750,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Inconsistent feeder nums "] = 0
errorsDicOriginal["Key [500,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [45,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["No FeederNum for circuit source"] = 0
errorsDicOriginal["Key [37.5,1,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [112,1,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [7500,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [2500,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field FeederID2 is Null"] = 0
errorsDicOriginal["Key [25000,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [0,3,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Mandatory field MAXINTERRUPTINGCURRENT is Null on Fuse object "] = 0
errorsDicOriginal["The operation 'Multiply' yielded null. Primary source is SecOHElectricLineSegment."] = 0
errorsDicOriginal["Key [3000,3,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [1000,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [335,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [330,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [337,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [0,3,UG] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Key [130,1,OH] not found in lookup table [Catalog_WindingTest:RATEDS,PHASES,TYPE]"] = 0
errorsDicOriginal["Error retrieving edge feature at junction Fuse"] = 0
errorsDicOriginal["Key [HOR,?] not found in lookup table [Catalog_WirePosition:CONDUCTORCONFIGURATION,POSITION]"] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0
#~ errorsDicOriginal[""] = 0

errorsDic = errorsDicOriginal.copy()

#errorsFoundDic = {}

print "FDR       , S,	M,	T1,	T2,	FN,	FS,	UK"

for file in glob.glob("C:\\ADMSExports\\*.log"):
	#print file
	infile = open(file,"r")
	fileErrorsDic = errorsDicOriginal.copy()
	errorsNotFound = 0
	disconnectedTerminals = 0
	terminalNoOther = 0
	ignoreLines = 0
	feedernumerror = 0
	feedersecterror = 0
	for line in infile:
		#~ if (ignoreLines == 1):
			#~ print line[0:3], line[0:4], line
		if (line[0:3] == "   "):
			#ignore line, you're in a terminals not connected
			disconnectedTerminals = disconnectedTerminals + 1
		elif (line[0:4] == "  > "):
			#ignore line, you're in terminals not connected to another terminal
			terminalNoOther = terminalNoOther + 1
		else:
			ignoreLines = 0
			#print line
			errorfound = 0
			for error in errorsDic.keys():
				if error in line:
					#print errorsDic[error]
					#parse(errorsDic[error], line)
					errorsDic[error] = errorsDic[error] + 1
					fileErrorsDic[error] = fileErrorsDic[error] + 1
					errorfound = 1
					
					if (("Mandatory field FEEDERNUM is Null on SecOHElectricLineSegment object" in error) or ("Mandatory field FEEDERSECTIONID is Null on SecOHElectricLineSegment object" in error)):
						feedernumerror = feedernumerror + 1
						feedersecterror = feedersecterror + 1
					
			if errorfound == 0:
				if ("ValidateFeederModel" in line and "terminals are not connected to the rest of the network." in line):
					ignoreLines = 1
					#print "Validate Feeder Model 1"
				elif ("ValidateFeederModel: These terminals are not connected to another terminal." in line):
					ignoreLines = 1
					#print "Validate Feeder Model 2"
				elif ("ValidateFeederModel: These equipment have more geometric connections than electrical connections or vice versa." in line):
					ignoreLines = 1
				elif ("\n" == line):
					test=""
				else:
					#print "error not found", line
					test = ""
					errorsNotFound = errorsNotFound + 1
				
	file_sorted_errors = sorted(fileErrorsDic.iteritems(), key=operator.itemgetter(1))
	errorsUnder20 = 0
	errorsOver20 = 0
	for error in file_sorted_errors:
		#print error[1], errorsUnder20, errorsOver20
		if error[1] > 20:
			errorsOver20 = errorsOver20 + error[1]
		else:
			errorsUnder20 = errorsUnder20 + error[1]
	#print "-----------------------------------------------------"
	print file.split("_")[0].replace("C:\\ADMSExports\\","") + ",	" + str(errorsUnder20) + ",	" + str(errorsOver20) + ",	"  + str(disconnectedTerminals) + ",	"  + str(terminalNoOther) + ",	"  + str(feedersecterror) + ",	" + str(feedernumerror) + ",	" + str(errorsNotFound)
	#print "-----------------------------------------------------"



sorted_errors = sorted(errorsDic.iteritems(), key=operator.itemgetter(1))
		
for error in sorted_errors:
	print error[1], error[0]