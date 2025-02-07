# **Geo DAILOC – Data Dictionary**  

## **Description**  
This dataset contains geographical and administrative location data related to DAILOC, including identifiers, ranking values, statistical measurements, and spatial attributes. The dataset comprises **21 entries**, offering a structured representation of location-based data for analysis.  

### **Suggested Use Cases:**  
- **Geospatial Analysis**: Mapping and analyzing geographical distributions linked to DAILOC.  
- **Statistical Research**: Studying various numerical attributes associated with locations.  
- **Urban and Regional Planning**: Evaluating the distribution and density of locations based on different metrics.  
- **Data Validation**: Ensuring consistency in spatial and statistical records.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| CMIULOCA                   | Location ID               | Unique identifier for each location. Stored as `object`, with **21** distinct values. |
| CMNOMLOCA                  | Location Name             | Name of the location (e.g., "Fontibón"). Stored as `object`, with **21** distinct values. |
| CMMES                      | Month Range               | Time period covered (e.g., "Ene-Dic"). Stored as `object`, with **1** distinct value. |
| Various Statistical Fields  | Statistical Measures      | Numerical variables (e.g., CMLP18CC, CMHA22CC) with values stored as `float64`, ranging across different scales. |
| CMVITOTAL                  | Total Count               | Total number associated with each record. Stored as `float64`, with varying values up to **32,625**. |
| SHAPE.AREA                 | Shape Area                | Geographic area measurement. Stored as `float64`, ranging from **0.00271** to **0.063545**. |
| SHAPE.LEN                  | Shape Length              | Geographic perimeter measurement. Stored as `float64`, ranging from **0.321915** to **1.914949**. |
| geometry                   | Geometry                  | Geospatial data stored in binary format. Stored as `object`. |