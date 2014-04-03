#!/usr/bin/env python

"""schemaUpdatesFeb2014.py: Makes a number of schema updates to the geodatabase.  Fields are needed to support new functionality."""


__author__      = "Tim Dine"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Development"

import arcpy

geodatabaseConnection = r'Database Connections\gis@gisprd01.sde'
arcpy.env.workspace = geodatabaseConnection + "\\GIS.Electric"



#Many - MaxOperatingVoltage

#DPD - RecloserProtectionFields


print "Conductor"

#PriOH - rDC20
arcpy.AddField_management("PriOHElectricLineSegment", "rDC20", "DOUBLE", "5", "2", "","Reduced Capacity", "NULLABLE", "NON_REQUIRED", "")

#PriOH - ConductorConfiguration
#ConductorConfiguration
#PriOH - thermalConstantCool
arcpy.AddField_management("Transformer", "thermalConstantCool", "LONG", "4", "0", "","Thermal Constant Cool", "NULLABLE", "NON_REQUIRED", "")
#PriOH - thermalConstantHeat
arcpy.AddField_management("Transformer", "thermalConstantHeat", "LONG", "4", "0", "","Thermal Constant Heat", "NULLABLE", "NON_REQUIRED", "")
#PriOH - allowedTemperature
arcpy.AddField_management("PriOHElectricLineSegment", "allowedTemperature", "LONG", "4", "0", "","Allowed Temperature", "NULLABLE", "NON_REQUIRED", "")
#PriUG - rDC20
arcpy.AddField_management("PriUGElectricLineSegment", "rDC20", "DOUBLE", "5", "2", "","Reduced Capacity", "NULLABLE", "NON_REQUIRED", "")

print "Transformers"

#Transformers - PhaseShift
arcpy.AddField_management("Transformer", "phaseShift", "DOUBLE", "5", "2", "","Phase Shift", "NULLABLE", "NON_REQUIRED", "")
#VoltageRegulator - PhaseShift
arcpy.AddField_management("VoltageRegulator", "phaseShift", "DOUBLE", "5", "2", "","Phase Shift", "NULLABLE", "NON_REQUIRED", "")

print "Switch"

#Switch - MaxInterruptingCurrent
arcpy.AddField_management("Switch", "MaxInterruptingCurrent", "DOUBLE", "38", "8", "","Maximum Interrupting Current", "NULLABLE", "NON_REQUIRED", "")
#Switch - isolating
arcpy.AddField_management("Switch", "isolating", "TEXT", "", "", "1","Isolating", "NULLABLE", "NON_REQUIRED", "Yes or No")

print "DPD"

#DPD - currentLimit
#Already Added
#DPD - lockoutTripCount
#Already Added
#DPD - isolating
arcpy.AddField_management("DynamicProtectiveDevice", "isolating", "TEXT", "", "", "1","Isolating", "NULLABLE", "NON_REQUIRED", "Yes or No")
#DPD - openingTime
arcpy.AddField_management("DynamicProtectiveDevice", "openingTime", "DOUBLE", "10", "8", "","Opening Time", "NULLABLE", "NON_REQUIRED", "")
#DPD - interruptionTime
arcpy.AddField_management("DynamicProtectiveDevice", "interruptionTime", "DOUBLE", "10", "8", "","Interruption Time", "NULLABLE", "NON_REQUIRED", "")
#DPD - peakCurrent
arcpy.AddField_management("DynamicProtectiveDevice", "peakCurrent", "LONG", "8", "", "","Peak Current", "NULLABLE", "NON_REQUIRED", "")  ##250000A
#DPD - thermalCurrent
arcpy.AddField_management("DynamicProtectiveDevice", "thermalCurrent", "LONG", "8", "", "","Thermal Current", "NULLABLE", "NON_REQUIRED", "")  ##50000A

print "Fuse"

#Fuse - isolating
arcpy.AddField_management("Fuse", "isolating", "TEXT", "", "", "1","Isolating", "NULLABLE", "NON_REQUIRED", "Yes or No")

print "OpenPoint"

#OpenPoint - isolating
arcpy.AddField_management("OpenPoint", "isolating", "TEXT", "", "", "1","Isolating", "NULLABLE", "NON_REQUIRED", "Yes or No")

print "PFCE"

#PFCE - ratedCurrent
arcpy.AddField_management("PFCorrectingEquipment", "MaxContinuousCurrent", "DOUBLE", "38", "8", "","Interruption Time", "NULLABLE", "NON_REQUIRED", "")

print "Transformer"

#Transformer - oilMass
arcpy.AddField_management("Transformer", "oilMass", "LONG", "6", "0", "","Oil Mass", "NULLABLE", "NON_REQUIRED", "")
#Transformer - onafRating
arcpy.AddField_management("Transformer", "onafRating", "DOUBLE", "5", "2", "","onaf Rating", "NULLABLE", "NON_REQUIRED", "") ##Rename This Field
#Transformer - ofafRating
arcpy.AddField_management("Transformer", "ofafRating", "DOUBLE", "5", "2", "","ofaf Rating", "NULLABLE", "NON_REQUIRED", "") ##Rename This Field
#Transformer - hotSpotRise
arcpy.AddField_management("Transformer", "hotspotRise", "LONG", "4", "0", "","Hotspot Rise", "NULLABLE", "NON_REQUIRED", "")
#Transformer - copperMass
arcpy.AddField_management("Transformer", "copperMass", "LONG", "6", "0", "","Copper Mass", "NULLABLE", "NON_REQUIRED", "")
#Transformer - allowedTemperature
arcpy.AddField_management("Transformer", "allowedTemperature", "LONG", "4", "0", "","Allowed Temperature", "NULLABLE", "NON_REQUIRED", "")
#Transformer - ironMass
arcpy.AddField_management("Transformer", "ironMass", "LONG", "6", "0", "","Iron Mass", "NULLABLE", "NON_REQUIRED", "")
#Transformer - tapPercent
arcpy.AddField_management("Transformer", "tapPercent", "DOUBLE", "5", "2", "","Tap Percentage", "NULLABLE", "NON_REQUIRED", "")
#Transformer - numberOfTaps
arcpy.AddField_management("Transformer", "numberOfTaps", "LONG", "3", "0", "","Number of Taps", "NULLABLE", "NON_REQUIRED", "")
#Transformer - normalTap
arcpy.AddField_management("Transformer", "normalTap", "LONG", "3", "0", "","Normal Tap", "NULLABLE", "NON_REQUIRED", "")
#Transformer - neutralTap
arcpy.AddField_management("Transformer", "neutralTap", "LONG", "3", "0", "","Neutral Tap", "NULLABLE", "NON_REQUIRED", "")
#Transformer - grounded
arcpy.AddField_management("Transformer", "grounded", "TEXT", "", "", "1","Grounded", "NULLABLE", "NON_REQUIRED", "Yes or No")
#Transformer - RatedU2
arcpy.AddField_management("Transformer", "RatedU2", "LONG", "10", "0", "","RatedU2", "NULLABLE", "NON_REQUIRED", "")
#Transformer - VoltageIndex
arcpy.AddField_management("Transformer", "VoltageIndex", "LONG", "10", "0", "","Voltage Index", "NULLABLE", "NON_REQUIRED", "")

print "Winding Test"

arcpy.env.workspace = geodatabaseConnection

#WindingTest - 
arcpy.CreateTable_management(geodatabaseConnection, "Catalog_WindingTest")
arcpy.AddField_management("Catalog_WindingTest", "RATEDS", "LONG", "10", "", "","RatedS", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "PHASES", "LONG", "10", "", "","Phases", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "TYPE", "TEXT", "", "", "4","Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "NOLOADLOSS", "DOUBLE", "5", "3", "","No Load Loss", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "LOADLOSS", "DOUBLE", "5", "3", "","Load Loss", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "EXCITINGCURRENT", "DOUBLE", "5", "3", "","Exciting Current", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "LEAKAGEIMPEDANCE", "DOUBLE", "5", "3", "","Leakage Impedance", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "LEAKAGEIMPEDANCE0", "DOUBLE", "5", "3", "","Leakage Impedance 0", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "MINLEAKAGEIMPEDANCE", "DOUBLE", "5", "3", "","Min Leakage Impedance", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WindingTest", "MAXLEAKAGEIMPEDANCE", "DOUBLE", "5", "3", "","Max Leakage Impedance", "NULLABLE", "NON_REQUIRED", "")

print "Wire Position"

#WirePosition - 
arcpy.CreateTable_management(geodatabaseConnection, "Catalog_WirePosition")
arcpy.AddField_management("Catalog_WirePosition", "ConductorConfiguration", "TEXT", "", "", "50","Conductor Configruation", "NULLABLE", "NON_REQUIRED", "Conductor Configuration")
arcpy.AddField_management("Catalog_WirePosition", "Position", "SHORT", "2", "", "","Position", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WirePosition", "OffsetX", "DOUBLE", "6", "2", "","Offset X", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_WirePosition", "OffsetY", "DOUBLE", "6", "2", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")

print "Wire Catalog"

#WireLine - 
arcpy.CreateTable_management(geodatabaseConnection, "Catalog_Line")
arcpy.AddField_management("Catalog_Line", "LineType", "TEXT", "", "", "50","LineType", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "CrossSection", "DOUBLE", "20", "10", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "B0CH", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "BCH", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "R", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "R0", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "X", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "X0", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "GMR", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")
arcpy.AddField_management("Catalog_Line", "RATEDCURRENT", "DOUBLE", "20", "12", "","Offset Y", "NULLABLE", "NON_REQUIRED", "")

arcpy.env.workspace = geodatabaseConnection + "\\GIS.Electric"

print "Fault Indicator"

#FaultIndicator - IndicatorType
arcpy.AddField_management("MiscNetworkFeature", "indicatorType", "TEXT", "", "", "12","Indicator Type", "NULLABLE", "NON_REQUIRED", "")
#FaultIndicator - Directional
arcpy.AddField_management("MiscNetworkFeature", "directional", "TEXT", "", "", "1","Directional", "NULLABLE", "NON_REQUIRED", "Yes or No")

arcpy.CreateDomain_management(geodatabaseConnection, "FaultIndicatorType", "Fault Indicator Type", "TEXT", "CODED")

domDict = {"overcurrent":"Over Current", "undervoltage":"Under Voltage"}
for code in domDict:
	arcpy.AddCodedValueToDomain_management(geodatabaseConnection, "FaultIndicatorType", code, domDict[code])
	print arcpy.GetMessages()

print "Generator"
	
#Generator - FaultContribution
arcpy.AddField_management("Generator", "faultContribution", "DOUBLE", "5", "2", "","Fault Contribution", "NULLABLE", "NON_REQUIRED", "FaultIndicatorType")
#Generator - Grounded
arcpy.AddField_management("Generator", "grounded", "TEXT", "", "", "1","Grounded", "NULLABLE", "NON_REQUIRED", "Yes or No")
#Generator - UnitCount
arcpy.AddField_management("Generator", "unitCount", "LONG", "3", "", "","Unit Count", "NULLABLE", "NON_REQUIRED", "")
#Generator - PhaseDesignation
arcpy.AddField_management("Generator", "phaseDesignation", "Long", "10", "", "","Phase Designation", "NULLABLE", "NON_REQUIRED", "PhaseDesignation - Master List")
#Generator - Efficiency
arcpy.AddField_management("Generator", "efficiency", "Double", "5", "2", "","Efficiency", "NULLABLE", "NON_REQUIRED", "")

print "Feeder Descriptions"

arcpy.CreateTable_management(geodatabaseConnection, "FeederDescriptions")

arcpy.env.workspace = geodatabaseConnection

#FeederDescriptions - FeederNum
arcpy.AddField_management("FeederDescriptions", "FeederNum", "TEXT", "", "", "30","FeederNum", "NULLABLE", "NON_REQUIRED", "")
#FeederDescriptions - Description
arcpy.AddField_management("FeederDescriptions", "Description", "TEXT", "", "", "650","Description", "NULLABLE", "NON_REQUIRED", "")




