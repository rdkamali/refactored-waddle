
from datetime import datetime
import os
import sys
import math 


def basecal(date, adjust):
    today = date
    # if adjus:
    #     adjustmili = 1000*60*60*24*adjust
    #     todaymili = today.getTime()+adjustmili
    #     today = datetime(todaymili)

    # wd = date.getDay() + 1
    dt = today.date()
    day = dt.day
    month = dt.month
    year = dt.year
    m = month+1
    y = year
    
    if m<3 :
        y -= 1
        m += 12

    a = math.floor(y/100.0)
    b = 2-a+math.floor(a/4.0)
    if y<1583: 
        b = 0
    if y==1582 :
        if m>10 :
            b = -10
        if m==10 :
            b = 0
            if day>4: 
                b = -10
		

    jd = math.floor(365.25*(y+4716))+math.floor(30.6001*(m+1))+day+b-1524

    b = 0
    if jd>2299160 :
        a = math.floor((jd-1867216.25)/36524.25)
        b = 1+a-math.floor(a/4.0)

    bb = jd+b+1524
    cc = math.floor((bb-122.1)/365.25)
    dd = math.floor(365.25*cc)
    ee = math.floor((bb-dd)/30.6001)
    day =(bb-dd)-math.floor(30.6001*ee)
    month = ee-1
    if(ee>13) :
        cc += 1
        month = ee-13
	
    year = cc-4716

    iyear = 10631.0/30.0
    epochastro = 1948084
	# var epochcivil = 1948085; Not used

    shift1 = 8.01/60.0

    z = jd-epochastro
    cyc = math.floor(z/10631.0)
    z = z-10631*cyc
    j = math.floor((z-shift1)/iyear)
    iy = 30*cyc+j
    z = z-math.floor(j*iyear+shift1)
    im = math.floor((z+28.5001)/29.5)
    if im==13 :
        im = 12
			
    id = z-math.floor(29.5001*im-29)

    myRes = []

    myRes.append( day) #calculated day (CE)
    myRes.append( month-1) #calculated month (CE)
    myRes.append( year) # calculated year (CE)
    myRes.append( jd-1) # julian day number
    # myRes[4] = wd-1) # weekday number
    myRes.append( id) # islamic date
    myRes.append(im-1) #islamic month
    myRes.append( iy) #islamic year
    return myRes

y = input("Enter date: ") # 20220804
date1 = datetime.strptime(y, '%Y%m%d')

print(date1)
x= basecal(date1, 0)

print(x)
