# **Geo CRNSCAT – Data Dictionary**  

## **Description**  
This dataset contains geographical and categorical data related to CRNSCAT, including identifiers, rankings, local classifications, legal references, and spatial attributes. The dataset comprises **9,358 entries**, providing a structured representation of CRNSCAT-related geographical and legal information.  

### **Suggested Use Cases:**  
- **Geospatial Analysis**: Mapping and analyzing geographical distributions linked to CRNSCAT.  
- **Legal and Policy Research**: Understanding how articles, numerals, and descriptions apply to different locations.  
- **Categorization and Classification**: Evaluating locations based on their assigned legal and numerical attributes.  
- **Urban and Regional Planning**: Studying the distribution and density of categorized locations.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| OBJECTID                   | Object ID                 | Unique identifier for each record. Stored as `int32`, ranging from **429,121** to **438,478**. |
| CMRANK                     | CRN Rank                  | Ranking assigned to each record. Stored as `int32`, with values from **1** to **10**. |
| CMRNCONT                   | CRN Count                 | Numeric count related to CRN. Stored as `int32`, ranging from **1** to **3,350**. |
| CMIUSCAT                   | Local Classification ID   | ID assigned to each local classification. Stored as `object`, with **1,078** distinct values. |
| CMNOMSCAT                  | Local Classification Name | Name of the local classification (e.g., "Puerto Rico"). Stored as `object`, with **1,018** distinct values. |
| CMRNART                    | Article                   | Legal article reference. Stored as `object`, with **32** distinct values. |
| CMRNNUM                    | Numeral                   | Legal numeral reference. Stored as `object`, with **34** distinct values. |
| CMRNDESCO                  | Description               | Detailed description related to CRN data. Stored as `object`, with **114** distinct values. |
| CMRNMES                    | Month Range               | Time period covered (e.g., "Ene-Dic"). Stored as `object`, with **1** distinct value. |
| CMRNTOTAL                  | Total Count               | Total number associated with each record. Stored as `int32`, with a single value **444,219**. |
| SHAPE.AREA                 | Shape Area                | Geographic area measurement. Stored as `float64`, ranging from **0.00** to **0.00**. |
| SHAPE.LEN                  | Shape Length              | Geographic perimeter measurement. Stored as `float64`, ranging from **0.00** to **0.36**. |
| geometry                   | Geometry                  | Geospatial data stored in binary format. Stored as `object`. |