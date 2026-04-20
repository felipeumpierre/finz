"""Rule-based classifier mapping NormalizedRow → classified intermediate category.

The output `classified_as` is sometimes a *leg* category (e.g., trade_buy_leg)
meaning pairing.py must still combine it with its counterpart rows before
producing final tax events.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml

from scripts.schemas import NormalizedRow

TAXONOMY_PATH = Path(__file__).parent.parent / "references" / "transaction-taxonomy.yaml"


@dataclass
class ClassificationResult:
    classified_as: str


class Classifier:
    def __init__(self, rules: list[dict], fiat_coins: set[str], fallback: str):
        self.rules = rules
        self.fiat_coins = fiat_coins
        self.fallback = fallback

    @classmethod
    def load_default(cls, path: Path = TAXONOMY_PATH) -> "Classifier":
        data = yaml.safe_load(path.read_text())
        return cls(
            rules=data["rules"],
            fiat_coins=set(data["fiat_coins"]),
            fallback=data["fallback_classification"],
        )

    def _match(self, rule: dict, row: NormalizedRow) -> bool:
        m = rule["match"]
        if m.get("source") and m["source"] != row.source:
            return False
        if m.get("raw_operation") and m["raw_operation"] != row.raw_operation:
            return False
        when = rule.get("when")
        if when:
            if "coin_is_fiat" in when:
                is_fiat = row.coin in self.fiat_coins
                if when["coin_is_fiat"] is not is_fiat:
                    return False
        return True

    def classify(self, row: NormalizedRow) -> ClassificationResult:
        for rule in self.rules:
            if self._match(rule, row):
                return ClassificationResult(classified_as=rule["classify"])
        return ClassificationResult(classified_as=self.fallback)
