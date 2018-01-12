import mechanicalsoup
import json
from pprint import pprint
browser = mechanicalsoup.StatefulBrowser()
response=browser.open("https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json")
pprint(response.text)
data1 = json.loads(response.text)
print(data1["advances"])
print(data1["declines"])


