# 📈 Stock Market Dashboard Using Machine Learning in Python

A web-based Stock Market Dashboard developed using **Python**, **Streamlit**, and **Yahoo Finance (yfinance)**. The application enables users to analyze stock prices, visualize historical trends, calculate moving averages, and identify market trends using basic machine learning concepts and data analysis techniques.

---

## 🚀 Features

* Search stocks using ticker symbols
* Select different historical time periods
* View real-time historical stock data
* Interactive stock price visualization
* 20-Day Moving Average (MA20)
* 50-Day Moving Average (MA50)
* Market trend prediction:

  * Bullish Trend
  * Bearish Trend
  * Sideways Trend

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* yFinance

---

## 📂 Project Structure

```text
Stock-Market-Dashboard/
│
├── stock_dashboard.py
├── requirements.txt
└── README.md
```

---

## 📦 Installation

Install the required libraries:

```bash
pip install streamlit yfinance pandas
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. Open Terminal or Command Prompt.
2. Navigate to the project folder.

```bash
cd Stock-Market-Dashboard
```

3. Run the application.

```bash
streamlit run stock_dashboard.py
```

If your Python file is named **stock_dashboard(1).py**, use:

```bash
streamlit run "stock_dashboard(1).py"
```

4. Your browser will automatically open the Streamlit application.

---

## 📊 Example Stock Symbols

| Company                   | Symbol      |
| ------------------------- | ----------- |
| Apple                     | AAPL        |
| Tesla                     | TSLA        |
| Microsoft                 | MSFT        |
| Google                    | GOOGL       |
| Amazon                    | AMZN        |
| Infosys                   | INFY.NS     |
| Reliance Industries       | RELIANCE.NS |
| Tata Consultancy Services | TCS.NS      |

---

## 📈 Trend Analysis

The dashboard compares the latest stock closing price with the 20-day and 50-day moving averages.

* **Bullish Trend:** Latest Price > MA20 > MA50
* **Bearish Trend:** Latest Price < MA20 < MA50
* **Sideways Trend:** Any other market condition

---

## 👨‍💻 Author

**Rathesh R**

M.Sc Computer Technology

---

## 📄 License

This project is developed for educational and academic purposes.
