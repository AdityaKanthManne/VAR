# VAR
Value-at-Risk (VaR) Estimation Model for Multi-Asset Portfolio
Setup Instructions:

Clone the repository.

Install dependencies from requirements.txt.

Obtain an API key from Alpha Vantage (or your preferred financial data provider).

Replace "your_api_key_here" in main.py with your actual API key.

Usage:

Run main.py to fetch live asset prices, compute daily returns, and estimate VaR using Monte Carlo and Historical Simulation methods.

Customise symbols, alpha levels, and horizon days as per your requirements.

Project Enhancements:

Add error handling and retry mechanisms for API requests.

Include additional risk metrics like CVaR, skewness, kurtosis, and drawdown calculations.

Implement visualisation using libraries like Matplotlib or Plotly to display results.

Extend the project to handle multiple portfolios, optimise computation with parallel processing, or integrate with a database for data storage.
