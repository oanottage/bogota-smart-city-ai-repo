# Exploratory Data Analysis of Bogotá SITP Bus Stop/Station Records – Translated Documentation

## Description
This file provides an exploratory data analysis (EDA) of SITP (Bogotá’s Integrated Public Transport System) bus stops or stations. Each record includes an internal numeric ID, SITP zone codes, textual descriptions (e.g., name, address), and geospatial coordinates (latitude, longitude). The dataset can be helpful for route optimization, passenger information systems, and general geospatial analysis of public transportation infrastructure.

**Suggested Use Cases**:
- Public transit network analysis (e.g., identifying coverage gaps).
- Map-based applications (e.g., real-time bus route tracking).
- Data governance or quality assurance for bus stop inventories.
- Integrating bus stop data into broader mobility or city planning initiatives.

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name  | Description                                                                                                                                     |
|------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **objectid**           | Object ID              | Integer identifier for each bus stop/record (int32). Range from 1 to 7,623.                                                                     |
| **cenefa**             | Cenefa                 | Alphanumeric code possibly representing bus stop signage or design (object). 7,623 distinct values.                                            |
| **zona_sitp**          | SITP Zone              | Code indicating the SITP operational zone for the stop (object). 15 distinct values.                                                             |
| **nombre**             | Name                   | Name or label for the bus stop (object). 3,554 distinct values.                                                                                 |
| **via**                | Road                   | Road or main street reference (object). 1,789 distinct values.                                                                                  |
| **direccion_**         | Address                | Text describing the location/address (object). 6,158 distinct values.                                                                           |
| **localidad**          | Locality               | Administrative division or neighborhood in Bogotá (object). 19 distinct values.                                                                 |
| **longitud**           | Longitude              | Geographic coordinate in decimal degrees (float64). Range: -74.22 to -74.02. Sample value: -74.06.                                              |
| **latitud**            | Latitude               | Geographic coordinate in decimal degrees (float64). Range: 4.47 to 4.82. Sample value: 4.69.                                                    |
| **consecutiv**         | Consecutive            | Alphanumeric sequence or reference code (object). 839 distinct values.                                                                          |
| **tipo_m_s**           | M/S Type               | Categorical field with 2 distinct values (e.g., "M", "S") (object).                                                                             |
| **consola**            | Console                | Text or code displayed on the operator console or signage (object). 7,622 distinct values.                                                      |
| **panel**              | Panel                  | Text or code displayed on the external or internal panel (object). 6,156 distinct values.                                                       |
| **audio**              | Audio                  | Audio announcement reference (object). 5,990 distinct values.                                                                                   |
| **zonas_nuev**         | New Zones              | Updated or alternative zone classification (object). 12 distinct values.                                                                        |
| **geometry**           | Geometry Binary Data   | Binary representation of the bus stop’s spatial geometry (object). 7,619 distinct values.                                                       |

---
