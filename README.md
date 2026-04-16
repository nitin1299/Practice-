# Stock Data Fetching and Exploratory Data Analysis (EDA)

A Python project that fetches historical stock market data and performs exploratory data analysis on a portfolio of tech and finance stocks.

## Overview

This project analyses 2 years of daily stock data (Jan 2023 to Jan 2025) for five major companies across two sectors:

**Tech:** Apple (AAPL), Microsoft (MSFT), Alphabet/Google (GOOGL)

**Finance:** JPMorgan Chase (JPM), Goldman Sachs (GS)

## What This Project Does

- **Fetches real-time stock data** from Yahoo Finance using the `yfinance` library
- - **Normalised price comparison** -- compares stock performance on an equal footing (base = 100)
  - - **Daily return analysis** -- calculates and visualises return distributions for each stock
    - - **Correlation analysis** -- builds a heatmap to show how stock returns move together
      - - **Cumulative return tracking** -- shows the growth of $1 invested in each stock over the period
        - - **Rolling volatility analysis** -- plots 30-day annualised volatility to track risk over time
         
          - ## Visualisations Included
         
          - 1. Normalised Stock Performance Chart
            2. 2. Daily Return Distribution Histograms
               3. 3. Return Correlation Heatmap
                  4. 4. Cumulative Returns (Growth of $1)
                     5. 5. 30-Day Rolling Annualised Volatility
                       
                        6. ## Tech Stack
                       
                        7. - **Python**
                           - - **pandas** -- data manipulation
                             - - **NumPy** -- numerical computations
                               - - **matplotlib** and **seaborn** -- data visualisation
                                 - - **yfinance** -- stock data API
                                  
                                   - ## How to Run
                                  
                                   - 1. Clone this repository
                                     2. 2. Install the required libraries: `pip install pandas numpy matplotlib seaborn yfinance`
                                        3. 3. Run the script: `python Stock_Data_Fetching_and_EDA.py`
                                          
                                           4. ## Author
                                          
                                           5. **Nitin** -- [GitHub Profile](https://github.com/nitin1299)
