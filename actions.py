"""Module demonstrating safe division with proper error handling."""

DIVISOR_START = 0
DIVIDEND = 10


def safe_division():
    """Attempt division while safely handling division by zero."""
    divisor = DIVISOR_START

    while True:
        try:
            result = DIVIDEND / divisor
            print(result)
            break
        except ZeroDivisionError:
            divisor += 1
