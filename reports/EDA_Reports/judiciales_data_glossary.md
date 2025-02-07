# **Judiciales – Data Dictionary**  

## **Description**  
This dataset contains judicial case information, including case identifiers, plaintiffs, legal arguments, evidentiary considerations, and rulings. The dataset comprises **456 entries**, providing structured details on legal proceedings for analysis.  

### **Suggested Use Cases:**  
- **Legal Case Analysis**: Identifying patterns in case outcomes and legal arguments.  
- **Risk Assessment**: Evaluating legal risks based on available evidence and precedents.  
- **Jurisprudence Study**: Analyzing related judicial rulings and legal reasoning.  
- **Data Validation**: Ensuring consistency in judicial records.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| PROCESO                    | Case Number               | Unique identifier for each judicial case. Stored as `object`, with **443** distinct values. |
| DEMANDANTE                 | Plaintiff                 | Name and identification of the plaintiff. Stored as `object`, with **397** distinct values. |
| Fortaleza de los planteamientos de la demanda, su presentación y desarrollo | Strength of the Legal Arguments | Qualitative assessment of the strength of the case. Stored as `object`, with **3** distinct values. |
| Debilidad de las excepciones propuestas al contestar la demanda | Weakness of the Exceptions | Qualitative assessment of the weaknesses in exceptions. Stored as `object`, with **3** distinct values. |
| Presencia de Riesgos Procesales | Presence of Legal Risks | Indicator of potential risks in the case. Stored as `object`, with **3** distinct values. |
| Suficiencia del material Probatorio en contra de la Entidad | Sufficiency of Evidence | Assessment of the sufficiency of evidence against the entity. Stored as `object`, with **3** distinct values. |
| Debilidad de las pruebas con las que se pueda considerar la prosperidad de las excepciones propuesta | Weakness of the Evidence | Evaluation of the strength of the evidence supporting exceptions. Stored as `object`, with **3** distinct values. |
| Nivel de Jurisprudencia relacionada o antecedentes similares | Level of Related Jurisprudence | Assessment of similar judicial precedents. Stored as `object`, with **3** distinct values. |
| INST ACTUAL                 | Current Instance           | Judicial instance level (e.g., first or second). Stored as `int64`, ranging from **1** to **3**. |
| FALLO 1a                    | First Ruling              | Decision in the first instance of the case. Stored as `object`, with **3** distinct values. |
| VR. PRETENSION ORIGINAL     | Original Claim Value      | Monetary value of the original claim. Stored as `float64`, ranging from **0** to **9.81E+11**. |