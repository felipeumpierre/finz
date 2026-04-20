from decimal import Decimal
from pathlib import Path
import pytest

FIXTURES = Path(__file__).parent / "fixtures"

@pytest.fixture
def fixtures_dir():
    return FIXTURES

@pytest.fixture
def D():
    """Shorthand for Decimal construction from strings."""
    return Decimal
