# Geo Road Network Data Dictionary – Translated Documentation  

## Description  
This dataset contains detailed information about the road network in Bogotá, Colombia, including functional classifications, surface types, geometric attributes, and spatial data. It includes 101,720 entries with 100% completion for all fields. The dataset is useful for analyzing road infrastructure, such as road widths, lengths, and spatial coverage.  

**Suggested Use Cases**:  
- Road network infrastructure analysis (e.g., functional classification, surface types).  
- Spatial analysis of road segments (e.g., length, width).  
- Urban planning and road infrastructure development.  
- Integration with other transportation datasets for multimodal studies.  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| CalFunction                   | Functional_Classification       | Functional classification of the road (1–2). `int64`, 2 distinct values.   |
| CalTSuperf                    | Surface_Type                    | Surface type classification (0–13). `int64`, 10 distinct values.           |
| CalCodigo                     | Road_Code                       | Unique identifier for road segments. `int64`, 101,715 distinct values.     |
| CalCIV                        | Road_CIV                        | Road CIV identifier (0–100,119,147). `int64`, 89,436 distinct values.      |
| CalAncho                      | Road_Width                      | Width of the road segment (0.66–618.99 meters). `float64`, 1,862 distinct values. |
| Call_ongitu                   | Road_Length                     | Length of the road segment (1.19–2,564.73 meters). `float64`, 17,757 distinct values. |
| SHAPE_Leng                    | Shape_Length                    | Length of the road segment in spatial terms. `float64`, range: 0.00–0.06.  |
| SHAPE_Area                    | Shape_Area                      | Area of the road segment in spatial terms. `float64`, range: 0.00–0.00.    |
| geometry                      | Geometry                        | Spatial geometry of the road segment (e.g., coordinates). `object`.        |

---  
*Notes:*  
- `CalFunction` likely represents the functional classification of roads (e.g., primary, secondary).  
- `CalTSuperf` indicates the surface type of the road (e.g., asphalt, gravel).  
- `CalCodigo` and `CalCIV` are unique identifiers for road segments, useful for mapping and analysis.  
- `CalAncho` and `Call_ongitu` provide physical measurements of road segments, essential for infrastructure analysis.  
- The `geometry` column contains spatial data, likely in a format like WKT or GeoJSON, for mapping purposes.  