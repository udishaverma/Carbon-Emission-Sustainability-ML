"""
Feature engineering functions.
"""

import pandas as pd


def create_regression_features(
    df: pd.DataFrame,
    feature_columns: list[str]
) -> pd.DataFrame:
    """Return the selected regression features."""
    return df[feature_columns].copy()


def add_co2_lags(
    df: pd.DataFrame,
    lags: list[int] = [1, 2, 3]
) -> pd.DataFrame:
    """Create country-specific CO₂ lag features."""
    result = df.sort_values(
        ["country", "year"]
    ).copy()

    for lag in lags:
        result[f"co2_lag_{lag}"] = (
            result.groupby("country")["co2"].shift(lag)
        )

    return result