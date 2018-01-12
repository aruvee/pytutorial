from datetime import datetime
import pytz
today=datetime.now(pytz.timezone('Asia/Kolkata'))
print(today.minute)
