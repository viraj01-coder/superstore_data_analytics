# Superstore Sales Analysis

A data analytics project exploring retail sales data using Python and SQL.
The goal is to identify profitable segments, loss-making products,
and the impact of discounts on business performance.

---

## Live Demo

Check out the interactive Streamlit dashboard:

**[Launch App](https://superstoredataanalytics-daar8sszaksqvhwh25jiuk.streamlit.app/)**

---

## Table of Contents
- [Project Overview](#project-overview)
- [Live Demo](#live-demo)
- [Dataset](#dataset)
- [Tools & Libraries](#tools--libraries)
- [Project Structure](#project-structure)
- [Key Findings](#key-findings)
- [How to Run Locally](#how-to-run-locally)

---

## Project Overview

This project performs end-to-end analysis on the Tableau Sample Superstore dataset.
It covers data cleaning, feature engineering, SQL-based querying using pandasql,
interactive visualizations with Plotly, and a live Streamlit dashboard
with final business recommendations.

---

## Dataset

- **Source:** Tableau Sample Superstore (publicly available)
- **Records:** 9,994 rows × 21 columns
- **Period:** 2014 – 2017
- **Domain:** US Retail (Orders, Customers, Products, Sales, Profit)

---

## Tools & Libraries

| Tool / Library | Purpose |
|----------------|---------|
| Python 3 | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Plotly Express | Interactive visualizations |
| pandasql | SQL queries on DataFrames |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Analysis and exploration |

---

## Project Structure

```
superstore-sales-analysis/
│
├── sales_analysis.ipynb       # Main analysis notebook
├── app.py                     # Streamlit dashboard
├── Sample - Superstore.csv    # Dataset
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Key Findings

1. **Technology** is the most profitable category with 145K profit and ~17% margin
2. **Furniture** has a margin problem — 742K in sales but only 2.5% profit margin
3. **Tables sub-category** is a net loss maker and should be repriced or discontinued
4. **High discounts (40%+) destroy profitability** — avg profit drops to -107 per order
5. **West region** outperforms all others in both revenue and profit
6. **Sales grew 51%** from 2014 to 2017 (484K to 733K)

---

## How to Run Locally

1. Clone this repository
   ```
   git clone https://github.com/your-username/superstore-sales-analysis.git
   ```

2. Install required libraries
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app
   ```
   streamlit run app.py
   ```

4. open the notebook
   ```
   jupyter notebook sales_analysis.ipynb
   ```

---



---

*Dataset: Tableau Sample Superstore | Author: Your Name*
