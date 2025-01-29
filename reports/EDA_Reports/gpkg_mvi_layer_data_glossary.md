# Exploratory Data Analysis of Bogotá Road Network – Translated Documentation

## Description
This file provides an exploratory data analysis (EDA) of a road network dataset in Bogotá, Colombia. It contains attributes for road identification, classifications, alternative names, and various geometry-related fields (e.g., shape length). The dataset appears extensive (over 139,000 records), offering rich detail for mapping, transportation analytics, and road infrastructure management.

**Suggested Use Cases**:
- Transportation and mobility studies (e.g., identifying high-traffic roads).
- Geospatial analysis and visualization (e.g., mapping roadway features).
- Public policy or urban planning (e.g., road maintenance, traffic flow optimization).
- Integration into broader mobility or accident analysis pipelines.

---

## Data Glossary

| Column_Name (Original) | Translated_Column_Name   | Description                                                                                                                                              |
|------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MVICCalzad**         | Road Carriageway Count   | Numeric identifier (int64) showing the count or code of the carriageway. Sample value: 520,097. Range: 0 – 91,030,676.                                   |
| **MVICCat**            | Road Category            | Text-based category or classification for the road (object type). Sample value: "17,000,249". Over 100k distinct values.                                 |
| **MVICla**             | Road Classification      | Numeric classification code (int64). Sample value: 3. Range: 1 – 7.                                                                                     |
| **MVITipo**            | Road Type                | Road type or label (object). Sample value: "CL" (could indicate "Calle"). 6 distinct values.                                                             |
| **MVINombre**          | Road Name                | Primary name or designated label (object). Sample value: "SIN_NMG". 130 distinct values.                                                                 |
| **MVIAltern**          | Alternate Name           | Alternate or secondary name of the road (object). Sample value: "AUTOPISTA N". 6 distinct values.                                                        |
| **MVINPrinci**         | Principal Road Segment   | Principal or main segment identifier (object). Sample value: "006ABISA00". Over 4,000 distinct values.                                                  |
| **MVINGenera**         | General Road Segment     | General segment identifier (object). Sample value: "002A000000". Over 2,000 distinct values.                                                             |
| **MVINAntigu**         | Old Road Name            | Historic or previous name for the road (object). Sample value: "CL 4A". Over 6,000 distinct values.                                                      |
| **MVIEtiquet**         | Road Label               | Standard label or reference for the road (object). Sample value: "CL 6ABISA". Over 6,000 distinct values.                                               |
| **MVISVia**            | Road Section Type        | Road section or segment type (object). Sample value: "B". 6 distinct values.                                                                             |
| **MVICIV**             | CIV Code                 | Numeric code (int64) with a wide range (0 – 91,029,075). Sample value: "3,001,043". 116,323 distinct values.                                             |
| **SHAPE_Leng**         | Shape Length             | Floating-point length of the road’s geometry (float64). Sample range: 0.00 – 0.04.                                                                       |
| **MVICodigo**          | Road Code                | Integer code (int64) identifying the road segment. Range: 1 – 144,245.                                                                                  |
| **MVINumC**            | Count/Number             | Integer field (int32) representing a count or number related to the road. Range: 1 – 6.                                                                  |
| **MVIVelReg**          | Regulated Speed          | Road speed designation (object). Sample value: "30". Only 2 distinct values found in this sample.                                                       |
| **geometry**           | Geometry Binary Data     | Binary geometry representation of the road segment (object). 139,107 distinct values.                                                                    |

---
