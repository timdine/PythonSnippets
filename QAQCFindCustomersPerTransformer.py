import arcpy

class customer:
    def __init__(self, premiseid, lastname, firstname, middleinitial, route, stop, serviceaddress, streetnumber, fraction, prefix, street, suffix, direction, apartment, city, province, postalcode):
        self.premiseid = premiseid
        self.lastname = lastname
        self.firstname = firstname
        self.middleinitial = middleinitial
        self.route = route
        self.stop = stop
        self.serviceaddress = serviceaddress
        self.streetnumber = streetnumber
        self.fraction = fraction
        self.prefix = prefix
        self.street = street
        self.suffix = suffix
        self.direction = direction
        self.apartment = apartment
        self.city = city
        self.province = province
        self.postalcode = postalcode

class transformer:
	def __init__(self, txoid, kva, customercount, spoidlist):
		self.txoid = txoid
		self.kva = kva
		self.customercount = customercount
		self.spoidlist = spoidlist
		
class servicepoint:
	def __init__(self, spoid, txoid):
		self.spoid = spoid
		self.txoid = txoid

geodatabaseConnection = r'Database Connections\gis@gisprd01.sde'
arcpy.env.workspace = geodatabaseConnection


print "Loading ServicePoint_CISTable..."
theCustDict = {}
checkedRows = 0
searchFields = ["SERVICEPOINTOBJECTID"]
with arcpy.da.SearchCursor("GIS.ServicePoint_CISTable", searchFields) as cursor:
	for row in cursor:
		checkedRows += 1
		if (checkedRows % 10000 == 0):
			print "Checked", checkedRows
		if not row[0] in theCustDict:
			theCustDict[row[0]] = 1
		else:
			theCustDict[row[0]] += 1


arcpy.env.workspace = geodatabaseConnection + "\\GIS.Electric"

print "Loading Transformers..."
checkedRows = 0
txDict = {}
searchFields = ["ObjectID", "RATEDKVA"]
with arcpy.da.SearchCursor("GIS.Transformer", searchFields) as cursor:
	for row in cursor:
		checkedRows += 1
		if (checkedRows % 10000 == 0):
			print "Checked", checkedRows
		theTx = transformer(row[0], row[1], 0, [])
		if not row[0] in txDict:
			txDict[row[0]] = theTx

print "Loading ServicePoints..."
searchFields = ["ObjectID", "TransformerObjectID"]
with arcpy.da.SearchCursor("GIS.ServicePoint", searchFields) as cursor:
	for row in cursor:
		checkedRows += 1
		if (checkedRows % 10000 == 0):
			print "Checked", checkedRows
		theSP = servicepoint(row[0], row[1])
		if (theSP.txoid in txDict):
			if (theSP.spoid in theCustDict):
				txDict[theSP.txoid].customercount += theCustDict[theSP.spoid]
				txDict[theSP.txoid].spoidlist.append(theSP.spoid)


print "TxOID, RatedkVA, CustomerCount"
for key, value in txDict.iteritems():
	print key, ",", value.kva, ",", value.customercount


			