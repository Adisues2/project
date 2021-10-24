import datetime 

today_date = datetime.date.today()
print(today_date)

x =datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))


current_time = datetime.datetime.now()
next_jaunary = datetime.datetime(2022,1,1)
time_left =next_jaunary-current_time
print(f"the 1st of january in {time_left} hours")

year_s = int(input("enter a year"))
month_s = int(input("enter a month"))
day_s = int(input("enter a day"))

birthdate = datetime.datetime.now()

result = birthdate.year_s ,birthdate.month_s,birthdate.day_s
print(result)

today_dates =datetime.datetime.today()
print(today_dates)

current_times = datetime.datetime.now()

next_holiday = datetime.datetime(2021,9,19)

remain_holiday = next_holiday-current_times
print(f"the next holidays is in {remain_holiday} hours")

datess = datetime.datetime.now()
print(datess.second)
print('helloworld')

from faker import Faker
fake = Faker()
users = {}
print(f'name: {fake.name()}')
print(f'address: {fake.address()}')

print(f'text: {fake.text()}')



