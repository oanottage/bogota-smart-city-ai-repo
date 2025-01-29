# Road Actor Vial Data Dictionary – Translated Documentation  

## Description  
This dataset contains detailed records of individuals involved in traffic accidents, including their roles, demographics, and vehicle information. It spans 422,416 entries with 100% completion for core fields like accident codes, dates, and conditions. The dataset is useful for analyzing accident patterns, victim demographics, and vehicle involvement.  

**Suggested Use Cases**:  
- Accident participant analysis (e.g., driver vs. pedestrian roles).  
- Demographic risk assessment (e.g., age, gender correlations).  
- Vehicle involvement studies (e.g., types of vehicles in accidents).  
- Temporal trend analysis (e.g., accident frequency over time).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| CODIGO_ACCIDENTE              | Accident_Code                   | Unique accident identifier. `int64`, 196,004 distinct values.              |
| CODIGO_ACCIDENTADO            | Injured_Code                    | Unique identifier for injured individuals. `int64`, 422,416 distinct values. |
| FECHA                         | Date                            | Accident date (e.g., `01/01/2015`). `object`, 2,192 distinct values.       |
| CONDICION                     | Condition                       | Role of the individual (e.g., `CONDUCTOR` = "Driver"). `object`, 5 distinct values. |
| ESTADO                        | Status                          | Injury status (e.g., `ILESO` = "Uninjured"). `object`, 3 distinct values.  |
| EDAD                          | Age                             | Age of the individual. `object`, 114 distinct values.                      |
| SEXO                          | Gender                          | Gender (e.g., `FEMENINO` = "Female"). `object`, 3 distinct values.         |
| VEHICULO                      | Vehicle                         | Vehicle identifier (e.g., `4401447-1`). `object`, 371,616 distinct values, 94.45% populated. |

---  
*Notes:*  
- `EDAD` is stored as an `object` type, suggesting potential mixed data (e.g., numeric and text values).  
- `VEHICULO` likely combines accident codes and vehicle identifiers (e.g., `4401447-1`).  
- `ESTADO` includes injury severity classifications, useful for safety impact studies.  