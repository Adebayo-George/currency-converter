# Ask user for amount input
amount = eval(input("Please Enter Amount: "))
# Ask user for the currency denomination they want
# NGN -> Nigerian Naira, USD -> United States Dollar, EURO -> Euro
CurrencyDenomination = input("NGN or USD or EURO: ")
# When currency denomination is lowercase changes it to uppercase
# If NGN it converts the currency to either USD or EURO
# If EURO or USD it converts the currency to NGN
if CurrencyDenomination.upper() == "NGN": 
    print("Do you want currency value in USD or EURO?")
    new_entry = input("USD or EURO: ")
    if new_entry.upper() == "USD":
        conversion = amount/381.45
        print(f"{amount}NGN in USD is", round(conversion, 2))
    else:
        conversion = amount/450.68
        print(f"{amount}NGN in USD is", round(conversion, 2))
elif CurrencyDenomination.upper() == "USD":
    print("Currency value will be in NGN")
    conversion = amount * 381.45
    print(f"{amount}USD in NGN is", round(conversion, 2))
elif CurrencyDenomination.upper() == "EURO":
    print("Currency value will be NGN")
    conversion = amount * 450.68
    print(f"{amount}EURO in NGN is", round(conversion, 2))
else:
    print("Currency denomination not found!")
