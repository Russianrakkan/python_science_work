import pandas as pd
import seaborn as sns
import matplotlib
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
        if (i<6):
            numberslist=line.split()
            x.append(float(numberslist[0]))
            y.append(float(numberslist[1]))
            N.append(round(float(numberslist[2])))
        if (i==5):
            xc.append(statistics.mean(x))
            yc.append(statistics.mean(y))
            Nc.append(round(statistics.mean(N)))
            x.clear()
            y.clear()
            N.clear()
            i=0
    d = dict()
    d['x'] = xc
    d['y'] = yc
    d['N'] = Nc
    file.close()
    return d;

if __name__ == "__main__":
    d_f=dict()
    d=Base("C:/Coords/1.txt")
    try:
        d_f['x']= d_f['x']+d['x']
        d_f['y']= d_f['y']+d['y']
        d_f['N']= d_f['N']+d['N']
    except Exception:
        d_f = d.copy()

    data = pd.DataFrame(d_f)

    print(data)

    x1=data["x"].to_list()
    y1=data["y"].to_list()
    w=data["N"].to_list()

    matplotlib.rc('xtick', labelsize=25)
    matplotlib.rc('ytick', labelsize=25)

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=20, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Цветовая диаграмма событий \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x1, y1, weights=w, bins=(22, 22), range=[[-6, 5],[-10, 1]], cmap=cm.jet);
    plt.colorbar()

    plt.show()
