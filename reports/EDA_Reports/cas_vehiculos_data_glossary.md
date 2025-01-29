# Accident Vehicles Data Dictionary – Translated Documentation  

## Description  
This dataset provides detailed information about vehicles involved in traffic accidents in Bogotá, Colombia. It includes 371,605 entries with accident codes, dates, vehicle identifiers, and classifications (e.g., vehicle type, service type). Core fields like `CODIGO_ACCIDENTE` and `FECHA` are fully populated, while some columns (e.g., `MODALIDAD`) show sparse data.  

**Suggested Use Cases**:  
- Vehicle-type risk analysis (e.g., private vs. public vehicles).  
- Accident cause studies (e.g., vehicle service type and accident rates).  
- Integration with other accident datasets using `CODIGO_ACCIDENTE`.  
- Fleet management insights (e.g., service types, vehicle classifications).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| CODIGO_ACCIDENTE              | Accident_Code                   | Unique accident identifier. `int64`, 196,004 distinct values.              |
| FECHA                         | Date                            | Accident date (e.g., `0101/2015`). `object`, 2,192 distinct values.        |
| VEHICULO                      | Vehicle                         | Vehicle identifier (e.g., `4401423-1`). `object`, 371,605 distinct values. |
| CLASE                         | Vehicle_Class                   | Vehicle type classification (1–28). `float64`, 15 distinct values, 99.23% populated. |
| SERVICIO                      | Service_Type                    | Vehicle service type (1–4). `float64`, 4 distinct values, 95.78% populated. |
| MODALIDAD                     | Operation_Mode                  | Operational context (1–12). `float64`, 12 distinct values, 38.67% populated. |
| ENFUGA                        | Fled_Scene                      | Indicates if the vehicle fled the scene (`N` = "No"). `object`, binary.    |

---  
*Notes:*  
- `FECHA` is stored as an `object` type, suggesting a specific date format (e.g., `DDMM/YYYY`).  
- `MODALIDAD` is sparsely populated, indicating optional or conditional data.  
- `CLASE` and `SERVICIO` use numeric codes, which likely map to predefined categories (e.g., vehicle types, service types).  
- `ENFUGA` is a binary flag (`N` = "No"), useful for hit-and-run analysis.  