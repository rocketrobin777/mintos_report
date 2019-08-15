#!/usr/bin/env python3
"""
Created on Wed Aug  7 18:36:03 2019

@author: robin
"""

from report_func import date_diff, apr, loan_d_sum, loan_mean, lo_sort 
import matplotlib.pyplot as plt
import numpy as np

def bar_chart(lo,value,title,dimension):
    x = np.arange(len(lo))  # the label locations
    width = 0.40  # the width of the bars
    fig, ax = plt.subplots()
    rects = ax.bar(x - width,
                   value, width,
                   label=title,
                   color = '#71c7c5') #mintos color
    ax.set_ylabel(title+' '+dimension)
    ax.set_title(title+' sorted by loan orgs')

    def autolabel(rects,label):
        """Attach a text label above each bar in *rects*, displaying its height."""
        xtl = []
        ct  = 0
        for rect in rects:
            ax.annotate('{}'.format(label[ct]),
                        xy=(rect.get_x()+0.05 + 2*rect.get_width() / 2, 0),
                        xytext=(0, 5),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='left', va='bottom',rotation=90)
            xtl.append('')
            ct += 1
        return xtl
    
    xtl = autolabel(rects,lo)
    ax.set_xticks(x)
    ax.set_xlim(-1,max(x)+1)
    ax.set_xticklabels(xtl)
    scale = round(np.log(max(value))/np.log(10))-1
    scale = np.power(10,scale)
    ymin = scale*round(0.49+min(value)/scale)
    ymax = scale*round(max(value)/scale)
    tick = scale*round(0.49+max(value)/(10*scale))
    yax = np.arange(ymin-tick,ymax+tick,tick)
    #ax.set_yticks(np.arange(10*round(min(value)/10),10*round(0.49+max(value)/10)+5,5))
    ax.set_yticks(yax)
    ax.grid(True)
    fig.tight_layout()
    plt.show()
    fig.savefig(title+'.pdf')

def profit_chart(lo,invest,receive):
    profit = loan_d_sum(invest,receive)
    [profit,lo] = lo_sort(profit,lo)
    bar_chart(lo,profit,'Profit','[€]')

def duration_chart(lo,days):
    duration = loan_mean(days)
    [duration,lo] = lo_sort(duration,lo)
    bar_chart(lo,duration,'Duration','[days]')
    
def apr_chart(lo,mapr):
    mapr = loan_mean(mapr)
    [mapr,lo] = lo_sort(mapr,lo)
    bar_chart(lo,mapr,'APR','[%]')
        