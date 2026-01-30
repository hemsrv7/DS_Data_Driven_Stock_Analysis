import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/processed_csv/stock_data.csv")
print(df.head())
print(df.info())
df["date"] = pd.to_datetime(df["date"])

symbol = df["Ticker"].iloc[0]   # pick one stock

stock_df = df[df["Ticker"] == symbol]

plt.figure()
plt.plot(stock_df["date"], stock_df["close"])
plt.title(f"Closing Price Trend - {symbol}")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.show()

plt.figure()
plt.plot(stock_df["date"], stock_df["volume"])
plt.title(f"Trading Volume - {symbol}")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

stock_df["daily_return"] = stock_df["close"].pct_change()

plt.figure()
plt.hist(stock_df["daily_return"].dropna())
plt.title(f"Daily Return Distribution - {symbol}")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()

monthly = stock_df.resample("M", on="date")["close"].mean()

plt.figure()
plt.plot(monthly.index, monthly.values)
plt.title(f"Monthly Average Close - {symbol}")
plt.xlabel("Month")
plt.ylabel("Avg Close")
plt.show()

monthly_avg = stock_df.groupby("month")["close"].mean()

plt.figure()
plt.plot(monthly_avg.index, monthly_avg.values)
plt.title(f"Monthly Average Closing Price - {symbol}")
plt.xlabel("Month")
plt.ylabel("Average Close Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()