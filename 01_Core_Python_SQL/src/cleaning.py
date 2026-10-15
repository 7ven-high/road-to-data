"""Reusable cleaning helpers."""
import pandas as pd


def drop_duplicate_ids(df: pd.DataFrame, id_col: str) -> pd.DataFrame:
    """Keep the first row for each id."""
    return df.drop_duplicates(subset=id_col, keep="first").reset_index(drop=True)
