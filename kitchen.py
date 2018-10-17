#!/usr/bin/python 
import psycopg2 
import sys 
import pprint
import psycopg2.extras
import socket
import psycopg2.extensions
import subprocess
from datetime import datetime
import JulTime
import random 
import sys
import time
import sched
#import OutLetSim
#values = OutLetSim.outletData(name)
a = JulTime.CalJT()
#dt = datetime.datetime.now()


##---------------------------------------------------------------------------------------------------------##
##                                                                                                         ##
## NMSU Power Project                                                                                      ##
## Author: Luis E Martinez                                                                                 ##
## with code from Jose Tabarez                                                                             ##
## Email:  luizmartines@gmail.com, luizm929@nmsu.edu                                                       ##
##                                                                                                         ##
##I created a few random number generators in order to simulate ocupancy and loads.
##
##---------------------------------------------------------------------------------------------------------##

#Make some values a bit random
#voltage=random.gauss(120.0, 8.0)
#current=random.gauss(20.0, 3.0)
#phase=random.gauss(180.0, 8.0)

def main():
    voltage = random.gauss(120.0, 2.0)
    current = random.gauss(20.0, 2.0)
    phase = random.gauss(180.0, 2.0)
    temp = random.gauss(70.0, 2.0)
    power = random.gauss(120.0, 2.0)

    v2 = random.gauss(120.0, 2.0)
    c2 = random.gauss(20.0, 2.0)
    ph2 = random.gauss(180.0, 2.0)
    temp2 = random.gauss(70.0, 2.0)
    power2 = random.gauss(120.0, 2.0)

    v3 = random.gauss(120.0, 2.0)
    c3 = random.gauss(20.0, 2.0)
    ph3 = random.gauss(180.0, 2.0)
    temp3 = random.gauss(70.00, 2)
    power3 = random.gauss(120.0, 2.0)

    v4 = random.gauss(120.0, 2.0)
    c4 = random.gauss(20.0, 2.0)
    ph4 = random.gauss(180.0, 2.0)
    temp4 = random.gauss(70.0, 2.0)
    power4 = random.gauss(120.0, 2.0)

    v5 = random.gauss(120.0, 2.0)
    c5 = random.gauss(20.0, 2.0)
    ph5 = random.gauss(180.0, 2.0)
    temp5 = random.gauss(70.0, 2.0)
    power5 = random.gauss(120.0, 2.0)

    v6 = random.gauss(120.0, 2.0)
    c6 = random.gauss(20.0, 2.0)
    ph6 = random.gauss(180.0, 2.0)
    temp6 = random.gauss(70.0, 2.0)
    power6 = random.gauss(120.0, 2.0)
    
    #Randomise Ocupancy we create a few just to not get the same value for all outlets
    oc1 = random.choice([True, False])
    oc2 = random.choice([True, False])
    oc3 = random.choice([True, False])

    """ This line is used by psypcopg2 to know where to connect to  """
    conn_string = "host='192.168.1.101' dbname='kitchen' user='worker101' password=powerproject"
    """ We wait to get a connection"""
    print("Connecting to database ...\n ->%s"%(conn_string))
    """ Get a connection, if a connect cannot be made an exception will be raised"""
    conn = psycopg2.connect(conn_string)
    """ """
    cursor = conn.cursor()
    print("Connected !!!\n")
    
    
    ##                                          MASTER TABLES - DO NOT REMOVE MASTER TABLES                                         

    ## We create a MASTER table allsmartoutlets and we create all the smart outlets from this template 
    cursor.execute("CREATE TABLE IF NOT EXISTS allsmartoutlets (Voltage integer, Current integer, Phase integer, Temperature integer, Ocupancy boolean, Power integer, Outlet1Timestamp numeric, RPITimestamp numeric, MainServerTimestamp numeric );")
    
    
    ## We leave room to grow in case there is more than one thermostat per house, we create a master thermostat table.
    
    ##                                         Master Thermostat                                      
    cursor.execute("CREATE TABLE IF NOT EXISTS all_thermostats (Onoff boolean, Ocupancy boolean, Temperature numeric, ThermostatTimestamp numeric, RPITimestamp numeric, MainServerTimestamp numeric);")

    ##                                         Master Alarms                                          
    cursor.execute("CREATE TABLE IF NOT EXISTS all_alarms (OperationalFailure boolean, MeasurementFailure boolean, TimeSync numeric, AlarmTimestamp numeric, RPITimestamp numeric, MainServerTimestamp numeric);")

    ##                                          MASTER TABLES - DO NOT REMOVE MASTER TABLES                                         
    
    
    
    
    ## SMART OUTLET 1   ##
    ## Create a table inhertis all columns from master table plus one extra timestamp column """
    cursor.execute("CREATE TABLE IF NOT EXISTS outlet1_2017_04 (Device_id varchar) INHERITS (allsmartoutlets);")
    
    ## Here we define types ans store values into table """
    cursor.execute("INSERT INTO outlet1_2017_04 (Device_id, Voltage, Current, Phase, Temperature, Ocupancy, Power, Outlet1Timestamp, RPITimestamp, MainServerTimestamp)  VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)", ("Ox01", voltage, current, phase, temp, oc1, power,a,a,a))

    
    
    
    ## SMART OUTLET 2  
    ## We create a table first  
    cursor.execute("CREATE TABLE IF NOT EXISTS outlet2_2017_04 (Device_id varchar) INHERITS (allsmartoutlets);")
    
    ## Here we define types ans store values into table 
    cursor.execute("INSERT INTO outlet2_2017_04 (Device_id,Voltage,Current,Phase, Temperature, Ocupancy,Power,Outlet1Timestamp, RPITimestamp, MainServerTimestamp)  VALUES (%s, %s,%s, %s, %s,%s,%s,%s,%s,%s)", ("Ox02", v2, c2, ph2, temp2, oc2, power2,a,a,a))
    
    
    ## Smart Outlet 3
    
    cursor.execute("CREATE TABLE IF NOT EXISTS outlet3_2017_04 (Device_id varchar) INHERITS (allsmartoutlets);")
    ## We insert the values in their columns
    cursor.execute("INSERT INTO outlet3_2017_04 (Device_id, Voltage, Current, Phase, Temperature, Ocupancy, Power, Outlet1Timestamp, RPITimestamp, MainServerTimestamp) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)", ("0x03", v3, c3, ph3, temp3, oc3, power3, a,a,a))
    
    ## Smart Outlet 4

    cursor.execute("CREATE TABLE IF NOT EXISTS outlet4_2017_04 (Device_id varchar) INHERITS (allsmartoutlets);")
    ## We insert the values in their columns
    cursor.execute("INSERT INTO outlet4_2017_04 (Device_id, Voltage, Current, Phase, Temperature, Ocupancy, Power, Outlet1Timestamp, RPITimestamp, MainServerTimestamp) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)", ("0x04", v4, c4, ph4, temp4, oc1, power4, a,a,a))
    

    ## Smart Outlet 5

    cursor.execute("CREATE TABLE IF NOT EXISTS outlet5_2017_04 (Device_id varchar) INHERITS (allsmartoutlets);")
    """We insert the values in their columns"""
    cursor.execute("INSERT INTO outlet5_2017_04 (Device_id, Voltage, Current, Phase, Temperature, Ocupancy, Power, Outlet1Timestamp, RPITimestamp, MainServerTimestamp) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)", ("0x05", v5, c5, ph5, temp5, oc2, power5, a,a,a))

    
    ## Smart Outlet 6

    cursor.execute("CREATE TABLE IF NOT EXISTS outlet6_2017_04 (Device_id varchar) INHERITS (allsmartoutlets);")
    ## We insert the values in their columns
    cursor.execute("INSERT INTO outlet6_2017_04 (Device_id, Voltage, Current, Phase, Temperature, Ocupancy, Power, Outlet1Timestamp, RPITimestamp, MainServerTimestamp) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)", ("0x06", v6, c6, ph6, temp6, oc3, power6, a,a,a))







    ## Thermostat 1
    cursor.execute("CREATE TABLE IF NOT EXISTS thermostat1 (Device_id varchar) INHERITS (all_thermostats);")
    
    ## We insert the values 
    cursor.execute("INSERT INTO thermostat1 (Device_id, Onoff, Ocupancy, Temperature, ThermostatTimestamp, RPITimestamp, MainServerTimestamp) VALUES (%s,%s, %s, %s, %s, %s, %s)", ("Therm0x01","1","1",temp, a,a,a)) 

    ##   Alarm 1  
    cursor.execute("CREATE TABLE IF NOT EXISTS alarm1 (Device_id varchar) INHERITS (all_alarms);")
    cursor.execute("INSERT INTO alarm1 (Device_id, OperationalFailure, MeasurementFailure, TimeSync, AlarmTimestamp, RPITimestamp, MainServerTimestamp) VALUES ( %s, %s, %s, %s, %s, %s, %s)", ("Alarm0x01", "0", "0", a, a, a, a))


   
    
    ## We need to commit all changes else nothign gets saved on table 
    conn.commit()
    cursor.close()
    conn.close()
if __name__== "__main__":
        main()

