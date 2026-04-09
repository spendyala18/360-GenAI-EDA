try:
    from src.kpi_city import city_kpi
except ImportError:
    # Fallback if the file is still in the root folder
    from kpi_city import city_kpi

def test_city_kpi_happy_path():
    """Verify that a valid city returns data."""
    result = city_kpi("Mumbai")
    assert result is not None
    assert result[0] > 0

def test_city_kpi_injection_attempt():
    """Verify that an injection string does not return all rows."""
    result = city_kpi("Mumbai' OR 1=1 --")
    assert result is None