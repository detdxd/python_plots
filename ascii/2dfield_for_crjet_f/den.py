#!/usr/bin/env python
#
#===========================================
# this script is a 2d-color-batch-plotting code 
# from a series files like: 'denascii.out1','denascii.out2',...
# Det, May 17,2018
#===========================================
#

import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
import os

#define a function for loading data 
def loaddata(filename):
    fo=open(filename,'r')
    data=fo.readlines()
    fo.close()
    x=[]
    for line in data:
        line=line.split()
        x.append(float(line[0]))
    del data
    print ("len(%s): %d"%(filename,len(x)))
    x=np.array(x) #transform the list x to an array
    return x

#define functions to reflect y and data for axisymmetric plotting:
def yreflect(y,jend):
    y1=np.zeros((jend*2-1),dtype=float)
    for j in range(0,jend*2-1):
        if j<=jend-1 :
            y1[j]=-y[jend-1-j]
        else:
            y1[j]=y[j-jend+1]
    return y1
def datareflect(data,iend,jend):
    data1=np.zeros((iend,jend*2-1),dtype=float)
    for i in range(0,iend):
        for j in range(0,jend*2-1):
            if j<=jend-1 :
                data1[i,j]=data[i,jend-1-j]
            else:
                data1[i,j]=data[i,j-jend+1]
    return data1

#data analyzing and ploting:
for denfile in os.listdir("./datas/"):
    if denfile.startswith("denascii.out"):  # find out the files with name starting as 'denascii.out' 
        x=loaddata("./datas/xhascii.out5")
        y=loaddata("./datas/yhascii.out5")
        den=loaddata("./datas/%s"%denfile)  # load data from iles with name starting as 'denascii.out' 

        cmkpc=3.08e21

        x=x/cmkpc
        y=y/cmkpc
        den=log10(den)
        den.shape=len(x),len(y) # transform 1d array to 2d array 
        den=transpose(den)
        print ("den.shape",den.shape)

#extract imax*jmax array data from len(x)*len(y) array data and transform it to imax*2jmax:
        imax=800
        jmax=800

        x1=np.zeros((imax),dtype=float) # define zero array x1
        for i in range(0,imax):x1[i]=x[i]
        y1=yreflect(y,jmax)
        den1=datareflect(den,imax,jmax)
        print ("x1.shape:",x1.shape)
        print ("y1.shape:",y1.shape)
        print ("den1.shape:",den1.shape)

#plotting:
        print ("plotting:")
        fig=plt.figure(figsize=(5,5))

        ax = plt.axes([0.15, 0.35, 0.8, 0.4]) #[left,bottom,width,height] position for plotting
        pcm=ax.pcolormesh(y1,x1,den1,vmin=-27.,vmax=-25.,cmap=cm.jet)
        ax.set_xlabel('x(kpc)')
        ax.set_ylabel('z(kpc)')
        gca().set_aspect('equal')
      #set colorbar:
        cax = plt.axes([0.15, 0.23, 0.8, 0.02])  #[left,bottom,width,height] position for colorbar
        cbar=plt.colorbar(pcm,cax=cax,orientation='horizontal')
        cbar.set_label('$lg(\\rho/g$ $cm^{-3})$')
        cbar.set_ticks(np.linspace(-27,-25,5))

        del x,y,x1,y1,den,den1

        fig.savefig("./%s.png"%('den'+denfile.split('.')[-1])) #save fig as "denoutN.pdf"
        #fig.show()

