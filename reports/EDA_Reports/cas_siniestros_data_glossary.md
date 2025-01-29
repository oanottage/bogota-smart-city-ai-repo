# Accident Incidents Data Dictionary – Translated Documentation  

## Description  
This dataset contains detailed records of traffic accidents in Bogotá, Colombia, including timestamps, severity classifications, collision types, and location information. It spans 196,152 entries with 100% completion for core fields like accident codes, dates, and severity. Some columns (e.g., `OBJETO_FLO`) are sparsely populated, indicating optional or conditional data.  

**Suggested Use Cases**:  
- Accident severity analysis (e.g., trends in injury severity over time).  
- Geographic hotspot identification (e.g., high-accident neighborhoods).  
- Collision type studies (e.g., most common types of accidents).  
- Infrastructure impact analysis (e.g., road design and accident rates).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| CODIGO_ACCIDENTE              | Accident_Code                   | Unique accident identifier. `int64`, 196,152 distinct values.              |
| FECHA                         | Date                            | Accident date (e.g., `0101/2015`). `object`, 2,192 distinct values.        |
| HORA                          | Time                            | Accident time (e.g., `01:05:00`). `object`, 1,439 distinct values.         |
| GRAVEDAD                      | Severity                        | Injury severity level (1–3). `int64`, 3 distinct values.                   |
| CLASE                         | Class                           | Accident type classification (1–7). `int64`, 7 distinct values.            |
| CHOQUE                        | Collision                       | Collision type (1–5). `float64`, 5 distinct values, 85.6% populated.       |
| OBJETO_FLO                    | Object_FLO                      | Object involved in the accident (1–16). `float64`, 13 distinct values, 3.41% populated. |
| DIRECCION                     | Address                         | Street address (e.g., `KR 64A-CL 2C 02`). `object`, 92,518 distinct values. |
| CODIGO_LOCALIDAD              | Locality_Code                   | Neighborhood identifier (1–20). `int64`, 20 distinct values.               |
| DISENO_LUGAR                  | Location_Design                 | Road design type (1–13). `int64`, 13 distinct values.                      |

---  
*Notes:*  
- `FECHA` is stored as an `object` type, suggesting a specific date format (e.g., `DDMM/YYYY`).  
- `OBJETO_FLO` and `CHOQUE` are sparsely populated, indicating optional or conditional data.  
- `GRAVEDAD` and `CLASE` use numeric codes, which likely map to predefined categories (e.g., severity levels, accident types).  
- `DIRECCION` provides detailed street-level information, useful for geospatial analysis.  