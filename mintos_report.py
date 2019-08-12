#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:05:41 2019

@author: robin
"""

from pandas import read_excel
from report_chart import duration_chart,profit_chart, apr_chart, date_diff, apr

data    = []
data.append([])                             # 0 Loan Originator
data.append([])                             # 1 Invested
data.append([])                             # 2 Received
data.append([])                             # 3 Yield
data.append([])                             # 4 Buy Day
data.append([])                             # 5 Pay Day
data.append([])                             # 6 Duration in days
data.append([])                             # 7 APR

report    = read_excel("report.xlsx", header=None)      # get content w.o. header

for i in range(1,len(report)):  
    ct = 0;                                 # counter value for loan originator
    for j in range(0,len(data[0])):         # create list of loan orgs only one time
        if data[0][j] != report[6][i]:
            ct += 1
    if ct == len(data[0]):
        data[0].append(report[6][i])
        data[1].append([])
        data[2].append([])
        data[3].append([])
        data[4].append([])
        data[5].append([])
        data[6].append([])
        data[7].append([])
        
    k = data[0].index(report[6][i])
    data[1][k].append(report[16][i])        # 1 Invested
    data[2][k].append(report[18][i])        # 2 Received
    data[3][k].append(data[2][k][len(data[2][k])-1] - data[1][k][len(data[1][k])-1])
    data[4][k].append(report[17][i])        # 4 Buy Day
    data[5][k].append(report[24][i])        # 5 Pay Day
    data[6][k].append(date_diff(data[4][k][len(data[4][k])-1],
                                data[5][k][len(data[5][k])-1])) # 6 Days
    data[7][k].append(apr(data[1][k][len(data[1][k])-1],
                          data[2][k][len(data[2][k])-1],
                          data[6][k][len(data[6][k])-1]))       # 7 APR
    if data[7][k][len(data[7][k])-1] == 0:  # if days < 3
        data[7][k][len(data[7][k])-1] = report[11][i]
      
profit_chart(data[0],data[1],data[2])
duration_chart(data[0],data[6])
apr_chart(data[0],data[7])