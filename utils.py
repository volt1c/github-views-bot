def to_int_or(number: str, default_value: int = 0) -> int:
    return int(number) if number.isdigit() else default_value
