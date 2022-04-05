# pylint: disable=missing-docstring


RATES = { "USDEUR":0.85,"GBPEUR":1.13,"CHFEUR":0.86,"EURGBP":0.885}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string like "USD"
    """
    key= amount[1] + currency
    if key in RATES:
        currency_value=RATES[key]
        conversion=round(currency_value*amount[0])
        return conversion
    return None
