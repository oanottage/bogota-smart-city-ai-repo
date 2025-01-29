# Exploratory Data Analysis of Bogota Localities – Translated Documentation

## Description
This file provides an overview of an exploratory data analysis (EDA) related to localities in Bogotá, Colombia. It contains core attributes such as locality names, administrative details, area measurements, and geometric information useful for understanding the spatial layout of each locality. The EDA includes statistics like minimum and maximum area, as well as data types and distinct counts, to give a clear snapshot of data quality and range.

**Suggested Use Cases**:
- Data governance or quality assurance workflows (e.g., verifying locality area ranges).
- Geospatial analysis and visualization (e.g., mapping localities, measuring shapes).
- Public policy or urban planning applications (e.g., analyzing administrative codes).
- Integration into broader data pipelines (e.g., merging with population or transportation data).

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name  | Description                                                                                                                     |
|------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **LocNombre**          | Locality Name           | Name of the locality (sample value: "ANTONIO NARI"). 20 distinct values, object type.                                           |
| **LocAdmini**          | Administrative Act      | Official agreement or act that established or recognized the locality (sample value: "Acuerdo 117 d"). 6 distinct values, object type.   |
| **LocArea**            | Locality Area           | Area of the locality (numeric). Ranges from approx. 2,060,242.92 to 780,968,757.7. float64 type.                                 |
| **LocCodigo**          | Locality Code           | Numeric code identifying the locality (sample value: 15.00). 20 distinct values, object type.                                    |
| **SHAPE_Leng**         | Shape Length            | Length of the locality’s boundary (numeric). Ranges from 0.07 to 1.91. float64 type.                                             |
| **SHAPE_Area**         | Shape Area             | Area of the locality’s geometric boundary (numeric). Ranges from 0.00 to 0.06. float64 type.                                     |
| **geometry**           | Geometry Binary Data    | Binary representation of the locality’s geometric shape (sample value: `b'\x01\x03\x00'`). 20 distinct values, object type.      |

---
