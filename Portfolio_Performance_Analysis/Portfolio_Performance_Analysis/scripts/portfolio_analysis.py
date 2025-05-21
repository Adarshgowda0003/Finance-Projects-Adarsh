import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Example portfolio: stock tickers and weights
portfolio = {
    'AAPL': 0.4,
    'MSFT': 0.3,
    'GOOGL': 0.3
}

# Download historical price data for the portfolio stocks
tickers = list(portfolio.keys())
data = yf.download(tickers, start='2023-01-01', end='2024-01-01')['Adj Close']

# Calculate daily returns
returns = data.pct_change().dropna()

# Calculate portfolio daily returns
weights = pd.Series(portfolio)
portfolio_returns = returns.dot(weights)

# Calculate cumulative returns
cumulative_returns = (1 + portfolio_returns).cumprod()

# Plot cumulative returns
plt.figure(figsize=(10,6))
plt.plot(cumulative_returns, label='Portfolio Growth')
plt.title('Portfolio Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Growth')
plt.legend()
plt.grid(True)
plt.savefig('../visuals/portfolio_growth.png')
plt.show()
