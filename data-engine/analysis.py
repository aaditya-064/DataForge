import pandas as pd  # type: ignore
import numpy as np  # type: ignore


# ? get the column datatype on the basis of columns
def get_column_type(column):
    if pd.api.types.is_numeric_dtype(column):
        return "nuemric"

    if pd.api.types.is_bool_dtype(column):
        return "boolean"

    date_column = pd.to_datetime(
        column, errors="coerce"
    )  # * errors="coerce" => if not valid, then don't crash, keep it invalid

    if date_column.notna().mean() >= 0.8:
        return "date"

    unique_values = column.nunique()

    if unique_values <= 20:
        return "categorical"

    return "text"


def analyze_columns(df):
    columns = []

    for name in df.columns:
        column = df[name]

        columns.append(
            {
                "name": name,
                "type": get_column_type(column),
                "missing": int(column.isna().sum()),
                "unique": int(column.nunique()),
            }
        )

        return columns


def analyze_csv(file_path):
    df = pd.read_csv(file_path)

    numeric_columns = df.select_dtypes(include=np.number).columns

    result = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "numeric_columns": list(numeric_columns),
        "column_analysis": analyze_columns(df),
    }

    if len(numeric_columns) > 0:
        result["statistics"] = df[numeric_columns].describe().to_dict()

    return result
