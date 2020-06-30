import numpy as n
import matplotlib.pyplot as plt
datafile = 'cassini_coords.txt'
scdat = n.recfromtxt(datafile, skip_header=103, skip_footer=47,
                      names=['date', 'time', 'hlon', 'hlat', 'r', 'rdot'])
print(scdat.dtype.names)
print(scdat[0])

plt.plot(scdat.r, scdat.hlat)
print('The mean of r is: ', n.mean(scdat.r))
print('The standard deviation of r is: ', n.std(scdat.r))