#inspired from this video
#https://www.youtube.com/watch?v=_T0l015ecK4

import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt

#data retrieval variables
start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()
stock = "FB"
data_source = 'yahoo'

# capture data to data frame
prices = web.DataReader(stock, data_source, start, end)['Close']
returns = prices.pct_change()
last_price = prices[-1]

# number of simulations
sim_num = 1000
days = 365 * 3

#monte carlo
simulation_df = pd.DataFrame()
for x in range(sim_num):
    counter = 0
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(days):
        if counter == days -1:
            break
        price = price_series(counter) * (1 + np.random.normal(0, daily_vol))
        price_series. append(price)
        counter += 1
    simulation_df[x] = price_series


# produce results on mathplot
fig = plt.figure()
plt.plot(simulation_df)
plt.axhline(y = last _price, color = 'r', linestyle = '-')
plt.xlabel('Time (Days)')
plt.ylabel('Price')
plt.show()