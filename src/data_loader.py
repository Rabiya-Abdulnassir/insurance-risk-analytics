import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load insurance dataset.
    """
    df = pd.read_csv(path)

    return df
