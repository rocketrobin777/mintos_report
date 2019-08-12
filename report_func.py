"""
Created on Wed Aug  7 18:06:29 2019

@author: robin
"""

import time
from datetime import datetime
from time import mktime

def date_diff(date1,date2):
   date1    = time.strptime(date1, '%d.%m.%Y')
   date2    = time.strptime(date2, '%d.%m.%Y')
   temp     = datetime.fromtimestamp(mktime(date2))
   temp     = temp - datetime.fromtimestamp(mktime(date1))
   return temp.days

def apr(invest,receive,days):
    if days < 3:
        apr = 0
    else:
        apr = (receive-invest)/invest
        if apr < 0:
            apr = 0
        else:
            apr = pow(1+apr,1/days)-1
            apr = 100*(pow(1+apr,360)-1)
    return apr

def loan_d_sum(value1,value2):
    result = []
    for i in range(0,len(value1)):
        result.append(round(100*(sum(value2[i])-sum(value1[i])))/100)
    return result

def loan_mean(value):
    result = []    
    for i in range(0,len(value)):
        result.append(round(100*sum(value[i]))/(100*len(value[i])))
    return result            

def lo_sort(value1,value2):
    temp = []
    for i in range(0,len(value1)):
        temp.append((value1[i],value2[i]))
    value2 = sorted(value2)
    res = [tuple for x in value2 for tuple in temp if tuple[1] == x]
    for i in range(0,len(res)):
        value1[i] = res[i][0]
    return value1,value2 

