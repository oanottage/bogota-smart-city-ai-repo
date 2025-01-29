# Accident Dictionary Data Dictionary – Translated Documentation  

## Description  
This document provides metadata for a dataset related to traffic incidents ("Siniestros") in Bogotá, Colombia. It defines attributes across 3 distinct sheets (indicated by the `HOJA` column), including field names, codes, and their descriptions. All columns are fully populated (100%), with 211 entries total.  

**Suggested Use Cases**:  
- Dataset documentation for internal or external stakeholders.  
- Data governance or quality assurance workflows.  
- Integration with accident analysis pipelines (e.g., joining with actor/victim datasets using `CODIGO`).  

---

## Data Glossary  

| Column_Name (Original) | Translated_Column_Name | Description                                                                 |
|-------------------------|-------------------------|-----------------------------------------------------------------------------|
| HOJA                    | Sheet                   | Name of the dataset sheet (e.g., `SINIESTROS`). `object`, 3 distinct values.|
| CAMPO                   | Field                   | Column name in the dataset (e.g., `GRAVEDAD`). `object`, 9 distinct values. |
| CODIGO                  | Code                    | Numeric identifier for the field (e.g., `1`). `int64`, 137 distinct values. |
| DESCRIPCION             | Description             | Explanation of the field (e.g., "Con Muertos" = "With Deaths"). `object`, 207 distinct values. |

---  
*Notes:*  
- "Con Muertos" translates to "With Deaths," indicating severity classifications.  
- Sheets likely categorize data (e.g., accidents, vehicles, victims) based on the `HOJA` distinct values.  
- `CODIGO` values range from 0 to 506, suggesting a comprehensive coding system for accident attributes.  