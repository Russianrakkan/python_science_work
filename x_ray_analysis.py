#!/usr/bin/env python
# coding: utf-8
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

def Base(file_name,smth):
    file=open(file_name, 'r')
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
    strRE = re.compile("# "+smth+" #.*")
    strRE2 = re.compile(", doublet.*")
    for line in file:
        i+=1
        if (i==5):
            if(not strRE.search(line)):
                print(file_name+" is not "+smth+"\n")
                break
            else:
                print("sucсess: "+file_name)
                if(strRE2.search(line)):
                    trig2=1
        if (i>=30):
            j+=1
            if (j>4) and (j<16):
                numberslist=line.split()
                if (len(numberslist)<4) and (len(numberslist)>1):
                    break
                x.append(round(float(numberslist[0])))
                y.append(round(float(numberslist[1])))
                t.append(float(numberslist[2]))
                I1.append(float(numberslist[3]))
                I2.append(float(numberslist[4]))
                #print(numberslist)
                ##x.append(float(line[:9]))
                ##y.append(float(line[10:19]))
                ##t.append(float(line[20:28]))

                ##if trig3==0:
                    ##if trig2==0:
                        ##if trig1==0:
                            ##I1.append(float(line[29:39]))
                            ##I2.append(float(line[40:48]))
                            ##if (float(line[40:48])>3000):
                                ##if (float(line[29:39])>9000):
                                    ##trig3=1
                                ##else:
                                    ##trig1=1
                        ##else:
                            ##I1.append(float(line[29:36]))
                            ##I2.append(float(line[37:51]))
                    ##else:
                        ##I1.append(float(line[29:36]))
                        ##I2.append(float(line[37:44]))
                ##else:
                    ##I1.append(float(line[29:39]))
                    ##I2.append(float(line[40:50]))

                # I2.append(float(line[37:44]))
                # I3.append(float(line[45:52]))
                # I4.append(float(line[53:60]))
                # HV1.append(float(line[61:68]))
                # HV2.append(float(line[69:76]))
                # HV3.append(float(line[77:84]))
                # HV4.append(float(line[85:92]))
                # XRayV.append(float(line[93:98]))
                # XRayI.append(float(line[99:104]))
                # XRTemp.append(float(line[105:110]))
            if (j==15):
                #if (statistics.mean(I1)>20):
                xc.append(round(statistics.mean(x)))
                yc.append(round(statistics.mean(y)))
                tc.append(statistics.mean(t))
                I1c.append(statistics.mean(I1))
                I2c.append(statistics.mean(I2))
                Srednc.append(statistics.mean(I1))
                # I2c.append(statistics.mean(I2))
                # I3c.append(statistics.mean(I3))
                # I4c.append(statistics.mean(I4))
                # HV1c.append(statistics.mean(HV1))
                # HV2c.append(statistics.mean(HV2))
                # HV3c.append(statistics.mean(HV3))
                # HV4c.append(statistics.mean(HV4))
                # XRayVc.append(statistics.mean(XRayV))
                # XRayIc.append(statistics.mean(XRayI))
                # XRTempc.append(statistics.mean(XRTemp))

                x.clear()
                y.clear()
                t.clear()
                I1.clear()
                I2.clear()
                # I2.clear()
                # I3.clear()
                # I4.clear()
                # HV1.clear()
                # HV2.clear()
                # HV3.clear()
                # HV4.clear()
                # XRayV.clear()
                # XRayI.clear()
                # XRTemp.clear()

                j=0
        #if(i==28000):
            #break
    #medI.append(statistics.mean(I1c))
    #print(t)
    d = dict()
    d['x'] = xc
    d['y'] = yc
    d['t'] = tc
    d['I1'] = I1c
    d['I2'] = I2c
    #medI = Average(Srednc)
    if len(Srednc)!=0:
        #print(sum(Srednc))
        #print(len(Srednc))
        #print(sum(Srednc)/len(Srednc))
        for number in Srednc:
            tutsrednee.append(statistics.mean(Srednc))
        d['sredn'] = tutsrednee
    else:
        d['sredn'] = tutsrednee


    #medI=sum(d['I1'])/len(d['I1'])
    #d['medI']= medI
    # d['I2']= I2c
    # d['I3']= I3c
    # d['I4']= I4c
    # d['HV1']= HV1c
    # d['HV2']= HV2c
    # d['HV3']= HV3c
    # d['HV4']= HV4c
    # d['XRayV']= XRayVc
    # d['XRayI']= XRayIc
    # d['XRTemp']= XRTempc
    #print(tutsrednee)
    file.close()
    return d;


if __name__ == "__main__":
    file=open('C:/Data/Directory_list', 'w+')
    print("Created Directory_list\n")
    d_f=dict()
    print("Processing...")
    smth= input("Which detector to use? (QL1C or QL1)\n[DF]: ")
    for line in os.listdir(path= "C:/Data/"):
        file.write(line + '\n')

        #qscanner_out.2018-03-07_16-10
        strRE1 = re.compile("qscanner_out.(.*)")

        print("Loading "+line)
        if strRE1.search(line):
            q=strRE1.search(line)
            d= Base("C:/Data/"+str(q.group(0)),smth)
            #print(d)
            try:
                d_f['x']= d_f['x']+d['x']
                d_f['y']= d_f['y']+d['y']
                d_f['t']= d_f['t']+d['t']
                d_f['I1']= d_f['I1']+d['I1']
                d_f['I2']= d_f['I2']+d['I2']
                d_f['sredn']= d_f['sredn']+d['sredn']
                #d_f['medI']= d_f['medI']+d['medI']
                # d_f['I2']= d_f['I2']+d['I2']
                # d_f['I3']= d_f['I3']+d['I3']
                # d_f['I4']= d_f['I4']+d['I4']
                # d_f['HV1']= d_f['HV1']+d['HV1']
                # d_f['HV2']= d_f['HV2']+d['HV2']
                # d_f['HV3']= d_f['HV3']+d['HV3']
                # d_f['HV4']= d_f['HV4']+d['HV4']
                # d_f['XRayV']= d_f['XRayV']+d['XRayV']
                # d_f['XRayI']= d_f['XRayI']+d['XRayI']
                # d_f['XRTemp']= d_f['XRTemp']+d['XRTemp']
            except Exception:
                d_f = d.copy()
            #print(d_f)
            #logger.debug(q.group(1)+"-q1 c-"+str(c))
            #logger.debug(Delta_data(q.group(1)))
            #"old" check Delta_data(str(q.group(1))) > 30
        else:
            print(line+ " is not researching data")

    data = pd.DataFrame(d_f)
    file.close()


    # In[60]:


    data

  #  data[["x","y","I1"]].head()


   # sns.histplot(data[["x","y","I1"]], x="x", y="y", cbar=True)


    x1=data["x"].to_list()
    y1=data["y"].to_list()
    #w=data["I1"].to_list()
    w=data["I2"].to_list()

    #otnosit=list()
    #otnosit2=list()
    #for number in w:
        #otn=number-statistics.mean(w)
        #otnosit.append(otn)
        #print(otn)
    #for number in otnosit:
        #otnosit2.append(number*number)
    #print(otnosit2)
    #pogr=(sum(otnosit2)/(len(otnosit2)*(len(otnosit2)-1)))**(0.5)
    #print(pogr)
    #otnpogr=pogr/statistics.mean(w)
    #print(otnpogr)

  #  data["I1"].mean()

    q1=data[data['I1'] > 1.1*data["sredn"]]
    q2=data[data['I1'] > 1.2*data["sredn"]]
    q3=data[data['I1'] > 1.3*data["sredn"]]
    q4=data[data['I1'] > 1.4*data["sredn"]]
    q5=data[data['I1'] > 1.5*data["sredn"]]
    q6=data[data['I1'] > 1.6*data["sredn"]]
    q7=data[data['I1'] > 1.7*data["sredn"]]
    q8=data[data['I1'] > 1.8*data["sredn"]]
    q9=data[data['I1'] > 1.9*data["sredn"]]
    q0=data[data['I1'] > data["sredn"]]


    h1=data[data['I1'] < 0.9*data["sredn"]]
    h2=data[data['I1'] < 0.8*data["sredn"]]
    h3=data[data['I1'] < 0.7*data["sredn"]]
    h4=data[data['I1'] < 0.6*data["sredn"]]
    h5=data[data['I1'] < 0.5*data["sredn"]]
    h6=data[data['I1'] < 0.4*data["sredn"]]
    h7=data[data['I1'] < 0.3*data["sredn"]]
    h8=data[data['I1'] < 0.2*data["sredn"]]
    h9=data[data['I1'] < 0.1*data["sredn"]]
    h0=data[data['I1'] < data["sredn"]]
    #q1=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.1*data["I1"].mean())]
    # q2=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.2*data["I1"].mean())]
    # q3=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.3*data["I1"].mean())]
    # q4=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.4*data["I1"].mean())]
    # q5=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.5*data["I1"].mean())]
    # q6=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.6*data["I1"].mean())]
    # q7=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.7*data["I1"].mean())]
    # q8=data[(data['I1'] > data["I1"].mean()) & (data['I1'] < 1.8*data["I1"].mean())]
    #q0=data[(data['I1'] > data["I1"].mean())]????????????


    # In[79]:


    x10=q0["x"].to_list()
    y10=q0["y"].to_list()

    x11=q1["x"].to_list()
    y11=q1["y"].to_list()

    x12=q2["x"].to_list()
    y12=q2["y"].to_list()

    x13=q3["x"].to_list()
    y13=q3["y"].to_list()

    x14=q4["x"].to_list()
    y14=q4["y"].to_list()

    x15=q5["x"].to_list()
    y15=q5["y"].to_list()

    x16=q6["x"].to_list()
    y16=q6["y"].to_list()

    x17=q7["x"].to_list()
    y17=q7["y"].to_list()

    x18=q8["x"].to_list()
    y18=q8["y"].to_list()


    x20=h0["x"].to_list()
    y20=h0["y"].to_list()

    x21=h1["x"].to_list()
    y21=h1["y"].to_list()

    x22=h2["x"].to_list()
    y22=h2["y"].to_list()

    x23=h3["x"].to_list()
    y23=h3["y"].to_list()

    x24=h4["x"].to_list()
    y24=h4["y"].to_list()

    x25=h5["x"].to_list()
    y25=h5["y"].to_list()

    x26=h6["x"].to_list()
    y26=h6["y"].to_list()

    x27=h7["x"].to_list()
    y27=h7["y"].to_list()

    x28=h8["x"].to_list()
    y28=h8["y"].to_list()


    # In[ ]:




    # cmap = LinearSegmentedColormap.from_list('mycmap', ['blue', 'yellow'])
    # fig, ax = plt.subplots()
    # im = ax.imshow(np.random.random((10, 10)), cmap=cmap, interpolation='nearest')
    # fig.colorbar(im)
    # plt.show()


    # In[80]:

#ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
#ax1.ax_joint.cla()
#ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
#ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
#ax1.ax_joint.set_title("Цветовая диаграмма \n\n\n\n\n", fontsize=25)
#plt.sca(ax1.ax_joint)
#plt.hist2d(x1,y1,weights=w,norm=mcolors.LogNorm(),cmap=cm.jet)
#plt.colorbar()


    #ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    #ax1.ax_joint.cla()
    #ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    #ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    #ax1.ax_joint.set_title("Цветовая диаграмма \n\n\n\n\n", fontsize=25)
    #plt.sca(ax1.ax_joint)
    #plt.hist2d(data["x"], data["y"], weights=w ,bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    #plt.colorbar()



    # In[81]:

    matplotlib.rc('xtick', labelsize=25)
    matplotlib.rc('ytick', labelsize=25)


    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=67, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Цветовая диаграмма I2 \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(data["x"], data["y"], weights=w ,bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    #plt.colorbar()




    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение над средним \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x10, y10, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 10% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x11, y11, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 20% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x12, y12, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 30% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x13, y13, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 40% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x14, y14, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 50% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x15, y15, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 60% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x16, y16, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 70% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x17, y17, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Превышение среднего на 80% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x18, y18, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.jet);
    plt.colorbar()


    ###


    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Значения, ниже среднего \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x20, y20, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 10% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x21, y21, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 20% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x22, y22, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 30% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x23, y23, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 40% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x24, y24, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 50% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x25, y25, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 60% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x26, y26, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 70% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x27, y27, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    ax1.ax_joint.cla()
    ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    ax1.ax_joint.set_title("Ниже среднего на 80% \n\n\n\n\n", fontsize=25)
    plt.sca(ax1.ax_joint)
    plt.hist2d(x28, y28, bins=(61, 67), range=[[330, 1550],[-10, 1330]], cmap=cm.brg);
    plt.colorbar()

    #ax1 = sns.jointplot(x=x1, y=y1, marginal_kws=dict(bins=55, fill=True))
    #ax1.ax_joint.cla()
    #ax1.ax_joint.set_xlabel("x, mm", fontsize=25)
    #ax1.ax_joint.set_ylabel("y, mm", fontsize=25)
    #ax1.ax_joint.set_title("Цветовая диаграмма \n\n\n\n\n", fontsize=25)
    #plt.sca(ax1.ax_joint)
    #plt.hist2d(x1,y1,weights=w,norm=mcolors.LogNorm(),cmap=cm.jet)
    #plt.colorbar()

    plt.show()

    #print(data["sredn"])

    #
    #
    # # In[82]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x12, y12, bins=(55, 40), cmap=cm.jet);
    #
    #
    # # In[83]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x13, y13, bins=(55, 40), cmap=cm.jet);
    #
    #
    # # In[84]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x14, y14, bins=(55, 40), cmap=cm.jet);
    #
    #
    # # In[85]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x15, y15, bins=(55, 40), cmap=cm.jet);
    #
    #
    # # In[86]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x16, y16, bins=(55, 40), cmap=cm.jet);
    #
    #
    # # In[87]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x17, y17, bins=(55, 40), cmap=cm.jet);
    #
    #
    # # In[88]:
    #
    #
    # ax1 = sns.jointplot(x=x1, y=y1)
    # ax1.ax_joint.cla()
    # plt.sca(ax1.ax_joint)
    # plt.hist2d(x18, y18, bins=(55, 40), cmap=cm.jet);
    #ax.set_title('Нормальное распределение')


    #print(data)
    #print(data["I1"].mean())
    #print(data["I1"])
    #print(q0)
    #print(q1)
    #print(q2)
    #print(q3)
    #print(q4)
    #print(q5)
    #print(q6)
    #print(q7)
    #print(q8)
    #print(q9)
    #print(w)
