import pandas as pd  # type: ignore
import numpy as np  # type: ignore


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
    }

    if len(numeric_columns) > 0:
        result["statistics"] = df[numeric_columns].describe().to_dict()

    return result
