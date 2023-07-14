from scripts import stoks

ticker = 'TSLA'
start_date = '2010-01-01'
end_date = '2022-12-21'
TSLA_data = stoks.get_stock_data(ticker, start_date, end_date)
print(TSLA_data.tail())
