"""Generate synthetic NordBank data into data/raw/ and a small sample into data/sample/.

Usage: python data/scripts/generate_synthetic.py [--rows 10000] [--seed 42]
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw"
SAMPLE = ROOT / "data" / "sample"


def generate(rows: int, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    fake = Faker("de_DE")
    Faker.seed(seed)

    n_customers = max(rows // 10, 10)
    customers = pd.DataFrame({
        "customer_id": range(1, n_customers + 1),
        "name": [fake.name() for _ in range(n_customers)],
        "birth_date": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(n_customers)],
        "city": [fake.city() for _ in range(n_customers)],
        "segment": rng.choice(["retail", "premium", "student"], n_customers, p=[0.7, 0.1, 0.2]),
        "created_at": [fake.date_between(start_date="-10y") for _ in range(n_customers)],
    })

    n_accounts = int(n_customers * 1.3)
    accounts = pd.DataFrame({
        "account_id": range(1, n_accounts + 1),
        "customer_id": rng.integers(1, n_customers + 1, n_accounts),
        "type": rng.choice(["checking", "savings"], n_accounts, p=[0.7, 0.3]),
        "opened_at": [fake.date_between(start_date="-10y") for _ in range(n_accounts)],
    })

    transactions = pd.DataFrame({
        "transaction_id": range(1, rows + 1),
        "account_id": rng.integers(1, n_accounts + 1, rows),
        "amount": np.round(rng.lognormal(3.5, 1.0, rows), 2),
        "category": rng.choice(["groceries", "rent", "travel", "salary", "leisure"], rows),
        "ts": pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 365 * 24 * 3600, rows), unit="s"),
        "is_fraud": rng.random(rows) < 0.002,
    })

    n_loans = max(n_customers // 3, 5)
    loans = pd.DataFrame({
        "loan_id": range(1, n_loans + 1),
        "customer_id": rng.integers(1, n_customers + 1, n_loans),
        "amount": np.round(rng.uniform(1000, 50000, n_loans), 2),
        "rate": np.round(rng.uniform(0.02, 0.09, n_loans), 4),
        "status": rng.choice(["active", "repaid", "default"], n_loans, p=[0.6, 0.35, 0.05]),
    })

    return {"customers": customers, "accounts": accounts, "transactions": transactions, "loans": loans}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    SAMPLE.mkdir(parents=True, exist_ok=True)
    for name, df in generate(args.rows, args.seed).items():
        df.to_csv(RAW / f"{name}.csv", index=False)
        df.head(100).to_csv(SAMPLE / f"{name}.csv", index=False)
        print(f"{name}: {len(df)} rows")


if __name__ == "__main__":
    main()
