# **Security Llamadas – Data Dictionary**  

## **Description**  
This dataset contains information related to security-related calls, including unique identifiers, timestamps, incident types, location details, and incident counts. The dataset comprises **950,431 entries**, providing structured data for analyzing security incidents over time.  

### **Suggested Use Cases:**  
- **Incident Trend Analysis**: Identifying patterns in security incidents across time and location.  
- **Geospatial Analysis**: Mapping the distribution of security incidents by locality and UPZ.  
- **Resource Allocation**: Assisting law enforcement in allocating resources based on incident frequency.  
- **Predictive Modeling**: Forecasting security trends using historical data.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| ID                          | Incident ID               | Unique identifier for each security call. Stored as `object`, with **947,556** distinct values. |
| ANIO                        | Year                      | Year of the recorded incident. Stored as `int64`, ranging from **2015** to **2024**. |
| MES                         | Month                     | Month of the recorded incident. Stored as `int64`, ranging from **1** to **12**. |
| TIPO_INCIDENTE              | Incident Type             | Classification code for the type of incident. Stored as `object`, with **107** distinct values. |
| TIPO_DETALLE                | Incident Detail           | Detailed classification of the incident (e.g., "RESTOS HUMANOS"). Stored as `object`, with **138** distinct values. |
| COD_LOCALIDAD               | Locality Code             | Numeric code representing the locality. Stored as `object`, with **22** distinct values. |
| LOCALIDAD                   | Locality                  | Name of the locality (e.g., "SIN LOCALIZACION"). Stored as `object`, with **22** distinct values. |
| COD_UPZ                     | UPZ Code                  | Unique identifier for UPZ (Urban Planning Zones). Stored as `object`, with **125** distinct values. |
| UPZ                         | UPZ Name                  | Name of the UPZ (e.g., "SIN LOCALIZACION"). Stored as `object`, with **125** distinct values. |
| CANT_INCIDENTES             | Incident Count            | Number of incidents recorded in a given case. Stored as `int64`, ranging from **1** to **10,285**. |