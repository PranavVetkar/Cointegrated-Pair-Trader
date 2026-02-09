import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

# 1. Simulate or load BTC and ETH data
df_btc = pd.read_csv('btc_history.csv')['close']
df_eth = pd.read_csv('eth_history.csv')['close']

# 2. Test for Cointegration
score, p_value, _ = coint(df_btc, df_eth)
print(f"--- Cointegration Test ---")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("✅ These assets are cointegrated. Good for Pairs Trading.")
else:
    print("❌ Weak cointegration. Be careful with this pair.")

# 3. Calculate the Spread (Linear Regression)
X = sm.add_constant(df_eth)
model = sm.OLS(df_btc, X).fit()
beta = model.params[0]
spread = df_btc - beta * df_eth

# 4. Calculate Z-Score of the Spread
z_score = (spread - spread.mean()) / spread.std()

# 5. Generate Signals
print(f"\nCurrent Z-Score: {z_score.iloc[-1]:.2f}")

if z_score.iloc[-1] > 2:
    print("📢 SIGNAL: SELL the Spread (Short BTC / Long ETH)")
elif z_score.iloc[-1] < -2:
    print("📢 SIGNAL: BUY the Spread (Long BTC / Short ETH)")
else:
    print("📢 SIGNAL: No clear divergence.")