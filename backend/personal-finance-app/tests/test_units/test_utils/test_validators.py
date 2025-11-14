from app.utils.validators import validate_currency_code

def test_validate_currency_code():
    assert validate_currency_code('USD')
    assert not validate_currency_code('US')
