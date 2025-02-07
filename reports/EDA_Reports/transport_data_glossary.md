# **Transport – Data Dictionary**  

## **Description**  
This dataset contains transportation-related data, including bus lines, station access points, timestamps, and daily passenger counts. The dataset comprises **50,501 entries**, providing structured information for analyzing public transport usage trends.  

### **Suggested Use Cases:**  
- **Public Transport Analysis**: Understanding trends in passenger usage over time.  
- **Infrastructure Planning**: Evaluating demand across different stations and bus lines.  
- **Operational Efficiency**: Assessing the effectiveness of scheduling and route allocation.  
- **Data Validation**: Ensuring completeness and accuracy in transit records.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| Línea                      | Line                       | Bus line identifier. Stored as `object`, with **13** distinct values. |
| Estación                   | Station                    | Name of the station (e.g., "Portal Eldorado"). Stored as `object`, with **152** distinct values. |
| Acceso de Estación         | Station Access             | Detailed station access points. Stored as `object`, with **422** distinct values. |
| MES                        | Month                      | Recorded month (e.g., "Noviembre"). Stored as `object`, with **1** distinct value. |
| INTERVALO                  | Time Interval              | Time range of recorded data (e.g., "00:00"). Stored as `object`, with **90** distinct values. |
| DÍA 01 - DÍA 31            | Daily Passenger Count      | Passenger count per day of the month. Stored as `float64`, ranging from **0** to **998**. |
| Total general              | Total Monthly Count        | Total passenger count for the month. Stored as `float64`, with values up to **999**. |
| Unnamed: 37, Unnamed: 38   | Unnamed Columns            | Extra fields with `float64` values, potentially unused. |