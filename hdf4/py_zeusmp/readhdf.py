#!/usr/bin/env python
#plotting dataoutput from zeus_MP(hdf4 files) 
#

import numpy as np
from pyhdf.SD import *
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pylab import *
import os

for filename in os.listdir("./"):
    if filename.startswith("hdfaa."):

        fo = SD(filename)
        fo_attr=fo.attributes()
        fo_dsets=fo.datasets()
#        print ("len(fo_attr): ", len(fo_attr))
#        print ("len(fo_dsets): ", len(fo_dsets))
#        print ("fo attributes: ", fo_attr.keys())
#        print ("fo datesets: ", fo_dsets.keys(), '\n')

        ds0=fo.select(0)
#        print ("fakeDim0 attributes:", ds0.attributes())
#        print ("ds0.dimensions(): ",ds0.dimensions())
#        print ("ds0[0],ds0[-1]:", ds0[0], ds0[-1])

        ds1=fo.select(1)
#        print ("fakeDim1 attributes:", ds1.attributes())
#        print ("ds1.dimensions(): ",ds1.dimensions())
#        print ("ds1[0],ds1[-1]", ds1[0], ds1[-1])

        ds2=fo.select(2)
#        print ("fakeDim2 attributes:", ds2.attributes())
#        print ("ds2.dimensions(): ",ds2.dimensions())
#        print ("ds0[0],ds2[-1]:", ds2[0], ds2[-1], '\n')

        ds5=fo.select('Data-Set-5')
#        print ("Data-Set-5 attributes:", ds5.attributes())
#        print ("ds5.dimensions(): ",ds5.dimensions().keys())
#        print ("ds5[0:2,0:1,0:1]:", ds5[0:2,0:1,0:1])

        phi=ds0.get()
        theta=ds1.get()
        r=ds2.get()
        #den=ds5.get()
        den=ds5[0]
#        print ("den.shape:", den.shape)

        igrid=len(theta); jgrid=len(r)
        xx=np.zeros((igrid,jgrid),dtype=float)
        yy=np.zeros((igrid,jgrid),dtype=float)
        for i in range(0,igrid):
            for j in range(0,jgrid):
                xx[i,j]=r[j]*np.sin(theta[i])
                yy[i,j]=r[j]*np.cos(theta[i])

        print ("plotting:",filename)
        fig=plt.figure(figsize=(5,6))
        ax=fig.add_subplot(111)
        #pcm=ax.pcolormesh(y1,x1,den1,vmin=-27.,vmax=-25.,cmap=cm.jet)
        pcm=ax.contourf(xx,yy,den,200,vmin=0.0,vmax=1.0,cmap=cm.jet)
        ax.set_xlim(0.,4.)
        ax.set_ylim(-4.,4.)
        #ax.set_xlabel('R')
        #ax.set_ylabel('R')
        #set colorbar:        
        cbar=plt.colorbar(pcm)
        cbar.set_label('$\\rho$')
        gca().set_aspect('equal')
        fig.savefig("./%s.png"%('den'+filename.split('.')[-1])) #save fig as "denoutN.pdf"

        fo.end()
