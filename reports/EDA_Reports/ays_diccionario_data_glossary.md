# Accident Dictionary Data Dictionary – Translated Documentation  

## Description  
This document provides metadata for a dataset related to traffic incidents ("Siniestros") in Bogotá, Colombia. It defines attributes across 3 distinct sheets (indicated by the `Hoja` column), including primary keys, field names, and their descriptions. All columns are fully populated (100%), with 110 entries total.  

**Suggested Use Cases**:  
- Dataset documentation for internal or external stakeholders.  
- Data governance or quality assurance workflows.  
- Integration with accident analysis pipelines (e.g., joining with actor/victim datasets using `Codigo_Accidente`).  

---

## Data Glossary  

| Column_Name (Original) | Translated_Column_Name | Description                                                                 |
|-------------------------|-------------------------|-----------------------------------------------------------------------------|
| Hoja                    | Sheet                   | Name of the dataset sheet (e.g., `Siniestros`). `object`, 3 distinct values.|
| Atributo                | Attribute               | Column name in the dataset (e.g., `Codigo_Accidente`). `object`, 59 distinct values. |
| Descripción             | Description             | Explanation of the attribute (e.g., "Clave primaria del ppt"). `object`, 53 distinct values. |

---  
*Notes:*  
- "Clave primaria del ppt" translates to "Primary key of the ppt" – "ppt" may refer to a participant or entity (context-specific).  
- Sheets likely categorize data (e.g., accidents, vehicles, victims) based on the `Hoja` distinct values.  