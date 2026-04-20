from decimal import Decimal
from pathlib import Path
import json
import pytest
from scripts.price_resolver import PriceResolver

@pytest.fixture
def cache_dir(tmp_path):
    d = tmp_path / "prices"
    d.mkdir()
    return d

def test_returns_cached_price_without_http(cache_dir):
    cache_file = cache_dir / "BTC" / "2021-05-13.json"
    cache_file.parent.mkdir(parents=True)
    cache_file.write_text(json.dumps({"eur": "42000.50"}))
    r = PriceResolver(cache_dir=cache_dir, http_client=None)
    assert r.resolve("BTC", "2021-05-13T23:00:23+02:00") == Decimal("42000.50")

def test_manual_override_beats_cache(cache_dir):
    (cache_dir / "BTC").mkdir()
    (cache_dir / "BTC" / "2021-05-13.json").write_text(json.dumps({"eur": "1"}))
    r = PriceResolver(cache_dir=cache_dir, http_client=None,
                      manual_prices=[{"coin": "BTC", "date": "2021-05-13", "eur_price": "99999"}])
    assert r.resolve("BTC", "2021-05-13T00:00:00+00:00") == Decimal("99999")

def test_fetches_and_caches_when_missing(cache_dir, monkeypatch):
    class FakeClient:
        def get(self, url, params=None, timeout=None):
            class R:
                status_code = 200
                def json(self):
                    return {"market_data": {"current_price": {"eur": 3000.0}}}
                def raise_for_status(self): pass
            return R()
    r = PriceResolver(cache_dir=cache_dir, http_client=FakeClient())
    price = r.resolve("ETH", "2022-01-01T00:00:00+00:00")
    assert price == Decimal("3000")
    cached = (cache_dir / "ETH" / "2022-01-01.json").read_text()
    assert "3000" in cached

def test_raises_missing_price_when_no_source(cache_dir):
    r = PriceResolver(cache_dir=cache_dir, http_client=None)
    with pytest.raises(PriceResolver.MissingPriceError):
        r.resolve("XYZ", "2022-01-01T00:00:00+00:00")
