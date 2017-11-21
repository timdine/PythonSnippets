import active_directory
import pyodbc
import re

updateStrings = []

con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = '', database = '')
#con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = '', database = '')
cur = con.cursor()
queryString = "select * from azteca.employee where (LOGINNAME = '' or EMAIL = '') and ISACTIVE = 'Y'" # and LASTNAME not like '%''%'"
for row in cur.execute(queryString):
    print "---------------------------------------------------------------"
    print(row.FIRSTNAME, row.LASTNAME, row.LOGINNAME, row.EMAIL, row.EMPLOYEESID)

    numPeople = active_directory.search("displayName='"+row.LASTNAME.replace("'", "''")+", "+row.FIRSTNAME+"'")
    peopleCount = len(list(numPeople))
    print "People With this name:", peopleCount
    for person in active_directory.search("displayName='"+row.LASTNAME.replace("'", "''")+", "+row.FIRSTNAME+"'"):
        print "AD Information:"
        print "--Name:", person.displayName
        print "--Email:", person.mail
        print "--Login", person.sAMAccountname
        #print "ldap info:", person
        print peopleCount
        if (peopleCount > 0):
            updateQueryString = "update azteca.employee set"
            if (person.mail != None):
                updateQueryString += " EMAIL = '"+person.mail+"'"
            if (person.mail != None and person.sAMAccountname != None):
                updateQueryString += ","
            if (person.sAMAccountname != None):
                updateQueryString += " LOGINNAME = '"+person.sAMAccountname+"'"
            updateQueryString += " where EMPLOYEESID = "+str(row.EMPLOYEESID)+""
            print updateQueryString
            updateStrings.append(updateQueryString)

for updateString in updateStrings:
    print updateString
