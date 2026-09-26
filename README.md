# P_132 Carbon Emission Prediction and Sustainability Modeling Framework

## Overview

P_132 is a Python-based machine learning and sustainability analysis project that studies annual country-level CO₂ emissions using socioeconomic and energy-system indicators.

The project integrates Our World in Data (OWID) CO₂ and Energy datasets using country and year, performs systematic data-quality and coverage screening, engineers predictive features, develops regression models, evaluates model performance, performs chronological time-series forecasting, and investigates statistical relationships between renewable-energy indicators and CO₂ emissions.

## Project Objectives

- Build a reproducible country-year CO₂ modeling dataset.
- Predict annual CO₂ emissions using socioeconomic and energy-related indicators.
- Compare multiple regression algorithms.
- Evaluate predictive performance using MAE, RMSE and R².
- Develop a lag-based chronological forecasting model.
- Study statistical relationships between renewable-energy indicators and CO₂ emissions.
- Generate analytical visualizations for interpretation.

## Dataset

The project uses publicly documented datasets from Our World in Data:

- OWID CO₂ dataset
- OWID Energy dataset

The datasets are merged using:

- `country`
- `year`

After coverage screening, the primary modeling dataset contains:

- 79 countries
- 2000–2022
- 1,817 observations
- 13 predictive features
- 1 target variable
- 2 identifier columns

## Machine Learning Models

The primary regression experiment compares:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

Gradient Boosting produced the strongest recorded test performance:

- MAE: 22.5743 Mt
- RMSE: 68.9022 Mt
- R²: 0.9973

A separate lag-based Gradient Boosting model is used for chronological time-series forecasting.

## Time-Series Forecasting

Three country-specific lag variables are created:

- CO₂ lag 1
- CO₂ lag 2
- CO₂ lag 3

The forecasting experiment uses chronological training, validation and testing rather than a random split.

Recorded test performance:

- MAE: 51.5167 Mt
- RMSE: 240.9586 Mt
- R²: 0.9711

## Renewable-Energy Analysis

The project also investigates renewable-energy relationships using:

- renewable-energy trends
- renewable-adoption groups
- correlation analysis
- controlled standardized regression

The controlled regression is interpreted as an association analysis rather than a causal study.

## Project Workflow

Data Collection
→ Data Quality Audit
→ Dataset Integration
→ Coverage Screening
→ Feature Engineering
→ Exploratory Data Analysis
→ Regression Modeling
→ Model Evaluation
→ Time-Series Forecasting
→ Renewable-Energy Analysis
→ Visualization

## Repository Structure

```text
notebooks/       ML and data-analysis notebooks
data/            Datasets
visualizations/  Generated analytical visualizations
docs/            Project documentation# Carbon-Emission-Sustainability-ML
outputs/         Generated files