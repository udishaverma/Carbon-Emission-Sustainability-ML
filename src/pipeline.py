"""
High-level project pipeline orchestration.
"""

from pathlib import Path
import pandas as pd


def load_modeling_data(
    path: Path
) -> pd.DataFrame:
    """Load the processed modeling dataset."""
    return pd.read_csv(path)


def run_pipeline() -> pd.DataFrame:
    """
    Entry point for the high-level project workflow.

    Detailed orchestration can be implemented when the
    notebook workflow is migrated into reusable modules.
    """
    raise NotImplementedError(
        "Pipeline orchestration is planned for the modular implementation phase."
    )