# http://pandas.pydata.org/
import pandas as pd

# import csv
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
df = pd.read_csv('data/BTC.csv')
# Just to display the first 5 lines
# df.head(5)

# rename column 'time' to 'unix_time' (https://en.wikipedia.org/wiki/Unix_time)
df.rename(inplace=True, columns={'time': 'unix_time'})

# convert second precision to nanosecond precision (add a column 'time in nanoseconds')
df['time_ns'] = df['unix_time'].apply(lambda x: x * 1000000000)
# Col 'time' dtype is int64 (check with `df.dtypes`)
# df.head(5)

# add column timestamp and convert int to Timestamp 
# (very costly operation)
# df['timestamp'] = df['unix_time'].apply(lambda x: pd.to_datetime(x, unit='s'))
# cheaper operation -- UTC TZ
df['timestamp'] = df['unix_time'].apply(lambda x: pd.Timestamp.utcfromtimestamp(x) )

# export as csv
ns_precision = df
ns_precision.to_csv('data/BTC_ns.csv', index=False)
