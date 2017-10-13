# -*- coding: utf-8 -*-
"""
Created on Sun May 21 13:11:03 2017

@author: pegasus
"""

import urllib
import pandas as pd
import numpy as np
import bs4 as bs
import re

df=pd.DataFrame(columns=[])
dates=[1,5,10,15,20]
state=['HR','MP']
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
yr=[2012,2013,2014,2015,2016,2017]
fin=np.array([])
print (len(fin))
for q,j in enumerate(state):
    df=pd.DataFrame(data=fin)
    print(df)
    df.to_csv("wh.csv",index=False)
    for r,w in enumerate(yr):
        for k,inn in enumerate(month):
            for p,i in enumerate(dates):
    
    
        
            
                if(p>0):
                    
                    print ("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=1&Tx_State="+j+"&Tx_District=0&Tx_Market=0&DateFrom="+str(i)+"-"+month[k]+"-"+str(w)+"&DateTo="+str(i+5)+"-"+month[k]+"-"+str(w)+"&Fr_Date="+str(i)+"-"+month[k]+"-"+str(w)+"&ToDate="+str(i+5)+"-"+month[k]+"-"+str(w)+"&Tx_Trend=0&Tx_CommodityHead=Maize&Tx_StateHead=Haryana&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--")
                    sauce=urllib.request.urlopen("http://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=1&Tx_State="+j+"&Tx_District=0&Tx_Market=0&DateFrom="+str(i)+"-"+month[k]+"-"+str(w)+"&DateTo="+str(i+5)+"-"+month[k]+"-"+str(w)+"&Fr_Date="+str(i)+"-"+month[k]+"-"+str(w)+"&ToDate="+str(i+5)+"-"+month[k]+"-"+str(w)+"&Tx_Trend=0&Tx_CommodityHead=Maize&Tx_StateHead=Haryana&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--").read()
                    arr=[]
                    soup = bs.BeautifulSoup(sauce, 'lxml')
                    
                    for co in soup.find_all("span",{"id":re.compile('cphBody_GridPriceData_Labmaxpric_*')}):
                           arr.append(int(str(co).split('>')[1].split('<')[0].split('.')[0]))
                    #print(arr)
                    if(len(arr)!=0):
                        print(sum(arr)/len(arr))
                        val=int(sum(arr)/len(arr))
                    else:
                        val=0
                    aa=np.array([p,q,k,r,val])
                    print(i,j,inn,w)
                    if len(fin)>0:
                        #print (fin)
                        print (np.array([aa]))
                        fin=np.append(fin,np.array([aa]),axis=0)
                    else:
                        print("hhh")
                        fin=np.array([aa])  
                    #print(fin)
                    if(len(fin)%50==0):
                        print (len(fin),len)
                        df=pd.DataFrame(data=fin)
                        print(df)
                        df.to_csv("file5.csv",index=False)
                    print (fin)
df=pd.DataFrame(data=fin)
print(df)
df.to_csv("wh.csv",index=False)
            
    