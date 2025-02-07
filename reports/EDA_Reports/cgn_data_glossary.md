# **CGN – Data Dictionary**  

## **Description**  
This dataset provides financial accounting information, including account codes, initial and final balances, and movement details (debits and credits). It contains **998 entries** with a variety of numeric values related to financial transactions. The dataset captures financial activity in a structured format, useful for financial analysis and reporting.  

### **Suggested Use Cases:**  
- **Financial Trend Analysis**: Identifying patterns in account movements over time.  
- **Accounting Reconciliation**: Verifying balances against financial records.  
- **Anomaly Detection**: Spotting irregular transactions based on extreme values.  
- **Budgeting & Forecasting**: Estimating future financial performance based on past trends.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| Codigo contable            | Accounting Code          | Unique identifier for financial accounts. Stored as `int64`, with a range from **100000** to **991590**. |
| Nombre cuenta              | Account Name            | Name of the financial account (e.g., "ACTIVOS"). Stored as `object`, with **726** distinct values. |
| Saldo inicial              | Initial Balance         | Opening balance for each account. Stored as `float64`, with values ranging from **-1.24E+12** to **2.18E+15**. |
| Movimiento debito          | Debit Movement         | Total debit transactions for the account. Stored as `float64`, with values from **0** to **5.04E+14**. |
| Movimiento credito         | Credit Movement        | Total credit transactions for the account. Stored as `float64`, with values from **0** to **4.88E+14**. |
| Saldo final               | Final Balance          | Closing balance for each account. Stored as `float64`, ranging from **-1.30E+12** to **2.20E+15**. |
| Corriente                 | Current Assets         | Portion of the balance classified as current assets. Stored as `float64`, ranging from **-1.29E+12** to **1.25E+15**. |
| No corriente              | Non-current Assets     | Portion of the balance classified as non-current assets. Stored as `float64`, with values from **-1.30E+12** to **2.07E+15**. |