# Raw Data

This folder holds the raw loan approval dataset. The file itself is **gitignored** because raw data should not be committed to version control.

## Dataset

**Name:** Loan Approval Prediction Dataset
**Author:** Muhammad Musharraf
**Source:** https://www.kaggle.com/datasets/muhammadmusharraf444/loan-approval-dataset
**License:** See Kaggle page
**Size:** 45,000 rows × 14 columns
## How to Download
# Requires ~/.kaggle/kaggle.json
kaggle datasets download -d muhammadmusharraf444/loan-approval-dataset -p data/raw/
unzip data/raw/loan-approval-dataset.zip -d data/raw/
mv data/raw/loan_data_new.csv data/raw/loan_data_new.csv


