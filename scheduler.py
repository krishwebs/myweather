#!/usr/bin/python

import subprocess
import re
import os
import sys
import time
import MySQLdb as mdb
import datetime

databaseUsername="root"
databasePassword="krish123"
databaseName="krish_py" #do not change unless you named the Wordpress database with some other name

def saveToDatabase(temperature,humidity):

    con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)
    currentDate=datetime.datetime.now().date()

    now=datetime.datetime.now()
    midnight=datetime.datetime.combine(now.date(),datetime.time())
    minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$


    with con:
            cur=con.cursor()

            cur.execute("INSERT INTO temperatures (temperature,humidity, dateMeasured, hourMeasured) VALUES (%s,%s,%s,%s)",(temperature,humidity,currentDate, minutes))

    print "Saved temperature"
    return "true"


def readInfo():
    temperatureSaved="false" #keep on reading till you get the info

    while(temperatureSaved=="false"):
    # Run the DHT program to get the humidity and temperature readings!

        source = "/home/praveen/project/joach-myweather/myweather/weather.py"
        # search for tempretures , continue to search untill it do not found 
        temp1_matches = search_attr('Temp1', source)
        temp2_matches = search_attr('Temp2', source)
        temp3_matches = search_attr('Temp3', source)
        temp4_matches = search_attr('Temp4', source)

        # search for humidity printout
        # matches = re.search("Press =\s+([0-9.]+)", output)

        # if (not matches):
        #     time.sleep(3)
        #     continue
        # humidity = float(matches.group(1))
        #humidity=str(humidity)+"%"

        humidity = search_attr('Press', source)
        print "Temperature: %.1f C" % temp1_matches
        print "Temperature: %.1f C" % temp2_matches
        print "Temperature: %.1f C" % temp3_matches
        print "Temperature: %.1f C" % temp4_matches
        print "Pressure:    %s %%" % humidity
        return "true"
        #return saveToDatabase(temp,humidity)


def search_attr(val, source):
    output = subprocess.check_output([source]);
    matches = re.search(("%s =\s+([-]?[0-9.]+)" % val), output)
    if (not matches):
        print "searching for %s"% (val)
        time.sleep(3)
        search_attr(val, source)
    return float(matches.group(1))

#check if table is created or if we need to create one
try:
    queryFile=file("createTable.sql","r")

    con=mdb.connect("localhost", databaseUsername,databasePassword,databaseName)
    currentDate=datetime.datetime.now().date()

    with con:
        line=queryFile.readline()
        query=""
        while(line!=""):
            query+=line
            line=queryFile.readline()

        cur=con.cursor()
        cur.execute(query)

            #now rename the file, because we do not need to recreate the table everytime this script is run
        queryFile.close()
        os.rename("createTable.sql","createTable.sql.bkp")


except IOError:
    pass #table has already been created

status="false"
while(status!="true"):

    status=readInfo()
