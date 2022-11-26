import pandas as pd
import re


def standardize_desc(series: pd.Series) -> pd.Series:
    """Standardizes description series such as rank and department

    Args:
        series (pd.Series):
            the series to process

    Returns:
        the updated series
    """
    return series.str.strip().str.lower().fillna("")


def standardize_desc_cols(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Cleans and standardize description columns

    Args:
        df (pd.DataFrame):
            the frame to process
        cols (list of str):
            descriptive columns such as rank_desc and department_desc

    Returns:
        the updated frame
    """
    for col in cols:
        df.loc[:, col] = standardize_desc(df[col])
    return df


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Removes unnamed columns and convert column names to snake case

    Args:
        df (pd.DataFrame):
            the frame to process

    Returns:
        the updated frame
    """
    df = df[[col for col in df.columns if not col.startswith("Unnamed:")]]
    df.columns = [
        re.sub(r"[\s\W]+", "_", col.strip()).lower().strip("_") for col in df.columns
    ]
    return df
