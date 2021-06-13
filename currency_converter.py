import requests
url='https://api.exchangerate-api.com/v4/latest/USD' # FREE API
response=requests.get(url)# GET API
data=response.json() # LOAD JSON FILE
rate=data['rates'] # LOAD RATE DICT
currencies= data['rates'].keys()
len(currencies)
currencies=list(currencies)
item=0
print("\n\t\t\t\t\t\t   CURRENCY CODE \t\t\t\t\t\t\t\n")
print("............................................................................................................................................\n")
while item <160:
    i=0
    while i< 10:
        print('   '+currencies[item],end='     ') # PRINTING AVAILABLE CURRENCY CODES
        i+=1
        item+=1
    print('\n\n' )
print("............................................................................................................................................\n\n")
user= input("Enter the code of currency you want to convert to USD from above : ") # READING USER CHOICE
value=eval(input("Enter the amount : ")) # READING AMOUNT
USD=value/rate.get(user) # CONVERT TO USD
print("Amount in USD : $", USD,'\n\n') #PRINTING USD
