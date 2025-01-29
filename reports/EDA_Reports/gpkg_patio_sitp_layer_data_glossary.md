# Exploratory Data Analysis of Bogotá SITP Patios – Translated Documentation

## Description
This file provides an exploratory data analysis (EDA) of SITP (Bogotá’s Integrated Public Transport System) patios. A "patio" typically refers to a bus yard or facility for storage, maintenance, and operation of the public transport fleet. The dataset includes attributes such as the patio’s ID, name, address, operational status, and geographic coordinates, offering insights into how these sites are distributed and managed within the city.

**Suggested Use Cases**:
- Public transit planning and optimization (e.g., determining locations for new or expanded patios).
- Operational analysis (e.g., evaluating fuel types, operational status).
- Urban and transportation studies (e.g., integration with city zoning data).
- Location-based services (e.g., mapping and geospatial analysis).

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name  | Description                                                                                                                                          |
|------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ID_Patio**           | Patio ID               | Unique identifier for each bus yard (object). 66 distinct values. Sample value: "PZ025".                                                             |
| **Nombre**             | Name                    | Name of the patio or facility (object). 65 distinct values. Sample value: "LAS ACACIAS".                                                             |
| **Direccion**          | Address                 | Physical address of the facility (object). 61 distinct values. Sample value: "KR 19D 64B 3".                                                         |
| **Componente**         | Component               | SITP operational component (object). 2 distinct values (e.g., “ZONAL”).                                                                              |
| **Zona_SITP**          | SITP Zone               | Designated geographical or administrative zone (object). 31 distinct values. Sample value: "SAN CRISTOB".                                            |
| **Operador**           | Operator                | Company or consortium responsible for operating the patio (object). 25 distinct values. Sample value: "CONSORCIO B".                                  |
| **Abastecimi**         | Fuel Supply Type        | Type of fuel used for vehicles at the facility (object). 7 distinct values. Sample value: "DIESEL".                                                  |
| **Estadolmp**          | Operational Status      | Current operating status of the patio (object). 1 distinct value: "OPERATIVO".                                                                       |
| **FaselImple**         | Implementation Phase    | Phase of the SITP rollout at which the patio was introduced (object). 5 distinct values. Sample value: "FASE III".                                    |
| **Formalizac**         | Formalization           | Indicates level or process of formalization/authorization (object). 3 distinct values. Sample value: "AVAL".                                          |
| **Indicador**          | Indicator               | Numeric indicator with a range from 0 to 2.97 (float64). 51 distinct values. Sample value: 1.13.                                                     |
| **Latitud**            | Latitude                | Geographic coordinate (float64). Range from 4.47 to 4.80. Sample value: 4.56.                                                                        |
| **Longitud**           | Longitude               | Geographic coordinate (float64). Range from -74.22 to -74.05. Sample value: -74.15.                                                                  |
| **Area_aprox**         | Approximate Area        | Numeric measure of the patio’s approximate area in unspecified units (float64). Range from 0.30 to 7.20. Sample value: 0.90.                          |
| **Area_Ha**            | Area (Hectares)         | Numeric measure of the patio’s area in hectares (float64). Range from 1,859.92 to 66,134.79. Sample value: 8,336.56.                                  |
| **SHAPE_Leng**         | Shape Length            | Floating-point value representing the perimeter or length of the patio shape (float64). Range: 0.00–0.02. Sample value: 0.01.                        |
| **SHAPE_Area**         | Shape Area             | Floating-point value representing the area of the geometry (float64). Range: 0.00–0.00.                                                               |
| **geometry**           | Geometry Binary Data    | Binary geometric representation of the patio boundaries (object). 66 distinct values.                                                                 |

---
