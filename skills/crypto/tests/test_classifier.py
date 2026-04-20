from pathlib import Path
import yaml

TAXONOMY = Path(__file__).parent.parent / "references" / "transaction-taxonomy.yaml"

def test_taxonomy_loads():
    data = yaml.safe_load(TAXONOMY.read_text())
    assert data["version"] == 1
    assert len(data["rules"]) > 20

def test_taxonomy_has_fiat_list():
    data = yaml.safe_load(TAXONOMY.read_text())
    assert "EUR" in data["fiat_coins"]
    assert "BRL" in data["fiat_coins"]

def test_every_rule_has_classify():
    data = yaml.safe_load(TAXONOMY.read_text())
    for rule in data["rules"]:
        assert "classify" in rule
        assert "match" in rule

from decimal import Decimal
from scripts.schemas import NormalizedRow
from scripts.classifier import Classifier

def _row(source, op, coin="BTC", change="1", account=None):
    return NormalizedRow(
        id="t-1", source=source, timestamp="2022-01-01T00:00:00+00:00",
        raw_operation=op, coin=coin, change=Decimal(change), account=account,
    )

def test_binance_fiat_deposit_is_fiat_movement():
    c = Classifier.load_default()
    assert c.classify(_row("binance", "Deposit", coin="EUR", change="100")).classified_as == "fiat_movement"

def test_binance_crypto_deposit_is_external_in():
    c = Classifier.load_default()
    assert c.classify(_row("binance", "Deposit", coin="BTC", change="1")).classified_as == "external_in"

def test_binance_simple_earn_interest_is_income():
    c = Classifier.load_default()
    assert c.classify(_row("binance", "Simple Earn Flexible Interest", coin="XRP", change="0.1")).classified_as == "income_receipt"

def test_binance_simple_earn_subscription_is_non_taxable():
    c = Classifier.load_default()
    assert c.classify(_row("binance", "Simple Earn Flexible Subscription", coin="XRP", change="-1")).classified_as == "non_taxable_transfer"

def test_binance_convert_is_swap_leg():
    c = Classifier.load_default()
    assert c.classify(_row("binance", "Binance Convert")).classified_as == "crypto_swap_leg"

def test_coinbase_send_is_external_out():
    c = Classifier.load_default()
    assert c.classify(_row("coinbase", "Send", change="-1")).classified_as == "external_out"

def test_unknown_op_falls_back_to_review():
    c = Classifier.load_default()
    assert c.classify(_row("binance", "Totally New Operation")).classified_as == "airdrop_pending_review"
