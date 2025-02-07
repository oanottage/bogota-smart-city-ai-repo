# **Geo CRNLOC – Data Dictionary**  

## **Description**  
This dataset provides geographical and legislative information associated with CRNLOC data. It includes identifiers, ranking values, location-specific data, legal references, and geometric attributes. The dataset contains **190 entries**, making it suitable for spatial and regulatory analysis.  

### **Suggested Use Cases:**  
- **Geospatial Analysis**: Mapping and visualizing geographical locations linked to CRNLOC.  
- **Legal and Policy Research**: Analyzing articles, numerals, and descriptions in legislative contexts.  
- **Urban Planning**: Evaluating the distribution and density of specified locations.  
- **Data Validation**: Checking for anomalies in spatial and legislative records.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| OBJECTID                   | Object ID                 | Unique identifier for each record. Stored as `int32`, ranging from **22,401** to **22,590**. |
| CMRANK                     | CRN Rank                  | Rank associated with the record. Stored as `int32`, with values ranging from **1** to **10**. |
| CMRNCONT                   | CRN Count                 | Numeric count related to CRN. Stored as `int32`, ranging from **112** to **23,684**. |
| CMIULOCAL                  | Local Code                | Code assigned to specific localities. Stored as `object`, with **19** distinct values. |
| CMNOMLOCA                  | Local Name                | Name of the locality (e.g., "Engativá"). Stored as `object`, with **19** distinct values. |
| CMRNART                    | Article                   | Legal article reference. Stored as `object`, with **8** distinct values. |
| CMRNNUM                    | Numeral                   | Legal numeral reference. Stored as `object`, with **13** distinct values. |
| CMRNDESCO                  | Description               | Description related to CRN data. Stored as `object`, with **18** distinct values. |
| CMRNMES                    | Month Range               | Time period covered (e.g., "Ene-Dic"). Stored as `object`, with **1** distinct value. |
| CMRNTOTAL                  | Total Count               | Overall total count. Stored as `int32`, with a single value **430,816**. |
| SHAPE.AREA                 | Shape Area                | Geographical area measurement. Stored as `float64`, ranging from **0.00** to **0.02**. |
| SHAPE.LEN                  | Shape Length              | Geographical perimeter measurement. Stored as `float64`, ranging from **0.07** to **0.98**. |
| geometry                   | Geometry                  | Geospatial data in binary format. Stored as `object`. |