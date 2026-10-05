# Carbon Emission Prediction and Sustainability Modeling Framework

## Overview

This repository contains a Python-based machine learning and sustainability analysis project focused on annual country-level carbon dioxide (CO₂) emissions. It uses socioeconomic, demographic and energy-system indicators to study emission patterns, develop regression models, evaluate forecasts and analyze renewable-energy relationships.

The project integrates publicly available CO₂ and Energy datasets from Our World in Data (OWID), performs data cleaning and feature engineering, conducts exploratory data analysis, compares regression algorithms, develops time-series forecasting models and generates visualizations.

The core analytical notebooks are shared project materials. Notebook 10 contains supplementary experimental evaluation for the YuvaIntern assignment, with its results stored separately from the core project outputs.

## Project Objectives

- Prepare a reproducible country-year CO₂ modeling dataset.
- Predict annual CO₂ emissions using socioeconomic and energy-related indicators.
- Compare Linear Regression, Random Forest and Gradient Boosting.
- Evaluate models using MAE, RMSE and R².
- Assess country-level generalization through grouped cross-validation.
- Evaluate temporal performance through rolling-origin experiments.
- Compare the forecasting model against a persistence baseline.
- Analyze renewable-energy relationships with CO₂ emissions.
- Generate visualizations and document methodological limitations.

## Dataset

The project uses two publicly available datasets from Our World in Data:

- CO₂ dataset: https://ourworldindata.org/co2-and-greenhouse-gas-emissions
- Energy dataset: https://catalog.ourworldindata.org/energy_data/owid_energy/

The datasets are integrated using country and year.

After data cleaning and coverage screening, the primary modeling dataset contains:

| Attribute | Value |
|---|---:|
| Countries | 79 |
| Period | 2000–2022 |
| Observations | 1,817 |
| Predictive features | 13 |
| Target variable | Annual CO₂ emissions (`co2`) |
| Target unit | Million tonnes (Mt) |

The predictive features include year, population, GDP, primary energy consumption, fossil-fuel share, renewable-energy indicators, electricity-generation indicators, GDP per capita and energy consumption per capita.

The raw datasets and codebooks are stored in `data/raw/`, while the processed datasets are stored in `data/processed/`.

## Machine Learning Models

The primary regression experiment implements and compares three algorithms:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

### Model Configurations

- **Linear Regression:** StandardScaler preprocessing followed by ordinary least squares regression.
- **Random Forest:** 300 estimators, `random_state=42`, and `n_jobs=-1`.
- **Gradient Boosting:** 200 estimators, learning rate 0.05, maximum tree depth 3 and `random_state=42`.

The primary regression experiment uses a random 70/15/15 training, validation and test split with `random_state=42`. Model selection is based on validation RMSE, and the held-out test set is used for final evaluation.

### Regression Results

Gradient Boosting achieved the lowest validation RMSE and highest validation R², while Random Forest achieved the lowest validation MAE. Gradient Boosting was selected using validation RMSE.

| Model | Validation MAE (Mt) | Validation RMSE (Mt) | Validation R² |
|---|---:|---:|---:|
| Linear Regression | 61.5610 | 101.1142 | 0.9925 |
| Random Forest | 16.3121 | 60.7112 | 0.9973 |
| Gradient Boosting | 20.9371 | 41.6238 | 0.9987 |

Selected Gradient Boosting test results:

| Metric | Test result |
|---|---:|
| MAE | 22.5743 Mt |
| RMSE | 68.9022 Mt |
| R² | 0.9973 |

These random-split regression results should not be interpreted as evidence of future-year or unseen-country generalization.

## Country-Grouped Cross-Validation

Five-fold `GroupKFold` cross-validation is performed on the original regression training subset, using country as the grouping variable. This evaluates performance on countries excluded from each fold's training data.

### Cross-Validation Results

| Model | Mean fold RMSE (Mt) | Pooled OOF RMSE (Mt) | Pooled OOF R² |
|---|---:|---:|---:|
| Linear Regression | 223.6568 | 283.7029 | 0.9345 |
| Random Forest | 402.3206 | 535.4261 | 0.7665 |
| Gradient Boosting | 411.5741 | 582.8486 | 0.7233 |

Linear Regression achieved the lowest mean fold and pooled out-of-fold RMSE in this experiment. This differs from the original random-split validation results, illustrating that model performance depends on the evaluation scenario.

## Time-Series Forecasting

A separate lag-based Gradient Boosting model is used for chronological forecasting. It incorporates three country-specific historical CO₂ features:

- CO₂ lag 1
- CO₂ lag 2
- CO₂ lag 3

The forecasting model uses 300 estimators, a learning rate of 0.05, maximum tree depth 3 and `random_state=42`.

The rolling-origin validation uses expanding training windows and five successive validation years from 2012 to 2016. The final chronological test comparison covers the available observations from 2021 and 2022, with the model trained on observations through 2016.

The evaluation uses observed same-year socioeconomic and energy-related predictors and historical CO₂ lags. The test predictions therefore represent conditional, sequential one-year-ahead predictions rather than a fixed-origin multiyear forecast.

### Forecasting Test Results

| Metric | Gradient Boosting | Persistence baseline |
|---|---:|---:|
| MAE | 51.5167 Mt | 20.1835 Mt |
| RMSE | 240.9586 Mt | 60.7773 Mt |
| R² | 0.9711 | 0.9982 |

The persistence baseline uses the previous year's observed CO₂ emissions. It outperformed Gradient Boosting on the reported aggregate metrics in both the rolling-origin validation and the chronological test period.

The future projections for 2023–2027 carry forward the latest observed non-lag predictors while updating the year and CO₂ lag features recursively. They are conditional projections, not forecasts of future economic or energy indicators.

## Renewable-Energy Analysis

The project investigates the relationships between renewable-energy indicators and CO₂ emissions through:

- Renewable-energy trends
- Renewable-adoption groups
- Correlation analysis
- Controlled standardized regression

The controlled regression is interpreted as an analysis of statistical association, not as proof of causation.

## Error Analysis

The regression and forecasting experiments include:

- Actual-versus-predicted visualizations
- Residual analysis
- Largest absolute prediction errors
- Country-wise error summaries
- Investigation of unusually large forecasting errors
- Comparison against a persistence baseline

The rolling-origin analysis identified substantial Gradient Boosting overprediction of India's emissions in 2014 and 2015. These observations contributed 99.44% and 98.38%, respectively, of the total squared errors in those validation years. The analysis identifies the errors but does not establish their cause.

## Project Workflow

```text
Data Collection
      |
Data Understanding and Quality Audit
      |
Dataset Integration
      |
Coverage and Missingness Screening
      |
Feature Engineering
      |
Exploratory Data Analysis
      |
Regression Modeling
      |
Model Evaluation
      |
Time-Series Forecasting
      |
Renewable-Energy Analysis
      |
Experimental Evaluation
      |
Visualization and Documentation
```

## Repository Structure

```text
Carbon-Emission-Sustainability-ML/
|
|-- data/
|   |-- raw/
|   |   |-- owid-co2-codebook.csv
|   |   |-- owid-co2-data.csv
|   |   |-- owid-energy-codebook.csv
|   |   |-- owid-energy-data.csv
|   |
|   |-- processed/
|       |-- cleaned_data.csv
|       |-- merged_model_base.csv
|       |-- modeling_data.csv
|
|-- docs/
|   |-- architecture/
|       |-- system_architecture.png
|       |-- implementation_workflow.png
|   |-- YuvaIntern_Task1_Project_Plan.docx
|   |-- YuvaIntern_Task2_Algorithm_Exploration.docx
|   |-- YuvaIntern_Task3_Experimental_Design_and_Evaluation_Metric_Formulation.docx
|   |-- YuvaIntern_Task4_Implementation_Strategy_and_Code_Architecture.docx
|
|-- notebooks/
|   |-- 01_data_understanding.ipynb
|   |-- 02_data_cleaning.ipynb
|   |-- 03_feature_engineering.ipynb
|   |-- 04_exploratory_data_analysis.ipynb
|   |-- 05_regression_modeling.ipynb
|   |-- 06_time_series_forecasting.ipynb
|   |-- 07_model_evaluation.ipynb
|   |-- 08_renewable_energy_impact.ipynb
|   |-- 09_visualizations.ipynb
|   |-- 10_yuvaintern_experimental_evaluation.ipynb
|
|-- outputs/
|   |-- feature_importance.csv
|   |-- model_evaluation.csv
|   |
|   |-- yuvaintern_evaluation/
|       |-- grouped_cv_fold_results.csv
|       |-- grouped_cv_pooled_results.csv
|       |-- grouped_cv_summary.csv
|       |-- grouped_cv_rmse.png
|       |-- rolling_origin_fold_results.csv
|       |-- rolling_origin_predictions.csv
|       |-- rolling_origin_summary.csv
|       |-- rolling_origin_pooled_results.csv
|       |-- rolling_origin_performance.png
|       |-- persistence_baseline_yearly.csv
|       |-- persistence_baseline_summary.csv
|       |-- persistence_baseline_pooled.csv
|       |-- final_test_baseline_comparison.csv
|       |-- final_test_baseline_yearly.csv
|
|-- src/
|   |-- __init__.py
|   |-- config.py
|   |-- data.py
|   |-- features.py
|   |-- models.py
|   |-- forecasting.py
|   |-- evaluation.py
|   |-- visualization.py
|   |-- pipeline.py
|   |-- main.py
|
|-- visualizations/
|   |-- exploratory/
|   |-- forecasting/
|   |-- regression/
|   |-- renewable_energy/
|
|-- .gitignore
|-- requirements.txt
|-- README.md
```

Notebook 10 and its output directory are supplementary YuvaIntern evaluation materials. The first nine notebooks contain the shared project analysis.

## Notebook Guide

| Notebook | Purpose |
|---|---|
| 01 | Data Understanding |
| 02 | Data Cleaning |
| 03 | Feature Engineering |
| 04 | Exploratory Data Analysis |
| 05 | Regression Modeling |
| 06 | Time-Series Forecasting |
| 07 | Model Evaluation |
| 08 | Renewable-Energy Impact Analysis |
| 09 | Visualizations |
| 10 | YuvaIntern Experimental Evaluation |

Notebook 10 performs country-grouped cross-validation, expanding-window rolling-origin evaluation, persistence-baseline comparison and additional error analysis. Its outputs are stored separately under `outputs/yuvaintern_evaluation/` to avoid overwriting the core project results.

## Modular Architecture

The `src/` directory contains the planned modular Python architecture
for migrating reusable functionality from the analytical notebooks
into maintainable components.

| Module | Responsibility |
|---|---|
| `config.py` | Project paths, feature definitions and configuration |
| `data.py` | Data loading and validation |
| `features.py` | Feature selection and CO₂ lag generation |
| `models.py` | Regression model definitions |
| `forecasting.py` | Forecasting model definitions and forecasting logic |
| `evaluation.py` | Model metrics and evaluation procedures |
| `visualization.py` | Plot generation and saving |
| `pipeline.py` | High-level workflow orchestration |
| `main.py` | Main execution entry point |

The current `src/` implementation establishes the architecture and
interfaces. The existing notebooks remain the primary implementation
of the completed analytical workflows.

## Reproducibility

### Requirements

Python and the libraries listed in `requirements.txt`.

### Setup

Clone the repository:

```bash
git clone https://github.com/udishaverma/Carbon-Emission-Sustainability-ML.git
cd Carbon-Emission-Sustainability-ML
```

Create and activate a virtual environment.

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Launch Jupyter:

```bash
jupyter notebook
```

Open the notebooks from the `notebooks/` directory and execute them in numerical order. Ensure the required raw and processed datasets are available at the relative paths expected by the notebooks.

## Data Sources

- **Our World in Data CO₂ dataset:** https://ourworldindata.org/co2-and-greenhouse-gas-emissions
- **Our World in Data Energy dataset:** https://catalog.ourworldindata.org/energy_data/owid_energy/

The original datasets and codebooks are organized under `data/raw/`. Processed datasets are stored under `data/processed/`.

Dataset versions, retrieval dates and applicable source attribution should be recorded when available to support reproducibility.