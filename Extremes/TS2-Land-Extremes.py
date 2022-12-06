
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:12:01 2021

@author: gkrinner
"""

import numpy as np
from xlrd import open_workbook
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path
from matplotlib.textpath import TextToPath
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# iselectlevels = [0, 1, 2, 4]
# iselectlevels = [0, 2, 3, 4]
# iselectlevels = [0, 1, 2, 3]
iselectlevels = [0, 1, 2, 3, 4]
dx = .1
sizeref = 100
size0 = .25*sizeref
size1 = 1*sizeref
size2 = 1.5*sizeref
size3 = 2.25*sizeref
large = 2.3*dx

def get_positions(dx0,iselectlevels,levels):

    npos = len(iselectlevels)
    retpos = np.empty((npos),np.float)

    if (False):
        retpos = np.arange(dx0, np.float(npos)+dx0)
    else:
        for i in range(npos):
           retpos[i] = dx0 + levels[iselectlevels[i]]
    
    return retpos

fp = FontProperties(fname=r"Font Awesome 5 Free-Solid-900.otf")

symbols = dict(thermometer = "\uf2c9",
               cloudshowersheavy = "\uf740",
               hourglass = "\uf253",
               stopwatch = "\uf2f2",
               nowater = "\uf5c7")

def get_marker(symbol):
    v, codes = TextToPath().get_text_path(fp, symbol)
    v = np.array(v)
    mean = np.mean([np.max(v,axis=0), np.min(v, axis=0)], axis=0)
    return Path(v-mean, codes, closed=False)

nGWL = 5
nrange = 5

i50 = 0; i17 = 1; i83 = 2; i5 = 3; i95 = 4
# iup = i83; ilo = i17
iup = i95; ilo = i5

c10 = "sandybrown"
c50 = "saddlebrown"

nsGWL = len(iselectlevels)

FreqTXx10 = np.empty((nGWL,nrange),np.float)
FreqTXx50 = np.empty((nGWL,nrange),np.float)
IntTXx10 = np.empty((nGWL,nrange),np.float)
IntTXx50 = np.empty((nGWL,nrange),np.float)

FreqRx1day10 = np.empty((nGWL,nrange),np.float)
FreqRx1day50 = np.empty((nGWL,nrange),np.float)
IntRx1day10 = np.empty((nGWL,nrange),np.float)
IntRx1day50 = np.empty((nGWL,nrange),np.float)

FreqDrought10s = np.empty((nsGWL,nrange),np.float)
IntDrought10s = np.empty((nsGWL,nrange),np.float)

wb = open_workbook('Changes in txx_baseline0deg.xlsx')
levels = []
for igwl,s in enumerate(wb.sheets()):
    print ('Sheet:',s.name)
    levels.append(np.float(s.name[0:3]))
    for row in range(s.nrows):
        if ('Global land' in str(s.cell(row,1))):
            for ir in range(nrange):
                FreqTXx10[igwl,ir] = s.cell(row,2+ir).value
                FreqTXx50[igwl,ir] = s.cell(row,7+ir).value
                IntTXx10[igwl,ir] = s.cell(row,12+ir).value
                IntTXx50[igwl,ir] = s.cell(row,17+ir).value

wb = open_workbook('Changes in rx1day_baseline0deg.xlsx')
for igwl,s in enumerate(wb.sheets()):
    for row in range(s.nrows):
        if ('Global land' in str(s.cell(row,1))):
            for ir in range(nrange):
                FreqRx1day10[igwl,ir] = s.cell(row,2+ir).value
                FreqRx1day50[igwl,ir] = s.cell(row,7+ir).value
                IntRx1day10[igwl,ir] = s.cell(row,12+ir).value
                IntRx1day50[igwl,ir] = s.cell(row,17+ir).value

selectlevels = []
for i in iselectlevels:
    selectlevels.append(levels[i])
  
FreqTXx10s = FreqTXx10[iselectlevels]
FreqTXx50s = FreqTXx50[iselectlevels]
IntTXx10s = IntTXx10[iselectlevels]
IntTXx50s = IntTXx50[iselectlevels]

FreqTXx10sError = [FreqTXx10s[:,i50] - FreqTXx10s[:,ilo],
                   FreqTXx10s[:,iup] - FreqTXx10s[:,i50]]
FreqTXx50sError = [FreqTXx50s[:,i50] - FreqTXx50s[:,ilo],
                   FreqTXx50s[:,iup] - FreqTXx50s[:,i50]]
IntTXx10sError = [IntTXx10s[:,i50] - IntTXx10s[:,ilo],
                  IntTXx10s[:,iup] - IntTXx10s[:,i50]]
IntTXx50sError = [IntTXx50s[:,i50] - IntTXx50s[:,ilo],
                  IntTXx50s[:,iup] - IntTXx50s[:,i50]]

FreqRx1day10s = FreqRx1day10[iselectlevels]
FreqRx1day50s = FreqRx1day50[iselectlevels]
IntRx1day10s = IntRx1day10[iselectlevels]
IntRx1day50s = IntRx1day50[iselectlevels]

FreqRx1day10sError = [FreqRx1day10s[:,i50] - FreqRx1day10s[:,ilo],
                      FreqRx1day10s[:,iup] - FreqRx1day10s[:,i50]]
FreqRx1day50sError = [FreqRx1day50s[:,i50] - FreqRx1day50s[:,ilo],
                      FreqRx1day50s[:,iup] - FreqRx1day50s[:,i50]]
IntRx1day10sError = [IntRx1day10s[:,i50] - IntRx1day10s[:,ilo],
                     IntRx1day10s[:,iup] - IntRx1day10s[:,i50]]
IntRx1day50sError = [IntRx1day50s[:,i50] - IntRx1day50s[:,ilo],
                     IntRx1day50s[:,iup] - IntRx1day50s[:,i50]]
               
wb = open_workbook('drought_prone_regions_annual_wrt_1850_1900_frequency.xlsx')
s = wb.sheets()[0]
row0=17
for irow in range(s.nrows-row0):
    for iGWL in range(nsGWL):
        if (float(s.cell(row0+irow,0).value) == float(selectlevels[iGWL])):
            #print(irow+row0, float(levels[iGWL]), s.cell(row0+irow,0).value)
            for ir in range(nrange):
                FreqDrought10s[iGWL,ir] = s.cell(row0+irow,1+ir).value

wb = open_workbook('drought_prone_regions_annual_wrt_1850_1900_intensity.xlsx')
s = wb.sheets()[0]
row0=15
for irow in range(s.nrows-row0):
    for iGWL in range(nsGWL):
        if (float(s.cell(row0+irow,0).value) == float(selectlevels[iGWL])):
            #print(irow+row0, float(levels[iGWL]), s.cell(row0+irow,0).value)
            for ir in range(nrange):
                IntDrought10s[iGWL,ir] = s.cell(row0+irow,1+ir).value
                IntDrought10s[iGWL,ir] *= -1. 

"""
TXx
"""

fig, ax = plt.subplots()

dx0 = -1.5*dx
positions = get_positions(dx0,iselectlevels,levels)
ax.scatter(positions, FreqTXx10s[:,i50],
        marker=get_marker(symbols["stopwatch"]), 
        s = size2, c=c10, edgecolors="none", linewidth=2,
        label="10-year event, frequency")
ax.scatter(positions, FreqTXx10s[:,iup], marker='1', s = size0, c=c10, edgecolors="none", linewidth=1)
ax.scatter(positions, FreqTXx10s[:,ilo], marker='2', s = size0, c=c10, edgecolors="none", linewidth=1)
# ax.errorbar(positions,FreqTXx10s[:,i50],yerr=FreqTXx10sError,fmt=' ',c=c10,elinewidth=1.e-9,capsize=4,capthick=1)

axr = ax.twinx()
dx0 = -.5*dx
positions = get_positions(dx0,iselectlevels,levels)
axr.scatter(positions, IntTXx10s[:,i50],
        marker=get_marker(symbols["thermometer"]), 
        s = size3, c=c10, edgecolors="none", linewidth=2,
        label="10-year event, intensity")
axr.scatter(positions, IntTXx10s[:,iup], marker='1', s = size0, c=c10, edgecolors="none", linewidth=1)
axr.scatter(positions, IntTXx10s[:,ilo], marker='2', s = size0, c=c10, edgecolors="none", linewidth=1)

dx0 = .5*dx
positions = get_positions(dx0,iselectlevels,levels)
ax.scatter(positions, FreqTXx50s[:,i50],
        marker=get_marker(symbols["stopwatch"]), 
        s = size2, c=c50, edgecolors="none", linewidth=2,
        label="50-year event, frequency")
ax.scatter(positions, FreqTXx50s[:,iup], marker='1', s = size0, c=c50, edgecolors="none", linewidth=1)
ax.scatter(positions, FreqTXx50s[:,ilo], marker='2', s = size0, c=c50, edgecolors="none", linewidth=1)

dx0 = 1.5*dx
positions = get_positions(dx0,iselectlevels,levels)
axr.scatter(positions, IntTXx50s[:,i50],
        marker=get_marker(symbols["thermometer"]), 
        s = size3, c=c50, edgecolors="none", linewidth=2,
        label="50-year event, intensity")
axr.scatter(positions, IntTXx50s[:,iup], marker='1', s = size0, c=c50, edgecolors="none", linewidth=1)
axr.scatter(positions, IntTXx50s[:,ilo], marker='2', s = size0, c=c50, edgecolors="none", linewidth=1)

ax.set_ylabel('Relative frequency (Preindustrial=1)')

dx0 = 0.
positions = get_positions(dx0,iselectlevels,levels)
ax.set_xticks(positions)
ax.set_xticklabels(selectlevels)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.tick_params(which='minor',length=15)

# fond
for i in range(nsGWL):
    ax.axvspan(levels[iselectlevels[i]]-large,levels[iselectlevels[i]]+large, alpha=0.1, color='grey')

axr.set_ylabel('Intensity change (°C)')
fig.legend(bbox_to_anchor=(.53, .87), labelspacing=.8)
ax.set_xlabel('Global surface temperature change since 1850-1900 (°C)')
ax.set_title('a) Hot extreme events')
plt.savefig("TXx.pdf")
plt.savefig("TXx.png")


"""
Rx1day
"""

fig, ax = plt.subplots()

dx0 = -1.5*dx
positions = get_positions(dx0,iselectlevels,levels)
ax.scatter(positions, FreqRx1day10s[:,i50],
        marker=get_marker(symbols["stopwatch"]), 
        s = size2, c=c10, edgecolors="none", linewidth=2,
        label="10-year event, frequency")
ax.scatter(positions, FreqRx1day10s[:,iup], marker='1', s = size0, c=c10, edgecolors="none", linewidth=1)
ax.scatter(positions, FreqRx1day10s[:,ilo], marker='2', s = size0, c=c10, edgecolors="none", linewidth=1)

axr = ax.twinx()
dx0 = -.5*dx
positions = get_positions(dx0,iselectlevels,levels)
axr.scatter(positions, IntRx1day10s[:,i50],
        marker=get_marker(symbols["cloudshowersheavy"]), 
        s = size1, c=c10, edgecolors="none", linewidth=2,
        label="10-year event, intensity")
axr.scatter(positions, IntRx1day10s[:,iup], marker='1', s = size0, c=c10, edgecolors="none", linewidth=1)
axr.scatter(positions, IntRx1day10s[:,ilo], marker='2', s = size0, c=c10, edgecolors="none", linewidth=1)

dx0 = .5*dx
positions = get_positions(dx0,iselectlevels,levels)
ax.scatter(positions, FreqRx1day50s[:,i50],
        marker=get_marker(symbols["stopwatch"]), 
        s = size2, c=c50, edgecolors="none", linewidth=2,
        label="50-year event, frequency")
ax.scatter(positions, FreqRx1day50s[:,iup], marker='1', s = size0, c=c50, edgecolors="none", linewidth=1)
ax.scatter(positions, FreqRx1day50s[:,ilo], marker='2', s = size0, c=c50, edgecolors="none", linewidth=1)

dx0 = 1.5*dx
positions = get_positions(dx0,iselectlevels,levels)
axr.scatter(positions, IntRx1day50s[:,i50],
        marker=get_marker(symbols["cloudshowersheavy"]), 
        s = size1, c=c50, edgecolors="none", linewidth=2,
        label="50-year event, intensity")
axr.scatter(positions, IntRx1day50s[:,iup], marker='1', s = size0, c=c50, edgecolors="none", linewidth=1)
axr.scatter(positions, IntRx1day50s[:,ilo], marker='2', s = size0, c=c50, edgecolors="none", linewidth=1)

ax.set_ylabel('Relative frequency (Preindustrial=1)')

dx0 = 0.
positions = get_positions(dx0,iselectlevels,levels)
ax.set_xticks(positions)
ax.set_xticklabels(selectlevels)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.tick_params(which='minor',length=15)

# fond
for i in range(nsGWL):
    ax.axvspan(levels[iselectlevels[i]]-large,levels[iselectlevels[i]]+large, alpha=0.1, color='grey')

axr.set_ylabel('Intensity change (%)')
fig.legend(bbox_to_anchor=(.53, .87), labelspacing=.8)

ax.set_xlabel('Global surface temperature change since 1850-1900 (°C)')
ax.set_title('b) Heavy precipitation events')
plt.savefig("Rx1day.pdf")
plt.savefig("Rx1day.png")

"""
Drought
"""

fig, ax = plt.subplots()

dx0 = -.5*dx
positions = get_positions(dx0,iselectlevels,levels)
ax.scatter(positions, FreqDrought10s[:,i50],
        marker=get_marker(symbols["stopwatch"]), 
        s = size2, c=c10, edgecolors="none", linewidth=2,
        label="10-year event, frequency")
ax.scatter(positions, FreqDrought10s[:,iup], marker='1', s = size0, c=c10, edgecolors="none", linewidth=1)
ax.scatter(positions, FreqDrought10s[:,ilo], marker='2', s = size0, c=c10, edgecolors="none", linewidth=1)

axr = ax.twinx()
dx0 = .5*dx
positions = get_positions(dx0,iselectlevels,levels)
axr.scatter(positions, IntDrought10s[:,i50],
        marker=get_marker(symbols["nowater"]), 
        s = size3, c=c10, edgecolors="none", linewidth=2,
        label="10-year event, intensity")
axr.scatter(positions, IntDrought10s[:,ilo], marker='1', s = size0, c=c10, edgecolors="none", linewidth=1)
axr.scatter(positions, IntDrought10s[:,iup], marker='2', s = size0, c=c10, edgecolors="none", linewidth=1)

ax.set_ylabel('Relative frequency (Preindustrial=1)')

dx0 = 0.
positions = get_positions(dx0,iselectlevels,levels)
ax.set_xticks(positions)
ax.set_xticklabels(selectlevels)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.tick_params(which='minor',length=15)

# fond
for i in range(nsGWL):
    ax.axvspan(levels[iselectlevels[i]]-large,levels[iselectlevels[i]]+large, alpha=0.1, color='grey')

axr.set_ylabel('Amplitude of annual soil moisture decrease (-)')
fig.legend(bbox_to_anchor=(.53, .87), labelspacing=.8)

ax.set_xlabel('Global surface temperature change since 1850-1900 (°C)')
ax.set_title('c) Droughts in drought-prone regions')
plt.savefig("Droughts.pdf")
plt.savefig("Droughts.png")

# special output for Sophie & Peter CSB2

iout = [1,2,4]

print()
print ('Frequency TXx 10y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], FreqTXx10[ilev,i5], FreqTXx10[ilev,i17], FreqTXx10[ilev,i50], FreqTXx10[ilev,i83], FreqTXx10[ilev,i95]))

print()
print ('Intensity TXx 10y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], IntTXx10[ilev,i5], IntTXx10[ilev,i17], IntTXx10[ilev,i50], IntTXx10[ilev,i83], IntTXx10[ilev,i95]))

print()
print ('Frequency TXx 50y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], FreqTXx50[ilev,i5], FreqTXx50[ilev,i17], FreqTXx50[ilev,i50], FreqTXx50[ilev,i83], FreqTXx50[ilev,i95]))

print()
print ('Intensity TXx 50y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], IntTXx50[ilev,i5], IntTXx50[ilev,i17], IntTXx50[ilev,i50], IntTXx50[ilev,i83], IntTXx50[ilev,i95]))

print()
print ('Frequency Rx1day 10y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], FreqRx1day10[ilev,i5], FreqRx1day10[ilev,i17], FreqRx1day10[ilev,i50], FreqRx1day10[ilev,i83], FreqRx1day10[ilev,i95]))

print()
print ('Intensity Rx1day 10y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], IntRx1day10[ilev,i5], IntRx1day10[ilev,i17], IntRx1day10[ilev,i50], IntRx1day10[ilev,i83], IntRx1day10[ilev,i95]))

print()
print ('Frequency Rx1day 50y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], FreqRx1day50[ilev,i5], FreqRx1day50[ilev,i17], FreqRx1day50[ilev,i50], FreqRx1day50[ilev,i83], FreqRx1day50[ilev,i95]))

print()
print ('Intensity Rx1day 50y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], IntRx1day50[ilev,i5], IntRx1day50[ilev,i17], IntRx1day50[ilev,i50], IntRx1day50[ilev,i83], IntRx1day50[ilev,i95]))

print()
print ('Frequency Drought 10y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], FreqDrought10s[ilev,i95], FreqDrought10s[ilev,i83], FreqDrought10s[ilev,i50], FreqDrought10s[ilev,i17], FreqDrought10s[ilev,i5]))

print()
print ('Intensity Drought 10y: 5 17 50 83 95')
for i, ilev in enumerate(iout):
   print("{} °C: {} {} {} {} {}".format(levels[ilev], IntDrought10s[ilev,i95], IntDrought10s[ilev,i83], IntDrought10s[ilev,i50], IntDrought10s[ilev,i17], IntDrought10s[ilev,i5]))
