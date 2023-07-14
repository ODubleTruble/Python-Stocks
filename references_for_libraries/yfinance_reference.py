import yfinance as yf

ticker = 'TSLA'

start_date = '2020-01-01'
end_date = '2021-12-31'

# Downloads historical data on the ticker from the start to end date.
# "data" is stored as a pandas dataframe.
data = yf.download(ticker, start_date, end_date)

print('\n----------------------------------------------------------------------------------')
print(f'The data immediately after downloading it:\n{data.head()}')
print('----------------------------------------------------------------------------------')

# Currently the indexes of the dataframe "data" are strings representing the date the candle is from.

# Turns the indexes into integers starting at 0 and counting up, like normal list indexes.
# "inplace" being True tells it to modify the existing dataframe rather than making a new one.
# The current indexes, which are the dates, are turned into a new column. 
data.reset_index(inplace=True)

print('\n----------------------------------------------------------------------------------')
print(f'Resets the indexes:\n{data.head()}')
print('----------------------------------------------------------------------------------')

# * You can use .to_csv on the data to save it as a csv file. 
#data.to_csv('raw data on the ticker.csv')
