import requests
from datetime import datetime
history = []
account = {
    "user_id": "USR-0001",
    "name": "Test User",
    "status": "Active",
    "verification": "Verified",
    "permission": "Allowed",
    "transaction_limit": 1000
}
while True:
    if account["status"] != "Active":
        status = "Failed"
        print("Account is not active")
        continue
    if account["verification"] !="Verified":
        status = "Failed"
        print("Account verification is not valid")
        continue
    if account["permission"] !="Allowed":
        status = "Failed"
        print("Transaction permission denied")
        continue
    amount = float(input("Enter amount: "))

    if amount > account["transaction_limit"]:
        status = "Failed"
        print("Transaction amount exceeds your limit")
        status = "failed"
        continue

    if amount <= 0:
        print("Amount must be greater than 0.")
        status = "Failed"
        continue

    print("Supported currencies: USD, EUR, GBP, MWK")
    from_currency = input("Enter currency you are converting from: ").upper()

    to_currency = input("Enter currency you are converting to: ").upper()

    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"
    response = requests.get(url)
    status = "Failed"
    if response.status_code != 200:
            print("Sorry, we could not get the exchange rate.")
            status = "Failed"
            continue
    data = response.json()
    rate = data["rate"]
    status = "Successful"

    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    transaction_id = len(history) + 1
    reference = "SWX-" +str(transaction_id)
    converted = amount * rate

    history.append(f"Transaction {transaction_id} | {transaction_time} - {amount} {from_currency} to {converted} {to_currency} | Rate: {rate} | Status: {status} | Reference: {reference}")
    status = "successful"

    print("you Converted", amount, from_currency, "to", converted, to_currency)
    again = input("Do you want to convert again? (yes/no): ").lower()
    if again != "yes":
        break
print("\nConversion History:")
for item in history:
        print(item)