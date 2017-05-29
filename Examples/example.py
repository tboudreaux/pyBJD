from astropy import units as u
from astropy.coordinates import SkyCoord
import pandas as pd
import numpy as np
import os
from pyBJD import getBJD

# Given some root folder (The exampleFiles.zip file -- to use unzip that in local directory)

JD = []
rBJD = []
Date = []
UTC = []
for root, dirs, f in os.walk('.', topdown=False):
    for i in f:
        if 'CS1246' in i:
            name = "{}/{}".format(root, i)
            JD.append(open(name, 'rb').readlines()[3].split('\t')[1].strip('='))
            rBJD.append(open(name, 'rb').readlines()[6].split('\t')[1].strip('='))
            Date.append(open(name, 'rb').readlines()[1].split('\t')[1].strip('=').split('-'))
            UTC.append(open(name, 'rb').readlines()[2].split('\t')[1].strip('=').split(':'))
# JD = np.array(JD).astype(np.float)
rBJD = np.array(rBJD).astype(np.float)

c = SkyCoord('12h49m37.690000s', '-63d32m8.9900000s', frame='icrs')

params = [JD, "{}:{}:{}".format(str(int((c.ra.hms)[0])), str(int((c.ra.hms)[1])), str((c.ra.hms)[2])),
        "{}:{}:{}".format(str(int((c.dec.dms)[0])), str(abs(int((c.dec.dms)[1]))), str(abs((c.dec.dms)[2]))),
        '-30.1716', '-70.8009', '2172']

#print params
print params[0], params[1], params[2], params[3], params[4], params[5]
kwargs = {
    "iJD": params[0],
    "iRA": params[1],
    "iDEC": params[2],
    "iLAT": params[3], 
    "iLON": params[4],
    "iALT": params[5]
}
bjd = GetBJD(**kwargs)
print bjd
