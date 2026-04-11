# 📊 Superstore Sales Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

A data analytics project exploring retail sales data using Python and SQL.
The goal is to identify profitable segments, loss-making products,
and the impact of discounts on business performance.

---

## 🌐 Live Demo

Check out the interactive Streamlit dashboard:

**[Launch App](https://superstoredataanalytics-daar8sszaksqvhwh25jiuk.streamlit.app/)**

---

## 📊 Table of Contents

- [Project Overview](#-project-overview)
- [Live Demo](#-live-demo)
- [Dataset](#-dataset)
- [Tools & Libraries](#️-tools--libraries)
- [Project Structure](#-project-structure)
- [What I Did](#-what-i-did)
- [Key Findings](#-key-findings)
- [How to Run Locally](#️-how-to-run-locally)

---

## 📖 Project Overview

This project performs end-to-end analysis on the Tableau Sample Superstore dataset.
It covers data cleaning, feature engineering, SQL-based querying using pandasql,
exploratory data analysis with Matplotlib and Seaborn, interactive visualizations
with Plotly, and a live Streamlit dashboard with final business recommendations.

---

## 📦 Dataset

- **Source:** Tableau Sample Superstore (publicly available)
- **Records:** 9,994 rows × 21 columns
- **Period:** 2014 – 2017
- **Domain:** US Retail (Orders, Customers, Products, Sales, Profit)

---

## 🛠️ Tools & Libraries

| Tool / Library | Purpose |
|----------------|---------|
| Python 3 | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Matplotlib | Static visualizations |
| Seaborn | Statistical visualizations |
| Plotly Express | Interactive visualizations |
| Pandasql | SQL queries on DataFrames |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Analysis and exploration |

---

## 📂 Project Structure

```
superstore-sales-analysis/
│
├── sales_analysis.ipynb         # Main analysis notebook
├── app.py                       # Streamlit dashboard
├── Sample - Superstore.csv      # Dataset
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ✅ What I Did

- 🔹 Performed Data Cleaning & Feature Engineering — Shipping Days, Profit Margin %, Year/Month extraction
- 🔹 Used pandasql to run SQL queries directly on DataFrames for business insights
- 🔹 Performed EDA using Matplotlib and Seaborn — category, region and discount analysis
- 🔹 Built 6+ interactive visualizations using Plotly Express
- 🔹 Identified loss-making products and high-discount impact on profitability
- 🔹 Developed a live Streamlit dashboard with dynamic filters (Year, Region, Category)

---

## 🔍 Key Findings

1. **Technology** is the most profitable category with 145K profit and ~17% margin
2. **Furniture** has a margin problem — 742K in sales but only 2.5% profit margin
3. **Tables sub-category** is a net loss maker and should be repriced or discontinued
4. **High discounts (40%+) destroy profitability** — avg profit drops to -$107 per order
5. **West region** outperforms all others in both revenue and profit
6. **Sales grew 51%** from 2014 to 2017 ($484K → $733K)

---

## ⚙️ How to Run Locally

1. Clone this repository
   ```bash
   git clone https://github.com/viraj01-coder/superstore_data_analytics.git
   cd superstore_data_analytics
   ```

2. Install required libraries
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```

4. Open the notebook
   ```bash
   jupyter notebook sales_analysis.ipynb
   ```

---

*Dataset: Tableau Sample Superstore | Author: Virajbhai Mavani*
