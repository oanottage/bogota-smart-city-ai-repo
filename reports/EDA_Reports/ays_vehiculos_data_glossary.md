# Road Vehicles Data Dictionary – Translated Documentation  

## Description  
This dataset details vehicles involved in traffic accidents in Bogotá, Colombia. It includes 24,403 entries with accident codes, vehicle classifications (e.g., `Bus`, `Publico`), operational modalities, and contextual flags (e.g., intoxication, road conditions). Core fields like `Codigo_Accidente` and `Fecha_Acc` are fully populated, while some columns (e.g., `Modalidad`) show sparse data.  

**Suggested Use Cases**:  
- Vehicle-type risk analysis (e.g., buses vs. motorcycles).  
- Public vs. private transportation safety comparisons.  
- Infrastructure impact studies (e.g., potholes, feeder roads).  
- Fleet management insights (e.g., service types, SITP classifications).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| Codigo_Accidente              | Accident_Code                   | Unique accident identifier. `int64`, 14,106 distinct values.               |
| Formulario                    | Form_Number                     | Form ID (e.g., `A001604925`). `object`, 14,106 distinct values.            |
| Fecha_Acc                     | Accident_Date                   | Timestamp of accident. `datetime64[ns]` (assumed), 365 distinct dates.     |
| AA_Acc                        | Accident_Year                   | Year (2023 only). `int64`.                                                 |
| Codigo_Vehiculo               | Vehicle_Code                    | Vehicle identifier (1–8). `int64`, 9 distinct values.                      |
| Clase                         | Vehicle_Class                   | Type (e.g., `Bus`). `object`, 18 distinct values, 99.98% populated.        |
| Servicio                      | Service_Type                    | Usage category (e.g., `Publico`). `object`, 5 distinct values.             |
| Modalidad                     | Operation_Mode                  | Operational context (e.g., "Pasajeros - Individual"). `object`, 7 distinct values, 10.27% populated. |
| Vehículo_Viajaba_Clasificado  | Vehicle_Traveling_Classified    | Travel purpose (e.g., "TRANSPORTE DE PASAJEROS"). `object`, 8 distinct values. |
| Tipo_SITP                     | SITP_Type                       | Public transit classification (e.g., `ZONAL`). `object`, 5 distinct values, 9.11% populated. |
| Con_Biccieta                  | With_Bicycle*                   | Bicycle involvement (`SI`). `object`, 17.68% populated.                    |
| Con_Carga                     | With_Cargo                      | Cargo involvement (`SI`). `object`, 7.04% populated.                       |
| Con_Embriaguez                | With_Intoxication               | Intoxication involvement (`SI`). `object`, 4.27% populated.                |
| Con_Huecos                    | With_Potholes                   | Pothole involvement (`SI`). `object`, 1.04% populated.                     |
| Con_Menores                   | With_Minors                     | Minor involvement (`SI`). `object`, 8.64% populated.                       |
| Con_Moto                      | With_Motorcycle                 | Motorcycle involvement (`SI`). `object`, 63.71% populated.                 |
| Con_Peston                    | With_Pedestrian                 | Pedestrian involvement (`SI`). `object`, 12.59% populated.                 |
| Con_Persona_Mayor             | With_Older_Person               | Elderly involvement (`SI`). `object`, 18.26% populated.                    |
| Con_Rutas                     | With_Routes                     | Route involvement (`SI`). `object`, 0.03% populated.                       |
| Con_Tpi                       | With_TPI                        | TPI involvement (`SI`). `object`, 14.63% populated.                        |
| Con_Tpp                       | With_TPP                        | TPP involvement (`SI`). `object`, 16.76% populated.                        |
| Con_Velocidad                 | With_Speed                      | Speed-related (`SI`). `object`, 0.57% populated.                           |
| Con_Stip                      | With_SITP                       | SITP involvement (`SI`). `object`, 13.81% populated.                       |
| Con_Troncal                   | With_Trunk                      | Trunk road involvement (`SI`). `object`, 1.44% populated.                  |
| Con_Ailmentador               | With_Feeder*                    | Feeder road involvement (`SI`). `object`, 1.23% populated.                 |
| Con_Zonal                     | With_Zonal                      | Zonal road involvement (`SI`). `object`, 11.17% populated.                 |
| Con_Provisional               | With_Provisional                | Provisional indicator. `float64`, 0.0% populated.                          |
| Con_Articulado                | With_Articulated                | Articulated vehicle involvement (`SI`). `object`, 0.5% populated.          |
| Con_Biarticulado              | With_Biarticulated              | Biarticulated vehicle involvement (`SI`). `object`, 0.67% populated.       |
| Con_Padron_Dual               | With_Dual_Registry              | Dual registry involvement (`SI`). `object`, 0.27% populated.               |

---  
*Notes:*  
- `Con_Biccieta` likely contains a typo (intended: *Bicicleta* = "Bicycle").  
- `Con_Ailmentador` likely misspelled (intended: *Alimentador* = "Feeder").  
- `Fecha_Acc` Python type "datetime6[iris]" is assumed to be `datetime64[ns]`.  
- `SI` = "Yes" for all `Con_` flag columns.  
- SITP refers to Bogotá’s Integrated Public Transport System.  