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

def vecextract(u,idd,jdd,iplot,jplot):
    u0=np.zeros((iplot,jplot),dtype=float)
    i1=0
    for i in range(0,iplot):
        j1=0
        for j in range(0,jplot):
            u0[i,j]=u[i1,j1]
            j1=j1+jdd
        i1=i1+idd
    return u0


rs=2.95e5*1.e8 #rs_sun * M_BH/M_sun

dtdump=1.0
for filename in os.listdir("./"):
    if filename.startswith("twoaa000000."):

        r=loaddata("./%s"%filename,3,0)    
        theta=loaddata("./%s"%filename,3,1) 
        den=loaddata("./%s"%filename,3,3) 
        v1=loaddata("./%s"%filename,3,5)
        v2=loaddata("./%s"%filename,3,6)
#        print ("den.shape:", den.shape)

        igrid=100; jgrid=160

        r.shape=igrid,jgrid 
        theta.shape=igrid,jgrid
        den.shape=igrid,jgrid
        v1.shape=igrid,jgrid
        v2.shape=igrid,jgrid       
 
        xx=r*np.sin(theta)
        yy=r*np.cos(theta)   

        vx=v1*np.sin(theta)+v2*np.cos(theta)+1.e-10
        vy=v1*np.cos(theta)+v2*np.sin(theta)+1.e-10
        vlg=np.log10(np.sqrt(vx**2+vy**2))
      
        vx=vx/np.sqrt(vx**2+vy**2)
        vy=vy/np.sqrt(vx**2+vy**2)

        iplot=50;jplot=80
        idd=int(igrid/iplot);jdd=int(jgrid/jplot)
        xx=vecextract(xx,idd,jdd,iplot,jplot)
        yy=vecextract(yy,idd,jdd,iplot,jplot)
        vx=vecextract(vx,idd,jdd,iplot,jplot)
        vy=vecextract(vy,idd,jdd,iplot,jplot) 
        vlg=vecextract(vlg,idd,jdd,iplot,jplot) 
       
        print ("plotting:",filename)
        fig=plt.figure(figsize=(7,6))
        ax=fig.add_subplot(111)
        pcm=ax.pcolormesh(xx,yy,vlg,vmin=3.,vmax=9.,cmap=cm.jet)
        Q = plt.quiver(xx,yy,vx,vy,color='black',headwidth=6,headlength=4,pivot='mid', scale_units='xy',scale=0.03) #velocity plotting
        #qk = plt.quiverkey(Q, 0.7, 0.3, 1e7, r'$100km/s$', labelpos='E',coordinates='figure')        

        ax.set_xlim(0.,1500.)
        ax.set_ylim(0.,1500.)
        ax.set_xlabel('$r\ /Rs$')
        ax.set_ylabel('$r\ /Rs$')
        gca().set_aspect('equal')
        #set colorbar:        
        plt.subplots_adjust(0.1,0.2,0.8,0.9)# (left,bottom,right,top)
        cax = plt.axes([0.805, 0.2, 0.02, 0.7])  #[left,bottom,width,height]
        cbar=plt.colorbar(pcm,cax=cax,orientation='vertical')
        cbar.set_label('$lg(v\ /\ cm\  s^{-1}) $')
        cbar.set_ticks(np.linspace(3,9,7))

        nfile=filename.split('.')[-1]
        print('nfile:',nfile)
        n=[]
        n.append(int(nfile))
        t=n[0]*dtdump
        plt.suptitle("{}{:.0f}{}".format('$M_{BH}=10^{8}M_{\odot}$, $\\epsilon=0.5$, $t=$',t,'yr'))


        fig.savefig("./%s.png"%('v'+filename.split('.')[-1])) #save fig as "denoutN.pdf"

