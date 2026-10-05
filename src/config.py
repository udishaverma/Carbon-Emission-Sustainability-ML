"""
Project configuration.

Stores shared paths, feature definitions and
reproducibility settings.
"""

from pathlib import Path

RANDOM_STATE = 42

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUT_DIR = PROJECT_ROOT / "outputs"
VISUALIZATION_DIR = PROJECT_ROOT / "visualizations"

MODELING_DATA_PATH = PROCESSED_DATA_DIR / "modeling_data.csv"

TARGET = "co2"

FEATURES = [
    "year",
    "population_co2",
    "gdp_co2",
    "primary_energy_consumption_energy",
    "fossil_share_energy",
    "renewables_share_energy",
    "renewables_electricity",
    "renewables_share_elec",
    "solar_share_energy",
    "wind_share_energy",
    "hydro_share_energy",
    "gdp_per_capita",
    "energy_per_capita",
]