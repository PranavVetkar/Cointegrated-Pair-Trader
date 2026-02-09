# 🔗 Cointegrated Pairs Trading Analyzer

A Python-based **statistical arbitrage research tool** that analyzes whether two crypto assets move together in a stable long-term relationship and generates **pairs trading signals** based on spread divergence.

This project applies **cointegration testing + mean reversion theory** to crypto markets.

---

## 🚀 What This Project Does

- Loads historical BTC & ETH price data
- Tests for **cointegration** using statistical methods
- Builds a **linear spread model**
- Calculates spread **Z-score**
- Generates **pairs trading signals**
- Identifies mean-reversion opportunities

---

## 🧠 What is Pairs Trading?

Pairs trading is a **market-neutral strategy** where you:

- Long the undervalued asset
- Short the overvalued asset
- Profit when prices converge again

Key assumption → The pair is **cointegrated**.

---

## 📊 Analysis Pipeline

### 1️⃣ Load Price Data

- BTC → btc_history.csv
- ETH → eth_history.csv

---

### 2️⃣ Cointegration Test

Uses:

- statsmodels.tsa.stattools.coint

Output:

- **P-value < 0.05** → Strong cointegration
- **P-value ≥ 0.05** → Weak relationship

---

### 3️⃣ Spread Modeling

A linear regression estimates the hedge ratio:

- BTC = β × ETH + constant
- Spread = BTC − β × ETH

This spread should mean-revert if cointegrated.

---

### 4️⃣ Z-Score Calculation

- Z = (Spread − Mean) / Std Dev

Measures how far the spread deviates from equilibrium.

---

## 📢 Signal Logic

| Z-Score | Signal |
|--------|--------|
| > +2 | SELL spread (Short BTC / Long ETH) |
| < −2 | BUY spread (Long BTC / Short ETH) |
| Between | No trade |

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pandas**
- **NumPy**
- **Statsmodels**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Cointegrated-Pair-Trader.git
cd Cointegrated-Pair-Trader
