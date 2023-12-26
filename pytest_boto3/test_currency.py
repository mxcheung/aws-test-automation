class Currency:
    def __init__(self, currency_code, account):
        self.currency_code = currency_code
        self.account = account

# Sample list of currency objects
currency_list = [
    Currency("USD", "Account1"),
    Currency("EUR", "Account2"),
    Currency("GBP", "Account3"),
    # ... add more currencies as needed
]

# Check if the list contains a currency with code "USD"
usd_exists = False
for currency in currency_list:
    if currency.currency_code == "USD":
        usd_exists = True
        break

if usd_exists:
    print("The list contains a currency with code USD.")
else:
    print("The list does not contain a currency with code USD.")



usd_exists = any(currency.currency_code == "USD" for currency in currency_list)

if usd_exists:
    print("The list contains a currency with code USD.")
else:
    print("The list does not contain a currency with code USD.")


class Currency:
    def __init__(self, currency_code, account):
        self.currency_code = currency_code
        self.account = account

# Sample list of currency objects
currency_list = [
    Currency("USD", "Account1"),
    Currency("EUR", "Account2"),
    Currency("GBP", "Account3"),
    # ... add more currencies as needed
]

# Find the currency object with code "USD"
usd_currency = None
for currency in currency_list:
    if currency.currency_code == "USD":
        usd_currency = currency
        break

if usd_currency is not None:
    print("Found the currency object with code USD:")
    print(f"Currency Code: {usd_currency.currency_code}")
    print(f"Account: {usd_currency.account}")
else:
    print("No currency object found with code USD.")

