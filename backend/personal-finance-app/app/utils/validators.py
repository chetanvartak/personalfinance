def validate_currency_code(code: str) -> bool:
    return len(code) == 3 and code.isalpha()
