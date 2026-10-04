"""
Project configuration: paths, constants, feature lists, column mappings.
"""

from pathlib import Path

# ---------- Paths ----------
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

MODEL_DIR = PROJECT_ROOT / "models"
REPORT_DIR = PROJECT_ROOT / "reports"
FIGURE_DIR = REPORT_DIR / "figures"

# ---------- Data ----------
RAW_DATA_FILE = RAW_DIR / "loan_data_new.csv"

# ---------- Target ----------
TARGET = "Loan Status"
TARGET_POSITIVE_LABEL = 1  # 1 = Approved, 0 = Rejected

# ---------- Original raw column names (as they appear in CSV) ----------
RAW_NUMERIC_FEATURES = [
    "Age",
    "Person Income",
    "Employee Experience",
    "Loan Amount",
    "Loan interest Rate",
    "Loan percentage",
    "Credit Score",
]

RAW_CATEGORICAL_FEATURES = [
    "Gender",
    "Education",
    "Home Onwership",   # NOTE: typo preserved from source
    "Loan Intent",
    "Previous Loan",
    "Credit History",
]

# ---------- Clean snake_case names we rename to ----------
RENAME_MAP = {
    "Age": "age",
    "Gender": "gender",
    "Education": "education",
    "Person Income": "person_income",
    "Employee Experience": "employee_experience",
    "Home Onwership": "home_ownership",
    "Loan Amount": "loan_amount",
    "Loan Intent": "loan_intent",
    "Loan interest Rate": "loan_interest_rate",
    "Loan percentage": "loan_percentage",
    "Credit History": "credit_history",
    "Credit Score": "credit_score",
    "Previous Loan": "previous_loan",
    "Loan Status": "loan_status",
}

# ---------- Final feature names (after rename) ----------
NUMERIC_FEATURES = [
    "age",
    "person_income",
    "employee_experience",
    "loan_amount",
    "loan_interest_rate",
    "loan_percentage",
    "credit_score",
]

CATEGORICAL_FEATURES = [
    "gender",
    "education",
    "home_ownership",
    "loan_intent",
    "previous_loan",
    "credit_history",
]

TARGET_CLEAN = "loan_status"

# ---------- Training ----------
RANDOM_STATE = 42
TEST_SIZE = 0.2
CV_FOLDS = 5
SCORING = "roc_auc"

# ---------- Model persistence ----------
BEST_MODEL_FILE = MODEL_DIR / "best_model.pkl"
PREPROCESSOR_FILE = MODEL_DIR / "preprocessor.pkl"
