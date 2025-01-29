# Metro Stations Data Dictionary – Translated Documentation  

## Description  
This dataset contains detailed information about metro stations in Bogotá, Colombia, including their names, coordinates, accessibility features, and spatial data. It includes 149 entries with 100% completion for all fields. The dataset is useful for analyzing metro station locations, accessibility, and integration with other transportation systems (e.g., bike stations).  

**Suggested Use Cases**:  
- Metro station location analysis (e.g., coverage, accessibility).  
- Integration with bike and road networks for multimodal transportation studies.  
- Urban planning and public transportation development.  
- Accessibility analysis (e.g., number of access points, bike parking capacity).  

---

## Data Glossary  

| Column_Name (Original)       | Translated_Column_Name          | Description                                                                 |
|-------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| object_id                     | Object_ID                       | Unique identifier for each station. `int32`, range: 1–149.                 |
| numero_est                    | Station_Number                  | Station number (e.g., `07103`). `object`, 149 distinct values.             |
| nombre_est                    | Station_Name                    | Name of the station (e.g., `AV.Chile`). `object`, 149 distinct values.     |
| coor_x                        | Coordinate_X                    | X-coordinate of the station. `float64`, range: 985,801.67–1,003,765.02.    |
| coor_y                        | Coordinate_Y                    | Y-coordinate of the station. `float64`, range: 992,869.21–1,019,088.46.    |
| ubicacion                     | Location                        | Street address of the station (e.g., `Kr 30 Cl72`). `object`, 148 distinct values. |
| troncal                       | Trunk_Line                      | Trunk line associated with the station (e.g., `NQS`). `object`, 12 distinct values. |
| num_vagon                     | Number_of_Cars                  | Number of cars at the station (0–6). `int32`, 7 distinct values.           |
| num_accesso                   | Number_of_Access_Points         | Number of access points (0–2). `int32`, 3 distinct values.                 |
| bici_est                      | Bike_Station                    | Indicates if the station has bike parking (`0` = "No"). `object`, binary.  |
| capac_bici                    | Bike_Capacity                   | Bike parking capacity (0–785). `int32`, 14 distinct values.                |
| tipo_est                      | Station_Type                    | Type of station (1–4). `int32`, 4 distinct values.                         |
| bicip_est                     | Bike_Parking                    | Indicates if the station has bike parking (`0` = "No"). `int32`, binary.   |
| latitud                       | Latitude                        | Latitude of the station. `float64`, range: 4.53–4.77.                      |
| longitud                      | Longitude                       | Longitude of the station. `float64`, range: -74.21 to -74.04.              |
| cod_nodest                    | Station_Node_Code               | Unique node identifier for the station. `int64`, range: 2,000–14,005.      |
| geometry                      | Geometry                        | Spatial geometry of the station (e.g., coordinates). `object`.             |

---  
*Notes:*  
- `coor_x` and `coor_y` provide Cartesian coordinates, while `latitud` and `longitud` provide geographic coordinates.  
- `bici_est` and `bicip_est` indicate bike parking availability, useful for multimodal transportation studies.  
- `troncal` identifies the trunk line associated with the station, essential for metro network analysis.  
- The `geometry` column contains spatial data, likely in a format like WKT or GeoJSON, for mapping purposes.  