# http://pandas.pydata.org/
import pandas as pd

# import csv
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
df = pd.read_csv('data/BTC.csv')
# Just to display the first 5 lines
# df.head(5)

# convert second precision to nanosecond precision
# df['time'] = [str(df['time'][t]) + "000000000" for t in range(len(df))]
df['time'] = df['time'].apply(lambda x: x * 1000000000)
# Col 'time' dtype is int64 (check with `df.dtypes`)
# df.head(5)

# export as csv
ns_precision = df
ns_precision.to_csv('data/BTC_ns.csv', index=False)
