# Model Card — Student Pass Predictor (teaching demo)

| Field | Value |
|---|---|
| Task | Binary classification: passed = 1 / 0 |
| Intended use | Classroom ML demonstration only |
| NOT for | Real student assessment, ranking, or disciplinary decisions |
| Inputs | hours_studied, attendance, practice_tests, sleep_hours, study_method |
| Excluded | final_score (leakage), personal identifiers |
| Data | 280 synthetic records |
| Split | Stratified 80/20, random_state=42 |
| Preprocessing | median + StandardScaler (num); most_frequent + OneHotEncoder (cat) |
| Models | DummyClassifier, LogisticRegression, RandomForestClassifier |
| Primary metric | Test F1 (with accuracy/precision/recall/confusion matrix) |
| Limitations | Synthetic; small sample; unaudited for fairness |
| Privacy | No personal or sensitive data used |
| Human oversight | Real use would require human review |
| Artifact | `student_pass_pipeline.joblib` — load only from trusted sources |