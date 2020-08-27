#!/usr/bin/env python
#read and visualize 2d ascii(tecplot) data 
#detdxd 2019


import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
import os

# define a function for loading data from column-ascii data
# istart is the data starting row number, jdata is the column number
def loaddata(filename,istart,jdata):
    fo=open(filename,'r')
    data=fo.readlines()
    fo.close()
    x=[]
    for line in data[istart:]:
        line=line.split()
        x.append(float(line[jdata]))
    del data
    print ("len(%s): %d"%(filename,len(x)))
    x=np.array(x)  #transform the list x to an array
    return x

rs=2.95e5*1.e8 #rs_sun * M_BH/M_sun

dtdump=1.0
for filename in os.listdir("./"):
    if filename.startswith("twoaa000000."):

        r=loaddata("./%s"%filename,3,0)    
        theta=loaddata("./%s"%filename,3,1) 
        den=loaddata("./%s"%filename,3,3) 
#        print ("den.shape:", den.shape)

        igrid=100; jgrid=160

        r.shape=igrid,jgrid 
        theta.shape=igrid,jgrid
        den.shape=igrid,jgrid
        
        xx=r*np.sin(theta)
        yy=r*np.cos(theta)   
 
        print ("plotting:",filename)
        fig=plt.figure(figsize=(7,6))
        ax=fig.add_subplot(111)
        pcm=ax.pcolormesh(xx,yy,np.log10(den),vmin=-22.,vmax=-9.,cmap=cm.jet)
        #pcm=ax.contourf(xx,yy,np.log10(den),200,vmin=-20,vmax=-10,cmap=cm.jet)
        ax.set_xlim(0.,1500.)
        ax.set_ylim(0.,1500.)
        ax.set_xlabel('$r\ /Rs$')
        ax.set_ylabel('$r\ /Rs$')
        gca().set_aspect('equal')
        #set colorbar:        
        plt.subplots_adjust(0.1,0.2,0.8,0.9)# (left,bottom,right,top)
        cax = plt.axes([0.805, 0.2, 0.02, 0.7])  #[left,bottom,width,height]
        cbar=plt.colorbar(pcm,cax=cax,orientation='vertical')
        cbar.set_label('$lg(\\rho\ /\ g\  cm^{-3}) $')
        cbar.set_ticks(np.linspace(-22,-9,5))

        nfile=filename.split('.')[-1]
        print('nfile:',nfile)
        n=[]
        n.append(int(nfile))
        t=n[0]*dtdump
        plt.suptitle("{}{:.0f}{}".format('$M_{BH}=10^{8}M_{\odot}$, $\\epsilon=0.5$, $t=$',t,'yr'))


        fig.savefig("./%s.png"%('den'+filename.split('.')[-1])) #save fig as "denoutN.pdf"

