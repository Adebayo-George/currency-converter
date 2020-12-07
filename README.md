# currency-converter
This is a simple code that helps to convert just three currencies USD, EURO, NGN to their equivalents. 
amount = eval(input("Please Enter Amount: "))
CurrencyDenomination = input("NGN or USD or EURO: ")
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
