import requests
from datetime import datetime, timezone, timedelta
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
            transaction_id = len(history) + 1
            
            reference = "SWX-" + str(transaction_id)
            history.append({
                "transaction_id": transaction_id,
                "date": transaction_date,
                "status": status,
                "reference": reference
            })
            continue
    data = response.json()
    rate = data["rate"]
    status = "Successful"

    transaction_time = datetime.now(timezone(timedelta(hours=2))).strftime("%Y-%m-%d %H:%M:%S")
    transaction_date = transaction_time.split()[0]
    transaction_id = len(history) + 1
    reference = "SWX-" +str(transaction_id)
    converted = amount * rate

    history.append({"transaction_id": transaction_id, "time": transaction_time, "date": transaction_time.split() [0], "amount": amount, "from_currency": from_currency, "converted": converted, "to_currency": to_currency, "rate": rate, "status": status, "reference": reference})

    choice = input("Enter transaction number: ")
    try:
        choice = int(choice)
    except ValueError:
            print("Please enter a valid transaction number.")
            continue
    if choice < 1 or choice > len(history):
        print("Invalid transaction number. ")
        continue
    selected_transaction = history[choice - 1]
    print(selected_transaction)

    print("\n--- Transaction Details---")
    print("Transaction ID:", selected_transaction["transaction_id"])

    print("Date:", selected_transaction["date"])
    print("Time:", selected_transaction["time"])
    print("Amount:", selected_transaction["amount"])
    print("From Currency:", selected_transaction["from_currency"])
    print("Converted Amount:", selected_transaction["converted"])
    print("Conversion:", selected_transaction["amount"], selected_transaction["from_currency"], "to", selected_transaction["converted"], selected_transaction["to_currency"])
    print("To Currency:", selected_transaction["to_currency"])
    print("Rate:", selected_transaction["rate"])
    print("Status:", selected_transaction["status"])
    print("Reference:", selected_transaction["reference"])
    print("--- End of Transaction Details ---")
    status = "successful"

    print("you Converted", amount, from_currency, "to", converted, to_currency)
    again = input("Do you want to convert again? (yes/no): ").lower()
    if again != "yes":
        break
    print("REACHED HISTORY")
print("\nConversion History:")
filter_status = input("Filter by status (successful/failed/pending/cancelled/all): ").lower()
for i, item in enumerate(history, 1):

    if filter_status == "all" or item["status"].lower() == filter_status:
        print(i, item["reference"] ,item["status"].upper())

choice = input("Enter transaction number: ")
choice = int(choice)
if choice < 1 or choice > len(history):
    print("Please enter a valid transaction_number")
else:
    selected_transaction = history[choice - 1]
    print("===== SWIFT EXCHANGE TRANSACTION RECEIPT =====")
    print("==============================")
    print("Transanction ID:", selected_transaction["transaction_id"])
    print("Date:", selected_transaction["date"])
    print("Time:", selected_transaction["time"])
    print("Amount:", selected_transaction["amount"], selected_transaction["from_currency"])
    print("From:", selected_transaction["from_currency"])
    print("to:", selected_transaction["to_currency"])
    print("Converted:", selected_transaction["converted"], selected_transaction["to_currency"])
    print("Exchange rate:", selected_transaction["rate"], selected_transaction["from_currency"], "=", selected_transaction["to_currency"])
    print("Status:", selected_transaction["status"].upper())
    print("Reference:", selected_transaction["reference"].upper())