# Loan Approval Prediction

> An end-to-end machine learning system that predicts loan approval decisions with explainability and deployment.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Business Problem

Manual loan approval is slow, inconsistent, and costly. This project builds a machine learning decision-support system that:

- Auto-approves low-risk applications in seconds
- Flags high-risk applications for manual review
- Explains every decision using SHAP


## Dataset

**Source:** [Loan Approval Prediction Dataset on Kaggle](https://www.kaggle.com/datasets/muhammadmusharraf444/loan-approval-dataset)

- 45,000 applications
- 14 features (demographics, financial, credit history)
- Target: `Loan Status` (Approved / Rejected)
See `data/raw/README.md` for details.