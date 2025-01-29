# Road Actor Vial Data Dictionary – Translated Documentation  

## Description  
This dataset contains detailed records of traffic incidents and participant information in Bogotá, Colombia. It includes accident codes, timestamps, locations, victim demographics, severity indicators, vehicle conditions, and contextual factors (e.g., road infrastructure, vehicle type). The data spans 33,542 entries with 100% completion for core fields like accident codes and timestamps, while some contextual columns (e.g., `Con_Provisional`) are sparsely populated.  

**Suggested Use Cases**:  
- Accident pattern analysis (e.g., time, location, severity trends).  
- Road safety policy evaluation (e.g., impact of infrastructure like bike lanes).  
- Demographic risk assessment (e.g., age, gender, vehicle type correlations).  
- Predictive modeling for accident severity or post-accident outcomes.  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| Codigo_Accidentado            | Injured_Code                    | Unique identifier for injured individuals. `int64`, range: ~12.8M–12.9M.   |
| Codigo_Accidente              | Accident_Code                   | Unique accident identifier. `int64`, 14,106 distinct values.               |
| Formulario                    | Form_Number                     | Form ID (e.g., `A001576573`). `object`, 14,106 distinct values.            |
| Codigo_Vehiculo               | Vehicle_Code                    | Vehicle identifier (1–9). `float64`, 90.22% populated.                     |
| Ccodigo_Victima               | Victim_Code                     | Victim category (0–44). `int64`, 45 distinct values.                       |
| FechaAcc                      | Accident_Date                   | Timestamp of accident. `datetime64[ns]`, 365 distinct dates.               |
| AmoAcc                        | Accident_Year                   | Year of accident (2023 only). `int64`.                                     |
| mesAcc                        | Accident_Month                  | Month name (e.g., `Septiembre`). `object`, 12 distinct values.             |
| DD_Mes_Acc                    | Day_of_Month                    | Day of month (1–31). `int64`.                                              |
| Dia_Semana_Acc                | Day_of_Week                     | Weekday name (e.g., `sábado`). `object`, 7 distinct values.                |
| hourAcc                       | Accident_Hour                   | Hour of day (0–23). `int64`.                                               |
| minuAcc                       | Accident_Minute                 | Minute of hour (0–59). `int64`.                                            |
| Localidad                     | Locality                        | Neighborhood (e.g., `Ciudad Bolivar`). `object`, 20 distinct values.       |
| Edad                          | Age                             | Victim age (0–112). `float64`, 96.65% populated.                           |
| Sexo                          | Gender                          | `Masculino` (Male) or other. `object`, 2 distinct values.                  |
| Gravedad_Indicador_Traditional| Severity_Indicator_Traditional  | Injury severity (e.g., `ILESO`). `object`, 3 distinct values.              |
| Muerte_Posterior              | Post_Accident_Death             | Death after accident (`N`/`Y`). `object`, binary.                          |
| Fecha_CambioGravedad          | Severity_Change_Date            | Timestamp of severity update. `datetime64[ns]`, 0.64% populated.           |
| Gravedad_Indicador_304        | Severity_Indicator_304          | Alternate severity classification. `object`, 3 distinct values.            |
| Condicion                     | Role                            | Participant role (e.g., `CONDUCTOR`). `object`, 6 distinct values.         |
| Condicion_Espectrica          | Specific_Condition              | Detailed role (e.g., `Cond Taxi`). `object`, 18 distinct values.           |
| Tipo_STIP                     | STIP_Type                       | Road type (e.g., `ZONAL`). `object`, 5 distinct values, 10.8% populated.   |
| Con_Bicicleta                 | With_Bicycle                    | Bicycle involvement (`SI`). `object`, 14.02% populated.                    |
| Con_Carga                     | With_Cargo                      | Cargo involvement (`SI`). `object`, 6.26% populated.                       |
| Con_Emintaguez                | With_Intoxication               | Intoxication involvement (`SI`). `object`, 3.49% populated.                |
| Con_Huecos                    | With_Potholes                   | Pothole involvement (`SI`). `object`, 1.01% populated.                     |
| Con_Menores                   | With_Minors                     | Minor involvement (`SI`). `object`, 12.15% populated.                      |
| Con_Moto                      | With_Motorcycle                 | Motorcycle involvement (`SI`). `object`, 59.72% populated.                 |
| Con_Peston                    | With_Pedestrian                 | Pedestrian involvement (`SI`). `object`, 19.72% populated.                 |
| Con_Persona_Mayer             | With_Older_Person               | Elderly involvement (`SI`). `object`, 21.21% populated.                    |
| Con_Rutas                     | With_Routes                     | Route involvement (`SI`). `object`, 0.09% populated.                       |
| Con_Tpi                       | With_TPI                        | TPI involvement (`SI`). `object`, 13.85% populated.                        |
| Con_Tpp                       | With_TPP                        | TPP involvement (`SI`). `object`, 19.07% populated.                        |
| Con_Velocidad                 | With_Speed                      | Speed-related (`SI`). `object`, 0.6% populated.                            |
| Con_Sltp                      | With_SLTP                       | SLTP involvement (`SI`). `object`, 16.01% populated.                       |
| Con_Troncal                   | With_Trunk                      | Trunk road involvement (`SI`). `object`, 2.15% populated.                  |
| Con_Alimentador               | With_Feeder                     | Feeder road involvement (`SI`). `object`, 1.43% populated.                 |
| Con_Zonal                     | With_Zonal                      | Zonal road involvement (`SI`). `object`, 12.49% populated.                 |
| Con_Provisional               | With_Provisional                | Provisional indicator. `float64`, 0.0% populated.                          |
| Con_Articulado                | With_Articulated                | Articulated vehicle involvement (`SI`). `object`, 0.63% populated.         |
| Con_Biarticulado              | With_Biarticulated              | Biarticulated vehicle involvement (`SI`). `object`, 1.23% populated.       |
| Con_Padron_Dual               | With_Dual_Registry              | Dual registry involvement (`SI`). `object`, 0.32% populated.               |

---  
*Note: Columns prefixed with `Con_` indicate binary flags (`SI` = "Yes") for specific accident conditions.*