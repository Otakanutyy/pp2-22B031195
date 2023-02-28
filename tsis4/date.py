import datetime
#1
tday = datetime.date.today()
tdelta = datetime.timedelta(days=5)
print(tday-tdelta)

#2
tdelta2 = datetime.timedelta(days=1)
print(tday-tdelta2, tday, tday+tdelta2)

#3
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
hours = int(input('Enter the hour: '))
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))
microseconds = int(input('Enter the microseconds: '))
d = datetime.datetime(year, month, day, hours, minutes, seconds, microseconds).replace(microsecond=0)
print(d)

#4
year1 = int(input('Enter a year: '))
month1 = int(input('Enter a month: '))
day1 = int(input('Enter a day: '))
sday1=datetime.date(year1, month1, day1)
year2 = int(input('Enter a year: '))
month2 = int(input('Enter a month: '))
day2 = int(input('Enter a day: '))
sday2=datetime.date(year2, month2, day2)
diffday=abs(sday2-sday1)
print(diffday.total_seconds())