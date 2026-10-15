# Data

**Rule: no real or confidential data in this repository.**

## Layers
| Folder | Content | Versioned in Git? |
|--------|---------|-------------------|
| `raw/` | Original data, never modified | No |
| `sample/` | Small extracts (<1 MB) for demos and tests | Yes |
| `interim/` | Intermediate transformations | No |
| `processed/` | Final tables used for BI / ML | No |

## Sources (fill in)
| Dataset | Source | License | Used in phase |
|---------|--------|---------|---------------|
| Synthetic NordBank | `scripts/generate_synthetic.py` | own work | all |
| Credit Card Fraud (example) | Kaggle | check page | 05 |
| Destatis / GENESIS (example) | destatis.de | check page | 02 |

## Data dictionary
See each table below (update when schema changes).

| Table | Columns |
|-------|---------|
| customers | customer_id, name, birth_date, city, segment, created_at |
| accounts | account_id, customer_id, type, opened_at |
| transactions | transaction_id, account_id, amount, category, ts, is_fraud |
| loans | loan_id, customer_id, amount, rate, status |
