# Geo Bike Network Data Dictionary – Translated Documentation  

## Description  
This dataset contains information about the bike network in Bogotá, Colombia, including spatial and geometric attributes. It includes 5,928 entries with 100% completion for all fields. The dataset is useful for analyzing bike infrastructure, such as bike paths, their lengths, and spatial coverage.  

**Suggested Use Cases**:  
- Bike network infrastructure analysis (e.g., coverage, connectivity).  
- Spatial analysis of bike paths (e.g., length, area).  
- Integration with other transportation datasets for multimodal studies.  
- Urban planning and bike infrastructure development.  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| ClcTSuperf                    | Surface_Type                    | Surface type classification (1–5). `int32`, 5 distinct values.             |
| CicCodigo                     | Bike_Path_Code                  | Unique identifier for bike paths. `int32`, 5,928 distinct values.          |
| CicCV                         | Bike_Path_CV                    | Bike path CV identifier (1–100,119,141). `int32`, 4,598 distinct values.   |
| SHAPE_Leng                    | Shape_Length                    | Length of the bike path segment. `float64`, range: 0.00–0.02.              |
| SHAPE_Area                    | Shape_Area                      | Area of the bike path segment. `float64`, range: 0.00–0.00.                |
| geometry                      | Geometry                        | Spatial geometry of the bike path (e.g., coordinates). `object`.           |

---  
*Notes:*  
- `ClcTSuperf` likely represents surface types (e.g., asphalt, gravel).  
- `CicCodigo` and `CicCV` are unique identifiers for bike paths, useful for mapping and analysis.  
- `SHAPE_Leng` and `SHAPE_Area` provide geometric measurements, essential for spatial analysis.  
- The `geometry` column contains spatial data, likely in a format like WKT or GeoJSON, for mapping purposes.  