"""Common preprocessing utilities for the Water Quality project."""

from pathlib import Path

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ============================================================
# CẤU HÌNH DỮ LIỆU
# ============================================================

TARGET_COLUMN = "Potability"

FEATURE_COLUMNS = [
    "ph",
    "Hardness",
    "Solids",
    "Chloramines",
    "Sulfate",
    "Conductivity",
    "Organic_carbon",
    "Trihalomethanes",
    "Turbidity",
]

TEST_SIZE = 0.20
RANDOM_STATE = 42

# ============================================================
# ĐỌC DATASET
# ============================================================

def load_dataset(file_path):
    """
    Đọc dataset từ file CSV.

    Parameters
    ----------
    file_path : str | Path
        Đường dẫn tới file CSV.

    Returns
    -------
    pandas.DataFrame
        Dataset đã được đọc.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Không tìm thấy dataset tại: {file_path}"
        )

    dataframe = pd.read_csv(file_path)

    return dataframe


# ============================================================
# KIỂM TRA CẤU TRÚC DATASET
# ============================================================

def validate_dataset_columns(dataframe):
    """
    Kiểm tra dataset có đầy đủ 9 feature và target hay không.

    Raises
    ------
    ValueError
        Nếu dataset thiếu cột bắt buộc.
    """

    required_columns = FEATURE_COLUMNS + [TARGET_COLUMN]

    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Dataset thiếu các cột bắt buộc: {missing_columns}"
        )

    return True


# ============================================================
# TÁCH FEATURE VÀ TARGET
# ============================================================

def split_features_target(dataframe):
    """
    Tách dataset thành X và y.

    Returns
    -------
    X : pandas.DataFrame
        9 feature đầu vào.

    y : pandas.Series
        Biến mục tiêu Potability.
    """

    validate_dataset_columns(dataframe)

    X = dataframe[FEATURE_COLUMNS].copy()
    y = dataframe[TARGET_COLUMN].copy()

    return X, y


def split_train_test(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
):
    """
    Chia dữ liệu thành tập train và test.

    Sử dụng stratify=y để giữ tỷ lệ hai lớp Potability
    gần giống nhau giữa train và test.

    Parameters
    ----------
    X : pandas.DataFrame
        Các feature đầu vào.

    y : pandas.Series
        Biến mục tiêu Potability.

    test_size : float
        Tỷ lệ dữ liệu dành cho test.

    random_state : int
        Seed giúp kết quả chia dữ liệu có thể tái lập.

    Returns
    -------
    X_train, X_test, y_train, y_test
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

# ============================================================
# PIPELINE CÓ STANDARD SCALER
# ============================================================

def build_scaled_preprocessor():
    """
    Tạo preprocessing pipeline dành cho các model cần scaling.

    Pipeline:
        Median Imputation
        -> StandardScaler

    Phù hợp với:
        - Logistic Regression
        - SVM
        - KNN

    Lưu ý:
        Hàm chỉ tạo pipeline.
        Pipeline chưa được fit trên dữ liệu.
    """

    pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
        ]
    )

    return pipeline


# ============================================================
# PIPELINE KHÔNG SCALE
# ============================================================

def build_unscaled_preprocessor():
    """
    Tạo preprocessing pipeline dành cho model không cần scaling.

    Pipeline:
        Median Imputation

    Phù hợp với:
        - Random Forest

    Lưu ý:
        Hàm chỉ tạo pipeline.
        Pipeline chưa được fit trên dữ liệu.
    """

    pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median"),
            ),
        ]
    )

    return pipeline