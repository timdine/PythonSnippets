import arcgisscripting
gp = arcgisscripting.create()

try:

    # Test input coords
    PointXcoord = -3000.00
    PointYcoord = 2000.00

    clon = 0.0
    prjIn = "PROJCS['Mars_Merc0',GEOGCS['GCS_Mars_2000_Sphere',DATUM['D_Mars_2000_Sphere',SPHEROID['Mars_2000_Sphere_IAU_IAG',3396190.0,0.0]],PRIMEM['Reference_Meridian',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',$clon],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]"
    srIn = gp.CreateSpatialReference(prjIn)

    clon = 54.4
    prjOut = "PROJCS['Mars_Merc0',GEOGCS['GCS_Mars_2000_Sphere',DATUM['D_Mars_2000_Sphere',SPHEROID['Mars_2000_Sphere_IAU_IAG',3396190.0,0.0]],PRIMEM['Reference_Meridian',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',$clon],PARAMETER['Standard_Parallel_1',0.0],UNIT['Meter',1.0]]"
    srOut = gp.CreateSpatialReference(prjOut)

###''''''' need help from here
    pnt = gp.CreateObject("point", srIn)
    pnt.X = PointXcoord
    pnt.Y = PointYcoord
    pnt = pnt.SpatialReference = srIn
    pnt = pnt.Project(srOut);
###''''''' need help to here

    # print test output
    print pnt.X
    print pnt.Y

except:
    print gp.GetMessage(2)
