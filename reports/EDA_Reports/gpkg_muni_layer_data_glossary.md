# Exploratory Data Analysis of Bogotá Municipality – Translated Documentation

## Description
This file provides a concise exploratory data analysis (EDA) for a dataset describing the municipality of Bogotá, D.C. It contains information such as the municipality name, area, administrative acts, and geometric boundaries. Although the dataset has only a single row in this snapshot, it can still offer key insights into municipal-level data and structure.

**Suggested Use Cases**:
- Data governance or quality assurance for municipal data.
- Geospatial analysis and visualization (e.g., mapping the municipality).
- Public policy, urban planning, or city management applications.
- Integration with broader datasets (e.g., combining with demographic or regional statistics).

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name | Description                                                                                          |
|------------------------|------------------------|------------------------------------------------------------------------------------------------------|
| **MunNombre**          | Municipality Name      | Name of the municipality (sample value: “BOGOTÁ D.C.”). Only 1 distinct value, object type.          |
| **MunArea**            | Municipality Area      | Numeric value representing the area of the municipality (sample value: 1,636.37). float64 type.      |
| **MunCodigo**          | Municipality Code      | Official numeric code for the municipality (sample value: 11,001.00). 1 distinct value, object type. |
| **MunAAdmini**         | Administrative Act     | Official decree or act related to the municipality (sample value: “Dec 3640 del”). object type.      |
| **SHAPE_Leng**         | Shape Length           | Numeric representation of the municipality’s boundary length (sample value: 3.75). float64 type.     |
| **SHAPE_Area**         | Shape Area            | Numeric area metric of the municipality’s shape (sample value: 0.13). float64 type.                  |
| **geometry**           | Geometry Binary Data   | Binary encoding of the municipality’s geometric shape (sample value: `b'\x01\x03\x00'`). object type.|

---
