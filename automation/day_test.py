import datetime

# 현재 날짜 출력
today = datetime.datetime.now()
print("현재 날짜:", today)

# 40일 뒤 날짜 출력
delta = datetime.timedelta(days=40)
future_date = today + delta
print("40일 뒤 날짜:", future_date)
