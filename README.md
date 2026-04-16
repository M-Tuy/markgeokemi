# Uranium risk zonation in Swedish Moraine deposits 
***Environmental Geodata Intelligence Project***
---

This project builds a practical geospatial risk intelligence workflow for identifying elevated uranium zones in Swedish moraine and estimating potential groundwater exposure hotspots.


## Project Goal

Transform SGU regional geochemical uranium data into:

1. Uranium hotspot intelligence maps  
2. Predictive uranium risk zonation maps  
3. Geological driver analysis dashboards  
4. Groundwater exposure screening layers  

This project demonstrates technical capabilities used in:

- environmental consulting
- contaminated land assessment
- groundwater risk screening
- geospatial environmental intelligence
- regulatory environmental agencies


### Geospatial Data Engineering
- geospatial data cleaning
- coordinate handling
- spatial joins
- GIS layer integration

### Environmental Data Analytics
- anomaly detection
- hotspot thresholding
- skewed environmental dataset interpretation

### Predictive Modeling
- random forest classification
- probability mapping
- model validation

### Spatial Risk Intelligence
- hotspot clustering
- risk zonation
- exposure overlay modeling

### Environmental Interpretation
- uranium mobility logic
- groundwater relevance screening
- geology-based risk drivers

---

# Project Architecture

---

# Phase 1 — Geochemical Data Processing Pipeline

### Objective:
Build a clean, structured uranium geodata foundation.

### Tasks:
- import SGU markgeokemi dataset
- extract uranium, pH, calcium, coordinates
- clean missing values
- remove duplicates
- validate coordinate consistency
- create hotspot labels

**01_build_uranium_dataset.py
02_hotspot_mapping.py
03_train_risk_model.py
04_driver_analysis.py
05_groundwater_overlay.py**
                  
### Tools / Skills:
- Python
- pandas
- geopandas
- numpy

### Deliverables:

summary:
count    28470.00
mean         2.04
std          1.92
min          0.10
25%          1.10
50%          1.60
75%          2.40
max         75.60
Name: u_ppm, dtype: float64
 Median 1.60
Skewness 11.52
Uranium hotspt conc: 4.7, elevated conc: 2.4, median conc: 1.6, and lower conc1.1
Hotspot threshold (95th percentile): 4.70 ppm
Number of hotspot samples: 1427

- cleaned uranium geodataset
- processed GeoDataFrame
- hotspot-tagged dataset

---

# Phase 2 — Uranium Hotspot Intelligence Mapping

### Objective:
Identify statistically elevated uranium zones.

### Tasks:
- compute percentile thresholds
- define 95th percentile uranium anomaly threshold
- classify hotspot samples
- create uranium hotspot map
- visualize concentration gradients

### Tools / Skills:
- descriptive statistics
- percentile anomaly logic
- matplotlib
- geopandas plotting

### Deliverables:
- uranium hotspot map
- anomaly threshold report
- hotspot candidate layer

---

# Phase 3 — Spatial Prediction Engine

### Objective:
Predict elevated uranium probability in unsampled areas.

### Tasks:
- create hotspot classification target
- train random forest model
- predict hotspot probability
- generate uranium probability surface

### Input Predictors:
- pH
- calcium
- Fe (if available)
- lithology
- coordinates

### Tools / Skills:
- scikit-learn
- random forest classifier
- train/test split
- ROC-AUC validation

### Deliverables:
- trained prediction model
- probability risk map
- model performance metrics

---

# Phase 4 — Geological Driver Intelligence

### Objective:
Identify what controls uranium enrichment.

### Tasks:
- rank variable importance
- compare geological drivers
- analyze predictor influence

### Tools / Skills:
- feature importance analysis
- permutation importance
- partial dependence interpretation

### Deliverables:
- driver ranking chart
- geological influence summary

---

# Phase 5 — Groundwater Exposure Screening Layer

### Objective:
Estimate where uranium hazard may intersect groundwater exposure risk.

### Overlay Inputs:
- uranium probability zones
- aquifer layers
- private well proxy layers
- groundwater vulnerability layers

### Tasks:
- overlay hazard + pathway + receptor layers
- identify exposure-priority zones

### Tools / Skills:
- GIS overlay analysis
- QGIS spatial layer integration
- geospatial risk screening

### Deliverables:
- groundwater exposure screening map
- priority zone identification layer

---

# Software Stack

---

## Core Programming Stack

### Python Libraries:
- pandas
- geopandas
- numpy
- matplotlib
- scikit-learn
- shapely
- rasterio

---

## GIS Platform:
### QGIS

Used for:
- geology overlays
- aquifer layers
- map validation
- final visualization exports

---

## Optional Advanced Spatial Tool:
### PyKrige

Use if adding:
- kriging interpolation
- geostatistical prediction surfaces

---

# Recommended Learning Stack

---

## 1. Machine Learning
### HarvardX CS109x

Use for:
- decision trees
- random forest modeling
- boosting methods

---

## 2. GIS Spatial Skills
Need:
### QGIS practical training

Learn:
- shapefile handling
- raster overlays
- layer joins

---

## 3. Spatial Analytics Upgrade
Learn:
- Moran’s I
- hotspot clustering
- spatial autocorrelation

---

## 4. Environmental Geochemistry Upgrade
Need:
- uranium mobility interpretation
- pH-carbonate uranium chemistry basics

Optional:
- PHREEQC intro

---

# Dataset Sources

### Primary:
SGU Markgeokemi Regional Dataset

### Additional:
- SGU geological layers
- SGU groundwater layers
- aquifer datasets
- bedrock maps

---

# Final Output Portfolio Package

At completion this project produces:

### Maps:
1. Uranium hotspot map  
2. Uranium probability risk zonation map  
3. Geological driver map  
4. Groundwater exposure screening map  

### Technical Outputs:
- predictive ML model
- reusable geospatial workflow
- environmental risk intelligence pipeline

---

# Why This Project Matters Professionally

This is not a descriptive academic exercise.

This project demonstrates ability to build:
### decision-support environmental intelligence systems

That is directly relevant for:
- environmental consulting companies
- groundwater agencies
- mining/environmental regulators
- geospatial environmental analytics roles

---

# Career Value

This project positions your profile toward:

### Target roles:
- Environmental Data Analyst
- Geospatial Environmental Consultant
- Groundwater Risk Analyst
- Environmental GIS Specialist
- Contaminated Land Data Analyst

---

# Development Priority Order

Build in this sequence:

1. Phase 1 → data pipeline  
2. Phase 2 → hotspot mapping  
3. Phase 3 → prediction model  
4. Phase 4 → driver analysis  
5. Phase 5 → exposure screening  

---

# Current Project Status

[x] uranium data extraction started  
[x] hotspot threshold identified  
[x] exploratory mapping underway  
[ ] predictive model pending  
[ ] groundwater overlay pending  

---

# End Goal

Create a deployable environmental geodata intelligence workflow that converts raw SGU uranium measurements into actionable groundwater risk screening outputs.




