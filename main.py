# main.py

import numpy as np
import requests
import pandas as pd
from scipy.stats import norm, t

# Function to fetch live asset prices using an API (example using Alpha Vantage)
def fetch_asset_prices(api_key, symbols):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "apikey": api_key,
        "outputsize": "compact",  # Adjust as needed
        "datatype": "json"
    }
    asset_data = {}

    for symbol in symbols:
        params["symbol"] = symbol
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()["Time Series (Daily)"]
            df = pd.DataFrame(data).transpose()
            df.index = pd.to_datetime(df.index)
            df["close"] = df["4. close"].astype(float)
            asset_data[symbol] = df["close"]
        else:
            print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")

    return asset_data

# Function to compute daily returns from asset prices
def compute_daily_returns(asset_data):
    returns = {}
    for symbol, prices in asset_data.items():
        returns[symbol] = prices.pct_change().dropna()
    return returns

# Function to estimate parametric VaR using Monte Carlo simulation
def monte_carlo_var(portfolio_returns, alpha, horizon_days):
    mu = np.mean(portfolio_returns)
    sigma = np.std(portfolio_returns)
    z_alpha = norm.ppf(1 - alpha)
    var_mc = mu - sigma * z_alpha * np.sqrt(horizon_days)
    return var_mc

# Function to estimate non-parametric VaR using historical simulation
def historical_simulation_var(portfolio_returns, alpha):
    var_hs = np.percentile(portfolio_returns, 100 * (1 - alpha))
    return var_hs

# Example usage
if __name__ == "__main__":
    # Replace with your Alpha Vantage API key
    api_key = "your_api_key_here"
    symbols = ["AAPL", "GOOGL", "MSFT"]  # Example symbols
    
    # Fetch live asset prices
    asset_data = fetch_asset_prices(api_key, symbols)
    
    # Compute daily returns
    returns = compute_daily_returns(asset_data)
    
    # Combine all returns into a single portfolio returns array (example: equally weighted portfolio)
    portfolio_returns = np.mean([returns[symbol] for symbol in symbols], axis=0)
    
    # Parameters
    alpha = 0.05  # 95% confidence level
    horizon_days = 1  # 1-day horizon
    
    # Compute VaR using Monte Carlo simulation
    var_mc = monte_carlo_var(portfolio_returns, alpha, horizon_days)
    
    # Compute VaR using historical simulation
    var_hs = historical_simulation_var(portfolio_returns, alpha)
    
    # Print results
    print(f"Parametric VaR (Monte Carlo): {var_mc}")
    print(f"Non-parametric VaR (Historical Simulation): {var_hs}")
