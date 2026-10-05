"""
Time-series forecasting functions.
"""

from sklearn.ensemble import GradientBoostingRegressor


def build_forecasting_model(
    random_state: int = 42
) -> GradientBoostingRegressor:
    """Create the lag-based forecasting model."""
    return GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=3,
        random_state=random_state
    )