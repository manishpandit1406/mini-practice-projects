def dollar_rupee(dollar):
    inr = dollar * 84.68
    print(inr,"INR")

def euro_rupee(euro):
    inr = euro * 88.96
    print(inr,"INR")

def yen_rupee(yen):
    inr = yen * 0.56
    rounded_number = round(inr, 2)
    print(rounded_number,"INR")


def ruble_rupee(ruble):
    inr = ruble * 0.80
    print(inr,"INR")

def yuan_rupee(yuan):
    inr = yuan * 11.65
    print(inr,"INR")
    # '{0:.2f}'.format(inr)
currency = input("Enter the currency: ")
if currency == "dollar" :
    dollar_rupee(dollar = int(input("Enter the dollar: ")))
elif currency == "euro" :
    euro_rupee(euro = int(input("Enter the euro: ")))
elif currency == "yen" :
    yen_rupee(yen = int(input("Enter the yen: ")))
elif currency == "ruble" :
    ruble_rupee(ruble = int(input("Enter the ruble: ")))
elif currency == "yuan" :
    yuan_rupee(yuan = int(input("Enter the yuan: ")))
else:
    print("Invalid currency")

# f'{pi:.2f}'