import pandas as pd


def missing_values(df):

    missing = df.isnull().sum()

    percent = (missing / len(df)) * 100

    summary = pd.DataFrame({
        "missing_count": missing,
        "missing_percent": percent
    })

    return summary.sort_values(
        by="missing_percent",
        ascending=False
    )


def calculate_loss_ratio(df):

    return (
        df["TotalClaims"].sum()
        / df["TotalPremium"].sum()
    )


def group_loss_ratio(df, group_col):

    grouped = (
        df.groupby(group_col)[
            ["TotalClaims", "TotalPremium"]
        ]
        .sum()
    )

    grouped["LossRatio"] = (
        grouped["TotalClaims"]
        / grouped["TotalPremium"]
    )

    return grouped.sort_values(
        by="LossRatio",
        ascending=False
    )