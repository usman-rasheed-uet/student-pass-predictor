# Error Analysis

Misclassified rows on the held-out test set (actual != predicted):

```
 hours_studied  attendance  practice_tests  sleep_hours study_method  actual  predicted
           7.6          88               0          5.0        group       0          1
           2.9          89               6          8.5        video       1          0
           6.4          76               5          8.5         self       0          1
           8.0          93               0          5.7         self       1          0
           7.0          89               3          8.2         self       0          1
```

## Interpretation

- **FN (actual Pass, predicted Fail)** — at-risk students the model missed. Most costly for a support use-case.
- **FP (actual Fail, predicted Pass)** — false alarms: students flagged as passing who actually failed.

Inspect the sample above: do any of them look unusual in a single feature
(e.g. very low practice_tests but high attendance)?
That can hint at which feature the model over-weights.

**Note:** `final_score` was NOT a model feature, so any misclassification is a genuine learning error, not a leakage artefact.