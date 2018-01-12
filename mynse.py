from nsetools import  Nse
nse = Nse()

stype = input("Enter the Stock type")
symbol = input("Enter the Stock name")
if stype == "stock":
    stockQuote = nse.get_quote(symbol)
elif stype == "index":
    stockQuote = nse.get_index_quote(symbol)
print(stockQuote['lastPrice'])
