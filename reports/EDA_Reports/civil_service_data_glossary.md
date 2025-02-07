# **Civil Service – Data Dictionary**  

## **Description**  
This dataset contains information on legislative proposals in the civil service sector, including proposal identifiers, approval dates, political affiliations, commission origins, and thematic details. It consists of **5,795 entries**, each capturing various aspects of policy discussions and decision-making processes. The dataset is well-structured and ideal for analyzing legislative trends and political dynamics.  

### **Suggested Use Cases:**  
- **Legislative Trends Analysis**: Tracking patterns in proposals and approvals over time.  
- **Political Party Influence**: Analyzing how different political parties propose and support policies.  
- **Thematic Research**: Studying prevalent topics in legislative discussions.  
- **Historical Policy Review**: Reviewing policy trends across different years.  

---

## **Data Glossary**  

| **Column_Name (Original)**   | **Translated_Column_Name**  | **Description** |
|-----------------------------|----------------------------|----------------|
| Id Proposición            | Proposal ID               | Unique identifier for each legislative proposal. Stored as `object`, with **5,795** distinct values. |
| Aprobación                | Approval Date            | Date when the proposal was approved. Stored as `object`, with **1,223** distinct values. |
| Bancada                   | Political Party          | The political party proposing the initiative. Stored as `object`, with **31** distinct values. |
| Comisión origen           | Origin Commission        | The commission responsible for the proposal's origin. Stored as `object`, with **5** distinct values. |
| Título                    | Title                    | Title of the legislative proposal. Stored as `object`, with **5,382** distinct values. |
| Tema                      | Theme                    | General theme of the proposal (e.g., Environmental Affairs). Stored as `object`, with **20** distinct values. |
| Subtema                   | Subtheme                 | More specific category under the general theme. Stored as `object`, with **247** distinct values. |
| Proposición               | Proposal Number          | Numeric identifier for the proposal. Stored as `int64`, ranging from **1** to **999**. |
| Año                       | Year                     | Year when the proposal was introduced. Stored as `int64`, ranging from **2016** to **2024**. |