#!/usr/bin/env python

"""loadProvincialRecloserList.py: ."""

__author__      = "Tim Dine"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Development"

import arcpy

class dpd:
    def __init__(self, deviceid, kv, dccremotecontrol, engineeringremotecontrol, scada, standalone, assessmentdate, lastmaintained, holdoffrequirement, switchconfig, bypassavailability, bypassrequirement,
    devicetype, manufacturer, devicemodel, devicesn, devicecatnum, devicedom, tripcount, maxamp, maxinterrupt, bil, weight, controltype, controllersn, controllercatnum, controllerdom, coilsize, phasetriplevel,
    phasefastcurve, fastphaseop, phaseslowcurve, phaseslowop, groundtriplevel, groundfastcurve, groundfastop, groundslowcurve, groundslowop, engineeringnotes):
        self.deviceid = deviceid
        self.kv = kv
        self.dccremotecontrol = dccremotecontrol
        self.engineeringremotecontrol = engineeringremotecontrol
        self.scada = scada
        self.standalone = standalone
        self.assessmentdate = assessmentdate
        self.lastmaintained = lastmaintained
        self.holdoffrequirement = holdoffrequirement
        self.switchconfig = switchconfig
        self.bypassavailability = bypassavailability
        self.bypassrequirement = bypassrequirement
        self.devicetype = devicetype
        self.manufacturer = manufacturer
        self.devicemodel = devicemodel
        self.devicesn = devicesn
        self.devicecatnum = devicecatnum
        self.devicedom = devicedom
        self.tripcount = tripcount
	self.maxamp = maxamp
	self.maxinterrupt = maxinterrupt
	self.bil = bil
	self.weight = weight
	self.controltype = controltype
	self.controllersn = controllersn
	self.controllercatnum = controllercatnum
	self.controllerdom = controllerdom
	self.coilsize = coilsize
	self.phasetriplevel = phasetriplevel
	self.phasefastcurve = phasefastcurve
	self.fastphaseop = fastphaseop
	self.phaseslowcurve = phaseslowcurve
	self.phaseslowop = phaseslowop
	self.groundtriplevel = groundtriplevel
	self.groundfastcurve = groundfastcurve
	self.groundfastop = groundfastop
	self.groundslowcurve = groundslowcurve
	self.groundslowop = groundslowop
	self.engineeringnotes = engineeringnotes

geodatabaseConnection = r'Database Connections\gis@gisprd01.sde'
arcpy.env.workspace = geodatabaseConnection + ""

recList = r'C:\temp\temp.gdb\provrecllist'
recFields = ['Device_ID','kV','DCC_Remote_Control',
'Engineering_Remote_Control','SCADA','StandAlone',
'Assesment_Date','Last_Maintained','Hold_Off_Requirement',
'Switch_config','By_Pass_Availability','By_pass_Requirement',
'Device_Type','Manufacturer','Device_Model',
'Device_SN','Device_CAT_Num','Device_DOM',
'Trip_Count','Max_Amp','Max_Interrupt','BIL',
'Weight','Control_Type','Controller_SN',
'Controller_CAT_Num','Controller_DOM','Coil_Size',
'Phase_Trip_Level','Phase_Fast_Curve','Fast_Phase_Op_',
'Phase_Slow_Curve','Phase_Slow_Op_','Ground_Trip_Level',
'Ground_Fast_Curve','Ground_Fast_Op_','Ground_Slow_Curve',
'Ground_Slow_Op_','Engineering_Notes']

recloserSheets = {}

with arcpy.da.SearchCursor(recList, recFields) as cursor:
	for row in cursor:
		#print ("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
		deviceid = row[0]
		kv = row[1]
		dccremotecontrol = row[2]
		
		recloserSheets[row[0]] = dpd(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16],
		row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35],
		row[36], row[37], row[38])
		
gisFields = ['FACILITYID', 'OPERATINGVOLTAGE', 'ENGINEERINGACCESS','STANDALONE','ASSESSMENTDATE','BILRATING', 'MANUFACTURER', 'MODEL', 'SERIALNUMBER', 'COILSIZE', 
'CONTROLMANUFACTURER','CONTROLCATNUM','CONTROLSERIALNUM','CONTROLDOM','SCADACOMMS','COMMMETHOD','TRIPCOUNT','MAXCONTINUOUSCURRENT','MAXINTERRUPTINGCURRENT',
'MANUFACTUREDATE'
]

#'LASTMAINTAINED' 'HOLDOFFREQUIREMENT'

with arcpy.da.SearchCursor("gis.DynamicProtectiveDevice", gisFields) as cursor:
	for row in cursor:
		print "-----"
		if row[0] in recloserSheets.keys():
			print "FacilityID", row[0], recloserSheets[row[0]].deviceid
			##print "Operating Voltage", row[1], recloserSheets[row[0]].kv ##We are making the assumption that the operating voltage in GIS is already correct
			print "Engineering Access", row[2], recloserSheets[row[0]].engineeringremotecontrol
			print "Standalone", row[3], recloserSheets[row[0]].standalone
			print "Assessment Date", row[4], recloserSheets[row[0]].assessmentdate
			print "BIL", row[5], recloserSheets[row[0]].bil
			print "Manufacturer", row[6], recloserSheets[row[0]].manufacturer
			print "Model", row[7], recloserSheets[row[0]].devicemodel
			print "Serial Number", row[8], recloserSheets[row[0]].devicesn
			print "Coil Size", row[9], recloserSheets[row[0]].coilsize
			print "Control Manufacturer", row[10], recloserSheets[row[0]].controllersn
			print "Control Cat Num", row[11], recloserSheets[row[0]].controllercatnum
			print "Control Serial Num", row[12], recloserSheets[row[0]].controllersn
			print "Control DOM", row[13], recloserSheets[row[0]].controllerdom
			print "SCADACOMMS", row[14], recloserSheets[row[0]].scada
			#print "Comm Method", row[15], recloserSheets[row[0]].commmethod
			print "Trip Count", row[16], recloserSheets[row[0]].tripcount
			print "MaxAmp", row[17], recloserSheets[row[0]].maxamp
			print "MaxInterrupt", row[18], recloserSheets[row[0]].maxinterrupt
			print "Device DOM", row[19], recloserSheets[row[0]].devicedom
			
			#print "DCC Remote Control", row[14], recloserSheets[row[0]].scada
			#print "Last Maintained", row[14], recloserSheets[row[0]].scada
			#print "Holdoff Requirement", row[14], recloserSheets[row[0]].scada
			#print "Switch Config", row[14], recloserSheets[row[0]].scada
			#print "Bypass Availability", row[14], recloserSheets[row[0]].scada
			#print "Device Cat Num", row[14], recloserSheets[row[0]].scada
			
			
			
			#print "Weight", row[14], recloserSheets[row[0]].scada
			#print "Control Type", row[14], recloserSheets[row[0]].scada
			#print "EngineeringNotes", row[14], recloserSheets[row[0]].scada
			

			
			protectionFields = ['PHASETRIP','TCCPHASEFAST','TCCPHASEFASTOPS','TCCPHASESLOW','TCCPHASESLOWOPS','GROUNDTRIP',
			'TCCGROUNDFAST','TCCGROUNDFASTOPS','TCCGROUNDSLOW','TCCGROUNDSLOWOPS']
			with arcpy.da.SearchCursor("GIS.RecloserProtection", protectionFields) as protectioncur:
				for protrow in protectioncur:
					print protrow
			
		else:
			print "Error", row[0]