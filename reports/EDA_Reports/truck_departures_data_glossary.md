# Exploratory Data Analysis of Bogotá Public Transport Monthly Usage – Translated Documentation

## Description
This file appears to contain daily usage or passenger counts for a public transport system in Bogotá, Colombia (likely TransMilenio or SITP, given the structure). Each record references a line, station, and entrance/exit, along with a time interval. Then, for each day of the month, there is a corresponding numeric column that (in most cases) shows counts from 0 to an upper bound (e.g., 998). The “MES” column indicates the month, here “NOVIEMBR” (November), and the final columns include a total summation, plus a few unnamed columns that may be placeholders with no data.

**Suggested Use Cases**:
- Ridership or passenger flow analysis for different stations/lines.
- Identifying peak usage days or intervals (e.g., to inform scheduling or resource allocation).
- Integrating with broader city mobility data for planning and policy decisions.
- Data quality or governance checks on daily transport usage records.

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name | Description                                                                                                                                                          |
|------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Línea**              | Line                   | Text field indicating the bus line or route. 13 distinct values (object). Sample: “(11) Zona K.”                                                                     |
| **Estación**           | Station                | Text field describing the station name/code. 152 distinct values (object). Sample: “(06000) Po.”                                                                     |
| **Acceso de Estación**        | Station Access        | Text field describing the station entrance or platform. 422 distinct values (object). Sample: “(01) PLAT2.”                                                          |
| **MES**                | Month                  | Text field identifying the month (object). Only 1 distinct value here, e.g., “NOVIEMBR.”                                                                            |
| **INTERVALO**          | Interval               | Time interval or segment (object). 90 distinct values. Sample: “00:00.”                                                                                             |
| **DÍA 01** … **DÍA 31**| Day 01 … Day 31        | Daily passenger counts or usage (typically float64). Each column represents a calendar day (1–31) within the month. Ranges vary (min = 0, max ≈ 998).                |
| **DÍA 31** (Special)   | Day 31 (Special)       | Note that for “DÍA 31,” sample value is “X,” indicating possibly a special notation or missing data. This column has 1 distinct value and is typed as object.        |
| **Total gener**        | Overall Total          | Summation or aggregate usage for the month (float64). 7,082 distinct values, range 0 – 999.                                                                          |
| **Unnamed: 37**        | Unnamed Column 37      | Empty or placeholder column (float64). No distinct values, min = 0, max = 0.                                                                                        |
| **Unnamed: 38**        | Unnamed Column 38      | Another empty or placeholder column (float64). No distinct values, min = 0, max = 0.                                                                                |

---
