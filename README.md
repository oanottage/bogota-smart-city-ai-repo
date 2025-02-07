bogota-smart-city-ai
==============================

**Project Overview: Building a Smart City Transportation Solution**

**Goal:**
------------
Develop an Big Data and AI-driven platform that integrates multiple Bogotá transport datasets to understand congestion hot spots and recommend optimal mobility solutions (e.g., bike routes, better scheduling for public transit, etc.).


**Datasets We’ll Use:**  
------------  

### **Civil Service**  
- **control-politico.csv**: Political control records and legislative activities. - https://datosabiertos.bogota.gov.co/dataset/control-politico

### **Economy & Finance**  
- **cgn001-metadata.csv**: Metadata for CGN001 financial dataset. - https://datosabiertos.bogota.gov.co/dataset/consolidados-de-bogota-d-c
- **cgn001.csv**: Financial records related to economic analysis. - https://datosabiertos.bogota.gov.co/dataset/consolidados-de-bogota-d-c
- **judiciales-informe-procesos-1er-trimestre-2019.csv**: Judicial report on legal processes for the first quarter of 2019. - https://datosabiertos.bogota.gov.co/dataset/informe-de-procesos-judiciales-1er-trimestre-2019
- **judiciales-metadata-procesos-2019.csv**: Metadata for the judicial processes dataset of 2019. - https://datosabiertos.bogota.gov.co/dataset/informe-de-procesos-judiciales-1er-trimestre-2019

### **Security & Defense**  
- **CRNLoc.geojson**: Geospatial representation of security zones. - https://datosabiertos.bogota.gov.co/dataset/medida-correctiva-bogota-d-c
- **CRNSCAT.geojson**: Geospatial security categorization data. - https://datosabiertos.bogota.gov.co/dataset/medida-correctiva-bogota-d-c
- **CRNUPZ.geojson**: Urban Planning Zones (UPZ) geospatial data for security analysis. - https://datosabiertos.bogota.gov.co/dataset/medida-correctiva-bogota-d-c
- **DAILoc.geojson**: Location-specific security incidents in GeoJSON format. - https://datosabiertos.bogota.gov.co/dataset/delito-de-alto-impacto-bogota-d-c
- **definicioncampos.csv**: Field definitions for security datasets. - https://datosabiertos.bogota.gov.co/dataset/incidentes
- **guiatipificacionincidentes.csv**: Incident classification guide. - https://datosabiertos.bogota.gov.co/dataset/incidentes
- **llamadastramitadas-c4-bogota_numerounicodeseguridadyemergencias-nuse_linea-123-a-31dic2024.csv**: Security and emergency call records processed through the C4 system in Bogotá. - https://datosabiertos.bogota.gov.co/dataset/incidentes

### **Transport**  
- **consolidado-de-salidas-sistema-troncal-por-franja-horaria-noviembre-2024.csv**: Consolidated Trunk System Departures by Time Zone (user departures by date/time slot). - https://datosabiertos.bogota.gov.co/dataset/consolidado-de-salidas-sistema-troncal-por-franja-horaria

---  

This list reflects the datasets available for analysis, covering sectors such as **civil service, economy & finance, security & defense, and transportation**. Each dataset provides valuable insights for policy-making, economic trends, security management, and public transport efficiency.  

**Project Organization**
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
