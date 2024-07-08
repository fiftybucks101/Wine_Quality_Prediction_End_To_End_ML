from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unziped_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

from typing import Optional

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    TARGET_COLUMN: str
    max_depth: Optional[int]
    max_features: str
    min_samples_split: int
    n_estimators: int

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    train_data_path: Path
    test_data_path: Path
    train_metrics_file: str
    test_metrics_file: str
    name: str
    model_name: str