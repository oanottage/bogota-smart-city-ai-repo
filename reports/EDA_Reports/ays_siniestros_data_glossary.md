# Accident Incidents Data Dictionary – Translated Documentation  

## Description  
This dataset contains geolocated traffic accident records from Bogotá, Colombia, with 14,106 fully populated entries. It includes spatial coordinates, timestamps, collision details, severity classifications, and contextual flags (e.g., vehicle types, infrastructure factors). Geographic fields like `Longitud`/`Latitud` and address data enable spatial analysis.  

**Suggested Use Cases**:  
- Geospatial accident clustering (e.g., hotspots near specific roads).  
- Severity correlation studies (e.g., speed-related vs. pedestrian-involved accidents).  
- Infrastructure risk assessment (e.g., potholes, zonal roads).  
- Temporal pattern analysis (hourly/weekly/monthly trends).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| Codigo_Accidente              | Accident_Code                   | Unique accident identifier. `int64`, 14,106 distinct values.               |
| Formulario                    | Form_Number                     | Form ID (e.g., `A001571139`). `object`, fully unique.                      |
| Longitud                      | Longitude                       | Geographic coordinate. `float64`, ~-74.25 to -74.01.                       |
| Latitud                       | Latitude                        | Geographic coordinate. `float64`, ~4.04 to 4.82.                           |
| Direccion                     | Address                         | Street description (e.g., "AV CIUDAD DE VILLAVICENCIO"). `object`, 9,979 distinct values. |
| Fecha_Acc                     | Accident_Date                   | Timestamp. `datetime64[ns]`, 365 distinct dates.                           |
| AA_Acc                        | Accident_Year                   | Year (2023 only). `int64`.                                                 |
| MM_Acc                        | Accident_Month                  | Month name (e.g., `Mayo`). `object`, 12 distinct values.                   |
| DD_Mes_Acc                    | Day_of_Month                    | Day (1–31). `int64`.                                                       |
| Dia_Semana_Acc                | Day_of_Week                     | Weekday (e.g., `viernes`). `object`, 7 distinct values.                    |
| Hora_Acc                      | Accident_Hour                   | Hour (0–23). `int64`.                                                      |
| Min_Acc                       | Accident_Minute                 | Minute (0–59). `int64`.                                                    |
| Localidad                     | Locality                        | District (e.g., `BOSA`). `object`, 20 distinct values.                     |
| Clase_Acc                     | Accident_Class                  | Collision type (e.g., `Choque`). `object`, 6 distinct values.              |
| Elemento_Choque               | Collision_Element               | Object involved (e.g., `Vehículo`). `object`, 4 distinct values, 70.51% populated. |
| Tipo_Objeto_Fip               | FIP_Object_Type                 | Specific object type (e.g., parked vehicles). `object`, 11 distinct values, 5.18% populated. |
| Gravedad_Indicador_Tradicional| Severity_Indicator_Traditional  | Injury classification (`Con Heridos` = "With Injuries"). `object`, 3 distinct values. |
| Gravedad_Indicador_304        | Severity_Indicator_304          | Alternate severity classification. `object`, 3 distinct values.            |
| Con_Bicicleta                 | With_Bicycle                    | Bicycle involvement (`Si`). `object`, 15.23% populated.                    |
| Con_Carga                     | With_Cargo                      | Cargo involvement (`Si`). `object`, 6.21% populated.                       |
| Con_Ermbnagerz                | With_Intoxication*              | Intoxication involvement (`Si`). `object`, 3.93% populated.                |
| Con_Huecos                    | With_Potholes                   | Pothole involvement (`Si`). `object`, 1.21% populated.                     |
| Con_Menores                   | With_Minors                     | Minor involvement (`Si`). `object`, 9.39% populated.                       |
| Con_Moto                      | With_Motorcycle                 | Motorcycle involvement (`Si`). `object`, 59.67% populated.                 |
| Con_Peston                    | With_Pedestrian                 | Pedestrian involvement (`Si`). `object`, 20.49% populated.                 |
| Con_Persona_Mayer             | With_Older_Person               | Elderly involvement (`Si`). `object`, 18.64% populated.                    |
| Con_Rutas                     | With_Routes                     | Route involvement (`Si`). `object`, 0.03% populated.                       |
| Con_Tpli                      | With_TPL                        | TPL involvement (`Si`). `object`, 12.59% populated.                        |
| Con_Tpp                       | With_TPP                        | TPP involvement (`Si`). `object`, 18.09% populated.                        |
| Con_Velocidad                 | With_Speed                      | Speed-related (`Si`). `object`, 0.63% populated.                           |
| Con_Slip                      | With_Slip                       | Slip-related (`Si`). `object`, 15.47% populated.                           |
| Con_Troncal                   | With_Trunk                      | Trunk road involvement (`Si`). `object`, 1.87% populated.                  |
| Con_Alimentador               | With_Feeder                     | Feeder road involvement (`Si`). `object`, 1.37% populated.                 |
| Con_Zonal                     | With_Zonal                      | Zonal road involvement (`Si`). `object`, 12.26% populated.                 |
| Con_Provisional               | With_Provisional                | Provisional indicator. `float64`, 0.0% populated.                          |
| Con_Articulado                | With_Articulated                | Articulated vehicle involvement (`Si`). `object`, 0.65% populated.         |
| Con_Biarticulado              | With_Biarticulated              | Biarticulated vehicle involvement (`Si`). `object`, 0.93% populated.       |
| Con_Padron_Dual               | With_Dual_Registry              | Dual registry involvement (`Si`). `object`, 0.3% populated.                |

---  
*Notes:*  
- `Con_Ermbnagerz` is assumed to mean "With Intoxication" (possible typo for *Embriaguez*).  
- Columns prefixed with `Con_` are binary flags (`Si` = "Yes").  
- Latitude/Longitude ranges suggest all accidents occurred within Bogotá's metropolitan area.  