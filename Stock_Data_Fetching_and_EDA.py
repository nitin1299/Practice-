#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Core libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Make plots look clean
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

print('Setup complete!')


# In[3]:


# Define the tickers we want to analyse
# Mix of tech (AAPL, MSFT, GOOGL) and finance (JPM, GS)
tickers = ['AAPL', 'MSFT', 'GOOGL', 'JPM', 'GS']

# Fetch 2 years of daily data
# 'Adj Close' accounts for splits and dividends — always use this for return calculations
data = yf.download(tickers, start='2023-01-01', end='2025-01-01', auto_adjust=True)

# We only need the adjusted closing prices for now
prices = data['Close']
prices.head()


# In[4]:


# Check shape, missing values, and basic stats
print(f'Date range: {prices.index[0].date()} to {prices.index[-1].date()}')
print(f'Trading days: {len(prices)}')
print(f'\nMissing values per stock:')
print(prices.isnull().sum())
print(f'\nBasic statistics:')
prices.describe().round(2)


# In[5]:


# Normalise: divide each price by the first price, multiply by 100
normalised = (prices / prices.iloc[0]) * 100

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
normalised.plot(ax=ax, linewidth=1.5)
ax.set_title('Normalised Stock Performance (Base = 100)', fontsize=14, fontweight='bold')
ax.set_ylabel('Normalised Price')
ax.set_xlabel('')
ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5, label='Starting value')
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()


# In[6]:


# Calculate daily returns
returns = prices.pct_change().dropna()

# Show summary statistics
print('Daily Return Statistics')
print('=' * 50)
summary = pd.DataFrame({
    'Mean (%)': (returns.mean() * 100).round(4),
    'Std Dev (%)': (returns.std() * 100).round(4),
    'Min (%)': (returns.min() * 100).round(2),
    'Max (%)': (returns.max() * 100).round(2),
})
summary


# In[7]:


fig, axes = plt.subplots(1, len(tickers), figsize=(18, 4), sharey=True)

for i, ticker in enumerate(tickers):
    axes[i].hist(returns[ticker], bins=50, alpha=0.7, color=f'C{i}', edgecolor='white')
    axes[i].set_title(ticker, fontweight='bold')
    axes[i].axvline(x=0, color='red', linestyle='--', alpha=0.5)
    if i == 0:
        axes[i].set_ylabel('Frequency')

fig.suptitle('Distribution of Daily Returns', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()


# In[8]:


# Calculate correlation matrix of returns
corr_matrix = returns.corr()

# Plot as a heatmap
fig, ax = plt.subplots(figsize=(8, 6))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Hide upper triangle (it's symmetric)
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt='.2f',
    cmap='RdYlBu_r',
    center=0,
    vmin=-1, vmax=1,
    square=True,
    linewidths=1,
    ax=ax
)
ax.set_title('Return Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()


# In[9]:


# Cumulative return = product of (1 + daily returns) over time
cumulative = (1 + returns).cumprod()

fig, ax = plt.subplots(figsize=(14, 7))
cumulative.plot(ax=ax, linewidth=1.5)
ax.set_title('Cumulative Returns (Growth of $1)', fontsize=14, fontweight='bold')
ax.set_ylabel('Portfolio Value ($)')
ax.set_xlabel('')
ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5)
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()

# Print total return for each stock
print('\nTotal Return over period:')
for ticker in tickers:
    total_ret = (cumulative[ticker].iloc[-1] - 1) * 100
    print(f'  {ticker}: {total_ret:+.1f}%')


# In[10]:


# 30-day rolling standard deviation, annualised
# We multiply by sqrt(252) because there are ~252 trading days in a year
rolling_vol = returns.rolling(window=30).std() * np.sqrt(252)

fig, ax = plt.subplots(figsize=(14, 7))
rolling_vol.plot(ax=ax, linewidth=1.2)
ax.set_title('30-Day Rolling Annualised Volatility', fontsize=14, fontweight='bold')
ax.set_ylabel('Annualised Volatility')
ax.set_xlabel('')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()


# In[ ]:




