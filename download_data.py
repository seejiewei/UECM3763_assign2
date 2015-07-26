from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# COLLECT DATA FROM 1/1/2011 TO 1/5/2015 FOR RHB CAPITAL BERHAD
start = dt(2011, 1, 1)
end = dt(2015, 5, 1)
data = DR("1066.KL", 'yahoo', start, end)

# calculate  rhb moving average
rhb = data['Close']
moving_average = pd.rolling_mean(rhb,5)        

#PLOT RHB MOVING AVERAGE
a = len(moving_average)
x_axis = np.arange(a) + 5
y_axis = moving_average
plt.xlabel('Days $n$')
plt.ylabel('5-day Moving Average')
plt.plot(x_axis,y_axis)
plt.title('RHB CAPITAL BERHAD 5-day Moving Average')
plt.show()

# COLLECT DATA FOR KLCI INDEX FOR SAME DURATION
mask = DR("^KLSE", 'yahoo', start, end)

#collect the closing data of RHB CAPITAL BERHAD and KLCI
combine = ['1066.KL', '^KLSE']
rhb_klse_close_value = DR(combine, 'yahoo', start, end)['Close']

 # calculate correlation between RHB CAPITAL BERHAD and KLCI Index
correlation = rhb_klse_close_value.corr()
print ('Correlation between RHB CAPITAL BERHAD and KLCI Index =')
print(correlation)