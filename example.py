from dataclasses import dataclass, asdict
import datetime
import json
from typing import List

# Models
@dataclass
class Day():
    day: int
    open: bool
    marketOpen: int
    lastDeliveryMinute: int
    
@dataclass    
class Holiday():
    date: datetime.date
    open: bool
    marketOpen: int
    lastDeliveryMinute: int
    
@dataclass
class DeliveryNotificationTimes():
    days: List[Day]
    
  
# Database  
sunday = Day(day=0, open=False, marketOpen=0, lastDeliveryMinute=0)
monday = Day(day=1, open=True, marketOpen=0, lastDeliveryMinute=1320)
tuesday = Day(day=2, open=True, marketOpen=0, lastDeliveryMinute=1320)
wednesday = Day(day=3, open=True, marketOpen=0, lastDeliveryMinute=1320)
thursday = Day(day=4, open=True, marketOpen=0, lastDeliveryMinute=1320)
friday = Day(day=5, open=True, marketOpen=0, lastDeliveryMinute=1320)
saturday = Day(day=6, open=False, marketOpen=0, lastDeliveryMinute=0)


x_day = Holiday(date=datetime.date(2022, 9, 27), open=False, marketOpen=0, lastDeliveryMinute=0)
y_day = Holiday(date=datetime.date(2022, 9, 30), open=False, marketOpen=0, lastDeliveryMinute=0)
z_day = Holiday(date=datetime.date(2022, 10, 3), open=False, marketOpen=0, lastDeliveryMinute=0)

dnt = DeliveryNotificationTimes(days=[monday, tuesday, wednesday, thursday, friday, saturday, sunday])

holidays = [x_day, y_day, z_day]


# Views
def get_holidays_for_the_week(date: datetime):
    """
    Returns the day of the week which is a holiday as an integer.
    Args:
        date: date of the day
    """
    start_date = date - datetime.timedelta(days=date.weekday())
    end_date = start_date + datetime.timedelta(days=6)
    print(end_date)
   
    days = [holiday for holiday in holidays if start_date <= holiday.date <= end_date]
    return days


today = datetime.date.today()

holidays_for_the_week = get_holidays_for_the_week(today)
print(holidays_for_the_week)

for holiday in holidays_for_the_week:
    for day in dnt.days:
        if holiday.date.weekday() == day.day:
            day.open = holiday.open
            day.marketOpen = holiday.marketOpen
            day.lastDeliveryMinute = holiday.lastDeliveryMinute
            day.is_holiday = True

# print(dnt)
print(json.dumps(asdict(dnt), indent=2))


