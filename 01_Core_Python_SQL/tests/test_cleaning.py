import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.cleaning import drop_duplicate_ids  # noqa: E402


def test_drop_duplicate_ids():
    df = pd.DataFrame({"id": [1, 1, 2], "v": ["a", "b", "c"]})
    out = drop_duplicate_ids(df, "id")
    assert len(out) == 2
    assert out.loc[0, "v"] == "a"
