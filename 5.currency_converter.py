#get amount
#check_currency
#calculation


currency_list = ('usd','eur','cad')

exchage_rates = { 'usd': {'eur':0.85 ,'cad': 1.13},
                   'eur':{'usd': 1.18, 'cad': 1.47},
                    'cad': {'usd': 0.80, 'eur': 0.68} 
                    }

def get_amount():
    while True:
        amount = input("Enter the amount to be converted: ")
        try:
            validated_amount = float(amount)
            if(validated_amount>0):
                return validated_amount
            else:
                raise ValueError
        except ValueError:
            print("invalid_value")

def check_currency(label):
    while True:
        currency_selected = input(f'{label} (USD/CAD/EUR): ').lower()
        if (currency_selected not in currency_list):
            print("invalid currency")
        else:
            return currency_selected


def convert( amount,source_currency,target_currency):
        if (source_currency == target_currency):
            return amount
        return amount * exchage_rates[source_currency][target_currency]


amount = get_amount()
source_currency = check_currency("source_currency")
target_currency = check_currency("target_currency")
converted_amount = convert(amount,
                        source_currency=source_currency, 
                        target_currency= target_currency)

print(f'{amount} {source_currency} is equal to {converted_amount:.2f} of {target_currency}')



       



    
    






 


        
    
