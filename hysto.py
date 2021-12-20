import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np
import os
import sys
import time
import datetime
import re
import statistics
from statistics import mean
from matplotlib.colors import LinearSegmentedColormap

def Average(lst):
    return sum(lst)/len(lst)

def Base(file_name):
    file=open(file_name, 'r')
    N=list()
    Nc=list()
    x=list()
    y=list()
    t=list()
    I1=list()
    I2=list()
    I3=list()
    I4=list()
    HV1=list()
    HV2=list()
    HV3=list()
    HV4=list()
    XRayV=list()
    XRayI=list()
    XRTemp=list()
    xc=list()
    yc=list()
    tc=list()
    I1c=list()
    Srednc=list()
    tutsrednee=list()
    I2c=list()
    I3c=list()
    I4c=list()
    HV1c=list()
    HV2c=list()
    HV3c=list()
    HV4c=list()
    XRayVc=list()
    XRayIc=list()
    XRTempc=list()
    i=0
    j=0
    trig1=0
    trig2=0
    trig3=0
    for line in file:
        i+=1
        if (i>1):
            numberslist=line.split()
            xc.append(float(numberslist[0])*100000000+0.034)
            #y.append(float(numberslist[1]))
            Nc.append(float(numberslist[1]))
    d = dict()
    d['x'] = xc
    #d['y'] = yc
    d['N'] = Nc
    file.close()
    return d;

if __name__ == "__main__":
    d_f=dict()
    #d_f1=dict()
    #res=dict()
    d=Base("C:/Hysto/F8full_spectrum_Cs137_LaBr3(Ce)_SensLfc3003500000.txt")
    #d1=Base("C:/Hysto/F8cut_spectrum_Cs137_LaBr3(Ce)_SensLfc3003500000.txt")
    #d2=Base("C:/Hysto/F8cut_spectrum_Cs137_LaBr3(Ce)_SensLfc30035_200000.txt")
    #d1=Base("C:/Hysto/F7cut_spectrum_Cs137_LaBr3(Ce)_SensLfc30035_pedestal00000.txt")
    try:
        #d_f['x']= d_f['x']+d1['x']
        d_f['y']= d_f['y']+d['y']
        #d_f['N']= d_f['N']+d1['N']

        #d_f['x']= d_f['x']+d2['x']
        d_f['y']= d_f['y']+d['y']
        #d_f['N']= d_f['N']+d2['N']
        #res=d_f['N']-d_f1['N']
    except Exception:
        d_f = d.copy()
        #d_f = d1.copy()
        #d_f = d2.copy()

    data = pd.DataFrame(d_f)

    print(data['x'])

    x1=data["x"].to_list()
    #y1=data["y"].to_list()
    w=data["N"].to_list()


    #ax1 = sns.jointplot(x=x1, y=w)
    #ax1.ax_joint.cla()
    #ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    #ax1.ax_joint.set_ylabel("N, mm", fontsize=25)
    #ax1.ax_joint.set_title("Color map событий \n\n\n\n\n", fontsize=23)
    #plt.sca(ax1.ax_joint)
    #plt.hist2d(x1, w, bins=(22, 22), cmap=cm.jet);
    #plt.colorbar()
    plt.hist(-data['x'], weights=data['N'], bins = 1000);
    plt.ylabel('Entries', fontsize=25)
    plt.xlabel('10^(-9) V', fontsize=25)
    plt.title('Spectrum', fontsize=25)

    plt.show()
