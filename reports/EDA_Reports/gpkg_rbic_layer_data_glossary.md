# Exploratory Data Analysis of Bogotá Road Infrastructure Segments – Translated Documentation

## Description
This file contains an exploratory data analysis (EDA) of road infrastructure segments in Bogotá, Colombia. Each record includes unique identification codes, classifications, directionality, surface types, and localized attributes. The dataset can be instrumental for transportation planning, roadway maintenance, and GIS-based studies.

**Suggested Use Cases**:
- Roadway and infrastructure management (e.g., tracking road types and conditions).
- Traffic flow analysis (e.g., leveraging the “RBiSentido” to understand road directionality).
- Urban and transportation planning (e.g., identifying patterns in road classification or location).
- GIS mapping and integration with other transportation datasets.

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name   | Description                                                                                                                     |
|------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **RBiCodigo**          | Road Segment Code        | Integer code (int64) identifying each road segment. Range: 34,000,000 – 91,064,010. 14,766 distinct values.                      |
| **RBiClase**           | Road Class               | Integer classification code (int32) for the road. Range: 1 – 13. 14,766 records.                                                |
| **RBiSentido**         | Road Direction           | Alphanumeric code for directionality (object). 2 distinct values (e.g., "DS").                                                  |
| **RBiTSuperf**         | Surface Type             | Integer code (int32) indicating road surface (e.g., pavement). Range: 1 – 4.                                                    |
| **RBiCIVial**          | Road CIV Code            | Long integer code (int64) possibly referencing civic or official road registry. Range: 0 – 92,089,180.                          |
| **RBiLocaliz**         | Road Localization        | Integer code (int32) indicating the road’s localized zone or area. Range: 1 – 9.                                                |
| **SHAPE_Leng**         | Shape Length             | Floating-point length of the road geometry (float64). Range: 0.00 – 0.01.                                                       |
| **geometry**           | Geometry Binary Data     | Binary representation of the segment's spatial geometry (object). 14,764 distinct values.                                       |

---
