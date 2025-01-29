# Exploratory Data Analysis of Bogotá Georeferenced Points – Translated Documentation

## Description
This file contains an exploratory data analysis (EDA) of georeferenced points in Bogotá, Colombia. Each record includes spatial coordinates (latitude, longitude), projected coordinates (northing and easting), altitude data, and additional descriptive information such as a unique code and name. The dataset appears to originate from a geological or cartographic source (e.g., "Servicio Geológico"), and it could be valuable for mapping, environmental studies, or other location-based analyses.

**Suggested Use Cases**:
- Geographic Information Systems (GIS) mapping and analysis.
- Environmental or geological studies (e.g., evaluating elevations, materials).
- Urban planning or infrastructure projects (e.g., referencing specific points of interest).
- Data governance or quality assurance of location-based datasets.

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name  | Description                                                                                                                                                          |
|------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PGeLatitud**         | Latitude                | Latitude in decimal degrees (float64). Range: 4.29 – 4.98. Sample value: 4.62.                                                                                       |
| **PGeLongitu**         | Longitude               | Longitude in decimal degrees (float64). Range: -74.26 – -73.72. Sample value: -74.14.                                                                                |
| **PGeAElipso**         | Ellipsoidal Height      | Approximate ellipsoidal elevation (float64). Range: 2,562.40 – 3,754.68. Sample value: 2,579.37.                                                                     |
| **PGeCNorte**          | Northing                | Projected northing coordinate (float64). Range: 66,107.74 – 142,151.41. Sample value: 102,733.58.                                                                    |
| **PGeCEste**           | Easting                 | Projected easting coordinate (float64). Range: 79,906.34 – 139,429.57. Sample value: 92,994.71.                                                                      |
| **PGeFActual**         | Update/Current Date     | Date field representing the most recent update or current date (datetime64[m]). 60 distinct values. Sample value: 44,926 (internal numeric date encoding).           |
| **PGeCodigo**          | Code                    | Unique code or identifier for each point (object). 363 distinct values. Sample value: "BAOC".                                                                        |
| **PGeNombre**          | Name                    | Name or designation of the point (object). 46 distinct values. Sample value: "Parque Am…".                                                                           |
| **PGeTMateri**         | Material Type           | Numeric code (int64) indicating the material classification (e.g., 1, 2, 3). Range: 1 – 3.                                                                           |
| **PGeFuente**          | Data Source             | Source of the georeferenced data (object). 19 distinct values. Sample value: "Servicio Geologico…".                                                                 |
| **geometry**           | Geometry Binary Data    | Binary representation of the georeferenced geometry (object). 363 distinct values.                                                                                   |

---
