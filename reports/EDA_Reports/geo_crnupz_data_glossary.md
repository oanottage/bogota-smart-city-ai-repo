# **Geo CRNUPZ – Data Dictionary**  

## **Description**  
This dataset contains geographical and urban planning data related to CRNUPZ, including identifiers, rankings, urban zones, legal references, and spatial attributes. The dataset consists of **1,191 entries**, providing structured information for geospatial and policy analysis.  

### **Suggested Use Cases:**  
- **Geospatial Analysis**: Mapping and analyzing urban zones linked to CRNUPZ.  
- **Urban Planning**: Evaluating zoning classifications and urban infrastructure.  
- **Legal and Policy Research**: Understanding legal articles and numerals in urban contexts.  
- **Data Validation**: Ensuring consistency in spatial records.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| OBJECTID                   | Object ID                 | Unique identifier for each record. Stored as `int32`, ranging from **100,161** to **101,351**. |
| CMRANK                     | CRN Rank                  | Ranking assigned to each record. Stored as `int32`, with values from **1** to **10**. |
| CMRNCONT                   | CRN Count                 | Numeric count related to CRN. Stored as `int32`, ranging from **1** to **10,928**. |
| CMIUUPLA                   | Urban Zone ID             | ID assigned to specific urban zones. Stored as `object`, with **121** distinct values. |
| CMNOMUPLA                  | Urban Zone Name           | Name of the urban zone (e.g., "La Flora"). Stored as `object`, with **121** distinct values. |
| CMRNART                    | Article                   | Legal article reference. Stored as `object`, with **17** distinct values. |
| CMRNNUM                    | Numeral                   | Legal numeral reference. Stored as `object`, with **19** distinct values. |
| CMRNDESCO                  | Description               | Detailed description related to CRN data. Stored as `object`, with **41** distinct values. |
| CMRNMES                    | Month Range               | Time period covered (e.g., "Ene-Dic"). Stored as `object`, with **1** distinct value. |
| CMRNTOTAL                  | Total Count               | Total number associated with each record. Stored as `int32`, with a single value **436,213**. |
| SHAPE.AREA                 | Shape Area                | Geographic area measurement. Stored as `float64`, ranging from **0.00** to **0.02**. |
| SHAPE.LEN                  | Shape Length              | Geographic perimeter measurement. Stored as `float64`, ranging from **0.02** to **0.98**. |
| geometry                   | Geometry                  | Geospatial data stored in binary format. Stored as `object`. |