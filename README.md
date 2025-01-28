bogota-smart-city-ai
==============================

**Project Overview: Building a Smart City Transportation Solution**

**Goal:**
------------
Develop an AI-driven platform that integrates multiple Bogotá transport datasets—including TransMilenio bicycle stations, trunk system departures, road accident data, and more—to predict congestion hot spots and recommend optimal mobility solutions (e.g., bike routes, better scheduling for public transit, etc.).


**Datasets We’ll Use:**
------------

bike-stations: TransMilenio bicycle stations (average entries at bike stations) - https://datosabiertos.bogota.gov.co/dataset/cicloparqueaderos-de-transmilenio

reference-map: Reference Map for Bogota DC (for geospatial data analysis) - https://datosabiertos.bogota.gov.co/dataset/mapa-de-referencia

truck-departures: Consolidated Trunk System Departures by Time Zone (user departures by date/time slot) - https://datosabiertos.bogota.gov.co/dataset/consolidado-de-salidas-sistema-troncal-por-franja-horaria

accident-yearbook: Road Accident Yearbook (historical accident data) - https://datosabiertos.bogota.gov.co/dataset/anuario-siniestralidad

consolidated-accidents: Consolidated Road Accidents in Bogotá DC (historical accident data) - https://datosabiertos.bogota.gov.co/dataset/siniestros-viales-consolidados-bogota-d-c

cycle-route: Cycle Route (bike lane infrastructure in GeoJSON, SHP, etc.) - https://datosabiertos.bogota.gov.co/dataset/cicloruta-bogota-d-c

bike-network: Bicycle Users Network (bike lane infrastructure in GeoJSON, SHP, etc.) - https://datosabiertos.bogota.gov.co/dataset/red-biciusuarios-bogota-d-c

(UNAVAILABLE) current-speed: Current Speed on Road (for real-time or historical traffic insights) - https://datosabiertos.bogota.gov.co/dataset/velocidad-actual-en-via-bogota-d-c

(UNAVAILABLE) incidents-on-via: Incidents on Via (for real-time or historical traffic insights) - https://datosabiertos.bogota.gov.co/dataset/incidentes-en-via-bogota-d-c 

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
