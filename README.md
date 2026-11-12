# Student Pass Prediction — Module 03 Baseline

## Goal
Predict `passed` (1) or `fail` (0) using features known before the final exam.

## Data
`student_learning.csv` — 280 synthetic records.
Target: `passed`. Excluded: `final_score` (target leakage).

## Workflow
1. Inspect rows, dtypes, missingness, target balance.
2. Stratified 80/20 split (`random_state=42`).
3. DummyClassifier baseline.
4. ColumnTransformer: median + StandardScaler (numeric); most_frequent + OneHotEncoder (categorical).
5. LogisticRegression + RandomForestClassifier, wrapped in a Pipeline.
6. Evaluate on the SAME held-out test set: accuracy, precision, recall, F1, confusion matrix.
7. Save pipeline with joblib; reload and predict `new_student_records.csv`.

## Files
- `Module03_Project.ipynb` — notebook
- `student_pass_pipeline.joblib` — fitted pipeline
- `evaluation_summary.md`, `error_analysis.md`, `model_card.md`
- `app.py` — Streamlit form
- `confusion_matrix.png`, `model_comparison.png`, `feature_importance.png`

## How to run
```bash
pip install streamlit joblib scikit-learn pandas matplotlib
python -m streamlit run app.py
```

## Reproducibility
All splits use `random_state=42`; the saved pipeline fully reproduces predictions.

## Limitations
Synthetic classroom data — for teaching only; not for real student decisions.