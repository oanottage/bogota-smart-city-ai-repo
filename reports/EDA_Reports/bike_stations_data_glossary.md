# Bike Stations Data Dictionary – Translated Documentation  

## Description  
This dataset provides information about bike stations in Bogotá, Colombia, including their infrastructure type, associated TransMilenio trunk lines, and usage statistics (e.g., average daily usage, capacity). The dataset contains 27 entries, but most columns are sparsely populated (2.67%). Unnamed columns (e.g., `Unnamed: 7` to `Unnamed: 25`) are entirely empty and likely artifacts from data processing.  

**Suggested Use Cases**:  
- Bike station capacity planning and optimization.  
- Integration with public transit systems (e.g., TransMilenio).  
- Usage pattern analysis (e.g., weekday vs. weekend trends).  
- Infrastructure improvement prioritization (e.g., high-demand stations).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| BiciEstación                  | Bike_Station                    | Station name (e.g., `San Mateo`). `object`, 27 distinct values, 2.67% populated. |
| Tipo de infraestructura       | Infrastructure_Type             | Station type (e.g., `Estación`). `object`, 3 distinct values, 2.67% populated. |
| Troncal de TransMilenio       | TransMilenio_Trunk              | Associated TransMilenio trunk line (e.g., `NQS Sur`). `object`, 10 distinct values, 2.67% populated. |
| Promedio Hábil                | Weekday_Average                 | Average weekday usage. `float64`, range: 0.0–642.0, 2.67% populated.       |
| Promedio Sábado               | Saturday_Average                | Average Saturday usage. `float64`, range: 0.0–758.0, 2.67% populated.      |
| Promedio Domingos y festivos  | Sunday_Holiday_Average          | Average Sunday/holiday usage. `float64`, range: 0.0–343.0, 2.67% populated. |
| Cupos                         | Capacity                        | Station capacity (e.g., 1.449–961). `float64`, 2.67% populated.            |
| Unnamed: 7–Unnamed: 25        | Unnamed_Columns                 | Empty columns (0.0% populated). Likely artifacts from data processing.     |

---  
*Notes:*  
- All named columns are only 2.67% populated, suggesting the dataset may be incomplete or require further cleaning.  
- `TransMilenio_Trunk` indicates integration with Bogotá’s bus rapid transit system.  
- Unnamed columns should be removed or investigated for potential data quality issues.  